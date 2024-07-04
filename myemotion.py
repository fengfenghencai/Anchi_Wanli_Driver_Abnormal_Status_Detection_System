import cv2  # 图像处理的库 OpenCv
import dlib  # 人脸识别的库 dlib
import numpy as np  # 数据处理的库 numpy


# 使用dlib.get_frontal_face_detector() 获得脸部位置检测器
detector = dlib.get_frontal_face_detector()
# 使用dlib.shape_predictor获得脸部特征位置检测器
predictor = dlib.shape_predictor('weights/shape_predictor_68_face_landmarks.dat')
EMOTIONS = ['nature', 'suprise', 'happy', 'angry']
def emotion_dec(frame):
    # 眉毛直线拟合数据缓冲
    line_brow_x = []
    line_brow_y = []
    label = 0

    img_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = detector(img_gray, 0)

    # 如果检测到人脸
    if (len(faces) != 0):

        # 对每个人脸都标出68个特征点
        for i in range(len(faces)):
            # enumerate 方法同时返回数据对象的索引和数据，k为索引，d为faces中的对象
            for k, d in enumerate(faces):
                # 计算人脸识别框边长
                face_width = d.right() - d.left()

                # 使用预测器得到68点数据的坐标
                shape = predictor(frame, d)

                # 分析任意 n 点的位置关系来作为表情识别的依据
                # 嘴中心	66，嘴左角48，嘴右角54
                mouth_width = (shape.part(54).x - shape.part(48).x) / face_width  # 嘴巴张开程度
                mouth_height = (shape.part(66).y - shape.part(62).y) / face_width  # 嘴巴张开程度
                # print("嘴巴宽度与识别框宽度之比：" , mouth_width)
                # print("嘴巴高度与识别框宽度之比：" , mouth_height)

                # 通过两个眉毛上的10个特征点，分析挑眉程度和皱眉程度
                brow_sum = 0  # 高度之和
                frown_sum = 0  # 两边眉毛距离之和
                for j in range(17, 21):
                    brow_sum += (shape.part(j).y - d.top()) + (shape.part(j + 5).y - d.top())
                    frown_sum += shape.part(j + 5).x - shape.part(j).x
                    line_brow_x.append(shape.part(j).x)
                    line_brow_y.append(shape.part(j).y)

                # self.brow_k, self.brow_d = self.fit_slr(line_brow_x, line_brow_y) # 计算眉毛的倾斜程度
                tempx = np.array(line_brow_x)
                tempy = np.array(line_brow_y)
                z1 = np.polyfit(tempx, tempy, 1)  # 拟合成一次直线
                brow_k = -round(z1[0], 3)  # 拟合出曲线的斜率和实际眉毛的倾斜方向是相反的

                brow_height = (brow_sum / 10) / face_width  # 眉毛高度占比
                brow_width = (frown_sum / 5) / face_width  # 眉毛距离占比
                # print("眉毛高度与识别框宽度之比：" , brow_height)
                # print("眉毛间距与识别框高度之比：" , brow_width)

                # 眼睛睁开程度
                eye_sum = (shape.part(41).y - shape.part(37).y + shape.part(40).y - shape.part(38).y +
                           shape.part(47).y - shape.part(43).y + shape.part(46).y - shape.part(44).y)
                eye_hight = (eye_sum / 4) / face_width
                # print("眼睛睁开距离与识别框高度之比：" , eye_hight)

                if round(mouth_height >= 0.038):
                    if eye_hight >= 0.033:  # 改阈值来判断
                        label = 1
                    else:
                        label = 2

                # 没有张嘴，可能是正常和生气，通过眉毛区分
                else:
                    if brow_k <= -0.005:
                        label = 3
                    else:
                        label = 0
        return label
    return label


