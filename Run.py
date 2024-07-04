import sys
import cv2
import datetime
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QTimer, QCoreApplication, QDateTime
from PyQt5.QtGui import QPixmap, QImage, QTextCursor
from UI_window import Ui_MainWindow
import myframe
import qimage2ndarray

class CameraShow(QMainWindow, Ui_MainWindow):

    def __del__(self):
        try:
            self.camera.release()  # 释放资源
        except:
            return

    def __init__(self, parent=None):
        super(CameraShow, self).__init__(parent)
        self.setupUi(self)
        self.Timer = QTimer()
        self.timer = QTimer()
        self.Timer.timeout.connect(self.show_img)
        self.timer.timeout.connect(self.showTime)
        self.PrepCamera()
        self.CallBackFunctions()
        self.showTime()

        self.case = 0
        self.Image_num = 0

        self.EMOTIONS = ['自然', '惊讶', '高兴', '生气']



    # prepare
    def PrepCamera(self):
        try:
            self.camera = cv2.VideoCapture(0)
            self.Image_num = 0
            self.Msg.clear()
            self.Msg.append('Oboard camera connected.')
            self.Msg.setPlainText()
            self.showTime()
        except Exception as e:
            self.Msg.clear()
            self.Msg.append(str(e))

    # 按钮的点击事件
    def CallBackFunctions(self):
        self.btntestcamera.clicked.connect(self.testCamera) # ok
        self.btn_start.clicked.connect(self.StartDection)
        self.btnexit.clicked.connect(self.ExitApp)

    # 显示时间
    def showTime(self):
        # time = QDateTime.currentDateTime()
        now_time = datetime.datetime.now()

        self.timer.start()
        # timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        hour = now_time.strftime('%H')
        minute = now_time.strftime('%M')
        second = now_time.strftime('%S')
        self.TimeHourLCD.display(hour)
        self.TimeMinuteLCD.display(minute)
        self.TimeSecondLCD.display(second)

    # 打开相机
    def testCamera(self):
        if self.Timer.isActive() == False:
            flag = self.camera.open(0)
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)
            else:
                self.printf('正在使用相机功能', 2)
                self.case = 1
                self.timelb = time.time()
                self.btntestcamera.setText(u'关闭相机')
                self.btn_start.setEnabled(False)
                self.Image_num = 0
                self.Timer.start(30)
        else:
            self.printf('已关闭相机功能', 2)
            self.Timer.stop()
            self.camera.release()
            # self.Camera.clear()
            self.Camera_2.clear()
            self.btntestcamera.setText(u'打开相机')
            self.btn_start.setEnabled(True)

    # 检测功能
    def StartDection(self):
        if self.Timer.isActive() == False:
            flag = self.camera.open(0)
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"请检测相机与电脑是否连接正确",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)
            else:
                self.printf('正在运行驾驶检测', 2)
                self.case = 2
                self.timelb = time.time()
                # 眼睛闭合判断
                self.EYE_AR_THRESH = 0.15  # 眼睛长宽比
                self.EYE_AR_CONSEC_FRAMES = 2  # 闪烁阈值

                # 嘴巴开合判断
                self.MAR_THRESH = 0.65  # 打哈欠长宽比
                self.MOUTH_AR_CONSEC_FRAMES = 3  # 闪烁阈值

                # 定义检测变量，并初始化
                self.COUNTER = 0  # 眨眼帧计数器
                self.TOTAL = 0  # 眨眼总数
                self.mCOUNTER = 0  # 打哈欠帧计数器
                self.mTOTAL = 0  # 打哈欠总数
                self.ActionCOUNTER = 0  # 分心行为计数器器

                # 情绪判断变量
                self.emotionCOUNTER = 0
                self.countEMOS = [0, 0, 0, 0]

                # 疲劳判断变量
                # Perclos模型
                # perclos = (Rolleye/Roll) + (Rollmouth/Roll)*0.2
                self.Roll = 0  # 整个循环内的帧技术
                self.Rolleye = 0  # 循环内闭眼帧数
                self.Rollmouth = 0  # 循环内打哈欠数
                self.btn_start.setText(u'停止运行')
                self.btntestcamera.setEnabled(False)
                self.Timer.start(30)

        else:
            self.printf('已关闭驾驶检测功能', 2)
            self.Timer.stop()
            self.camera.release()
            self.Camera_2.clear()
            self.btn_start.setText(u'开始运行')
            self.btntestcamera.setEnabled(True)

    def StartDection_fun(self):
        # 检测
        # 将摄像头读到的frame传入检测函数myframe.frametest()
        ret, frame, label_emo = myframe.frametest(self.img)
        lab, eye, mouth = ret
        # ret和frame，为函数返回
        # ret为检测结果，ret的格式为[lab,eye,mouth],lab为yolo的识别结果包含'phone' 'smoke' 'drink',eye为眼睛的开合程度（长宽比），mouth为嘴巴的开合程度
        # frame为标注了识别结果的帧画面，画上了标识框

        # 分心行为判断
        # 分心行为检测以15帧为一个循环
        self.ActionCOUNTER += 1

        # 如果检测到分心行为
        # 将信息返回到前端ui，使用红色字体来体现
        # 并加ActionCOUNTER减1，以延长循环时间
        for i in lab:
            if (i == "phone"):
                self.Danger_state1.setText("<font color=red>正在用手机 请不要分心</font>")
                self.printf('使用了手机')
                if self.ActionCOUNTER > 0:
                    self.ActionCOUNTER -= 1
            elif (i == "smoke"):
                self.Danger_state1.setText("<font color=red>正在抽烟 请不要分心</font>")
                self.printf('抽烟行为')
                if self.ActionCOUNTER > 0:
                    self.ActionCOUNTER -= 1
            elif (i == "drink"):
                self.Danger_state1.setText("<font color=red>正在喝水 请不要分心</font>")
                self.printf('喝水行为')
                if self.ActionCOUNTER > 0:
                    self.ActionCOUNTER -= 1

        # 如果超过15帧未检测到分心行为，将label修改为平时状态
        if self.ActionCOUNTER == 15:
            self.Danger_state1.setText("")
            self.ActionCOUNTER = 0

        # 情绪判断
        # 16帧更新一次
        self.emotionCOUNTER += 1
        self.countEMOS[label_emo] += 1
        if self.emotionCOUNTER == 16:
            pre_emotion = self.EMOTIONS[self.countEMOS.index(max(self.countEMOS))]
            for i, nums in enumerate(self.countEMOS):
                self.countEMOS[i] = round((nums / 16)*100, 2)
            self.one_LCD.display(self.countEMOS[0])
            self.two_LCD.display(self.countEMOS[1])
            self.three_LCD.display(self.countEMOS[2])
            self.four_LCD.display(self.countEMOS[3])
            self.Emotion.setText(pre_emotion if pre_emotion != '生气' else f'<font color=red>{pre_emotion}</font>')
            # print(self.EMOTIONS[self.countEMOS.index(max(self.countEMOS))])
            # print('max:', self.countEMOS.index(max(self.countEMOS)))
            self.emotionCOUNTER = 0
            self.countEMOS = [0, 0, 0, 0]

        # 疲劳判断
        # 眨眼判断
        if eye < self.EYE_AR_THRESH:
            # 如果眼睛开合程度小于设定好的阈值
            # 则两个和眼睛相关的计数器加1
            self.COUNTER += 1
            self.Rolleye += 1
        else:
            # 如果连续2次都小于阈值，则表示进行了一次眨眼活动
            if self.COUNTER >= self.EYE_AR_CONSEC_FRAMES:
                self.TOTAL += 1
                self.Blink_num.display(self.TOTAL)
                # 重置眼帧计数器
                self.COUNTER = 0

        # 哈欠判断，同上
        if mouth > self.MAR_THRESH:
            self.mCOUNTER += 1
            self.Rollmouth += 1
        else:
            # 如果连续3次都小于阈值，则表示打了一次哈欠
            if self.mCOUNTER >= self.MOUTH_AR_CONSEC_FRAMES:
                self.mTOTAL += 1
                self.Yawn_num.display(self.mTOTAL)
                self.printf('打了一次哈欠')
                # 重置嘴帧计数器
                self.mCOUNTER = 0

        # 将画面显示在前端UI上
        show = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        self.Camera_2.setPixmap(QPixmap(showImage))  # 展示图片
        self.Camera_2.show()
        # 疲劳模型
        # 疲劳模型以150帧为一个循环
        # 每一帧Roll加1
        self.Roll += 1
        # 当检测满150帧时，计算模型得分
        if self.Roll == 150:
            # 计算Perclos模型得分
            blink_fre = self.Rolleye / self.Roll
            yawn_fre = self.Rollmouth / self.Roll
            perclos = blink_fre + yawn_fre  # 打哈欠比例为0.2 为了更方便测试改大一点
            # 在前端UI输出perclos值、眨眼频率、哈欠频率
            self.Blink_fre.display(round(blink_fre*60, 3))
            self.Yawn_fre.display(round(yawn_fre*60, 3))
            self.PERCLOS.display(round(perclos, 3))
            self.printf("过去150帧中，Perclos得分为" + str(round(perclos, 3)))
            # 当过去的150帧中，Perclos模型得分超过0.38时，判断为疲劳状态
            if perclos > 0.38:
                self.printf("当前处于疲劳状态！！！")
                self.State.setText("<font color=red>疲劳！！！</font>")
            else:
                self.printf("当前处于清醒状态")
                self.State.setText("清醒")
            # 归零
            # 将三个计数器归零
            # 重新开始新一轮的检测
            self.Roll = 0
            self.Rolleye = 0
            self.Rollmouth = 0
            self.printf("重新开始执行新一轮的检测...\n")

    # 前台调度
    def show_img(self):
        success, self.img = self.camera.read()
        if success:
            # 帧率展示
            self.Image_num += 1
            if self.Image_num % 10 == 9:
                frame_rate = 10 / (time.time() - self.timelb)
                self.FmRateLCD.display(1+frame_rate)
                self.timelb = time.time()
                # 进行判断，通过case的值来看触发的是什么事件
            if self.case == 0:
                showImg = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
                showImg = qimage2ndarray.array2qimage(showImg)
                self.Camera_2.setPixmap(QPixmap(showImg))  # 展示图片
                self.Camera_2.show()
            elif self.case == 1:
                # ret, frame, label_emo = myframe.frametest(self.img)
                # show = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
                # self.Camera_2.setPixmap(QPixmap(showImage))  # 展示图片
                # self.Camera_2.show()
                showImg = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
                showImg = qimage2ndarray.array2qimage(showImg)
                self.Camera_2.setPixmap(QPixmap(showImg))  # 展示图片
                self.Camera_2.show()
            elif self.case == 2:
                self.StartDection_fun()
    # 退出程序
    def ExitApp(self, event):
        reply = QtWidgets.QMessageBox.question(self, '退出', '确定要退出吗?',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            if self.camera.isOpened():
                self.camera.release()
            if self.Timer.isActive():
                self.Timer.stop()
            if self.timer.isActive():
                self.timer.stop()
            QtWidgets.qApp.quit()  # 关闭应用程序
        else:
            if event:
                event.ignore()  # 忽略关闭事件



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = CameraShow()
    ui.show()
    sys.exit(app.exec_())
