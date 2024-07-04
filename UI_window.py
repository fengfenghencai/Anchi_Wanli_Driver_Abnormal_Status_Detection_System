# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLCDNumber
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1163, 820)
        MainWindow.setMaximumSize(QtCore.QSize(1600, 850))
        MainWindow.setStyleSheet("#MainWindow{border-image:url(./img_resource/bg.png);}")

        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(950, 730, 211, 31))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(190, 10, 521, 71))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 0, 511, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.TimeSecondLCD = QtWidgets.QLCDNumber(self.groupBox_3)
        self.TimeSecondLCD.setGeometry(QtCore.QRect(440, 20, 64, 36))
        self.TimeSecondLCD.setMaximumSize(QtCore.QSize(100, 16777215))
        self.TimeSecondLCD.setObjectName("TimeSecondLCD")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(200, 20, 81, 36))
        self.label_10.setStyleSheet("font: 11pt \"Adobe 黑体 Std R\";")
        self.label_10.setObjectName("label_10")
        self.FmRateLCD = QtWidgets.QLCDNumber(self.groupBox_3)
        self.FmRateLCD.setGeometry(QtCore.QRect(90, 20, 71, 36))
        self.FmRateLCD.setMaximumSize(QtCore.QSize(100, 16777215))
        self.FmRateLCD.setObjectName("FmRateLCD")
        self.TimeMinuteLCD = QtWidgets.QLCDNumber(self.groupBox_3)
        self.TimeMinuteLCD.setGeometry(QtCore.QRect(360, 20, 64, 36))
        self.TimeMinuteLCD.setMaximumSize(QtCore.QSize(100, 16777215))
        self.TimeMinuteLCD.setObjectName("TimeMinuteLCD")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(160, 20, 31, 36))
        self.label_13.setStyleSheet("font: 11pt \"Adobe 黑体 Std R\";")
        self.label_13.setObjectName("label_13")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(0, 20, 90, 36))
        self.label_12.setStyleSheet("font: 11pt \"Adobe 黑体 Std R\";")
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(350, 30, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(24)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.TimeHourLCD = QtWidgets.QLCDNumber(self.groupBox_3)
        self.TimeHourLCD.setGeometry(QtCore.QRect(280, 20, 71, 36))
        self.TimeHourLCD.setMaximumSize(QtCore.QSize(100, 16777215))
        self.TimeHourLCD.setObjectName("TimeHourLCD")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(430, 30, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(24)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.Msg = QtWidgets.QTextEdit(self.centralwidget)
        self.Msg.setGeometry(QtCore.QRect(260, 730, 661, 31))
        self.Msg.setObjectName("Msg")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(250, 190, 681, 531))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame_5)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 10, 661, 511))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.Camera_2 = QtWidgets.QLabel(self.groupBox_5)
        self.Camera_2.setGeometry(QtCore.QRect(10, 20, 640, 480))
        self.Camera_2.setText("")
        self.Camera_2.setObjectName("Camera_2")

        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(710, 10, 451, 71))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_6)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 0, 461, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.btntestcamera = QtWidgets.QPushButton(self.groupBox_4)
        self.btntestcamera.setGeometry(QtCore.QRect(15, 20, 121, 41))
        self.btntestcamera.setObjectName("btntestcamera")

        self.btn_start = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_start.setGeometry(QtCore.QRect(170, 20, 121, 41))
        self.btn_start.setObjectName("btn_start")
        self.btnexit = QtWidgets.QPushButton(self.groupBox_4)
        self.btnexit.setGeometry(QtCore.QRect(323, 20, 121, 41))
        self.btnexit.setObjectName("btnexit")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(930, 190, 231, 531))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.State_record = QtWidgets.QTextEdit(self.groupBox)
        self.State_record.setGeometry(QtCore.QRect(10, 20, 211, 561))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.State_record.setFont(font)
        self.State_record.setObjectName("State_record")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 50, 181, 61))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setTextFormat(QtCore.Qt.AutoText)
        self.label_11.setObjectName("label_11")

        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(30, 10, 131, 101))
        self.logo.setText("")
        self.logo.setObjectName("logo")
        # self.logo.setPixmap(QtGui.QPixmap("img_resource/logo.png"))
        # self.logo.setScaledContents(True)  # 可以根据需要调整是否按比例缩放图片

        self.logo_1 = QtWidgets.QLabel(self.centralwidget)
        self.logo_1.setGeometry(QtCore.QRect(20, 550, 221, 211))
        self.logo_1.setText("")
        self.logo_1.setObjectName("logo_1")
        self.logo_1.setPixmap(QtGui.QPixmap("img_resource/logo.png"))
        self.logo_1.setScaledContents(True)  # 可以根据需要调整是否按比例缩放图片

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 180, 221, 361))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")

        self.frame_8 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_8.setGeometry(QtCore.QRect(0, 210, 221, 51))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_28 = QtWidgets.QLabel(self.frame_8)
        self.label_28.setGeometry(QtCore.QRect(16, 0, 61, 51))
        self.label_28.setStyleSheet("font: 11pt \"Adobe 黑体 Std R\";")
        self.label_28.setObjectName("label_28")
        self.four_LCD = QtWidgets.QLCDNumber(self.frame_8)
        self.four_LCD.setGeometry(QtCore.QRect(80, 10, 71, 31))
        self.four_LCD.setObjectName("four_LCD")
        self.label_29 = QtWidgets.QLabel(self.frame_8)
        self.label_29.setGeometry(QtCore.QRect(160, 10, 61, 30))
        self.label_29.setObjectName("label_29")
        self.label_31 = QtWidgets.QLabel(self.frame_8)
        self.label_31.setGeometry(QtCore.QRect(190, 50, 61, 30))
        self.label_31.setObjectName("label_31")

        self.frame_9 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_9.setGeometry(QtCore.QRect(0, 150, 221, 51))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.three_LCD = QtWidgets.QLCDNumber(self.frame_9)
        self.three_LCD.setGeometry(QtCore.QRect(80, 10, 71, 31))
        self.three_LCD.setMinimumSize(QtCore.QSize(0, 30))
        self.three_LCD.setMaximumSize(QtCore.QSize(90, 16777215))
        self.three_LCD.setObjectName("three_LCD")
        self.label_22 = QtWidgets.QLabel(self.frame_9)
        self.label_22.setGeometry(QtCore.QRect(160, 10, 61, 30))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame_9)
        self.label_23.setGeometry(QtCore.QRect(16, 0, 61, 51))
        self.label_23.setStyleSheet("font: 11pt \"Adobe 黑体 Std R\";")
        self.label_23.setObjectName("label_23")

        self.frame_16 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_16.setGeometry(QtCore.QRect(0, 30, 221, 51))
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.label_27 = QtWidgets.QLabel(self.frame_16)
        self.label_27.setGeometry(QtCore.QRect(16, 0, 61, 51))
        self.label_27.setStyleSheet("font: 11pt \"Adobe 黑体 Std R\";")
        self.label_27.setObjectName("label_27")
        self.label_19 = QtWidgets.QLabel(self.frame_16)
        self.label_19.setGeometry(QtCore.QRect(160, 10, 61, 30))
        self.label_19.setObjectName("label_19")
        self.one_LCD = QtWidgets.QLCDNumber(self.frame_16)
        self.one_LCD.setGeometry(QtCore.QRect(80, 10, 70, 30))
        self.one_LCD.setMinimumSize(QtCore.QSize(0, 30))
        self.one_LCD.setMaximumSize(QtCore.QSize(90, 16777215))
        self.one_LCD.setObjectName("one_LCD")

        self.frame_17 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_17.setGeometry(QtCore.QRect(0, 90, 221, 51))
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.two_LCD = QtWidgets.QLCDNumber(self.frame_17)
        self.two_LCD.setEnabled(True)
        self.two_LCD.setGeometry(QtCore.QRect(80, 10, 71, 31))
        self.two_LCD.setMaximumSize(QtCore.QSize(1677, 16777215))
        self.two_LCD.setObjectName("two_LCD")
        self.label_32 = QtWidgets.QLabel(self.frame_17)
        self.label_32.setGeometry(QtCore.QRect(160, 10, 61, 30))
        self.label_32.setObjectName("label_32")
        self.label_34 = QtWidgets.QLabel(self.frame_17)
        self.label_34.setGeometry(QtCore.QRect(16, 0, 61, 51))
        self.label_34.setStyleSheet("font: 11pt \"Adobe 黑体 Std R\";")
        self.label_34.setObjectName("label_34")

        self.label_pred_img = QtWidgets.QLabel(self.groupBox_2)
        self.label_pred_img.setGeometry(QtCore.QRect(1, 20, 211, 331))
        self.label_pred_img.setText("")
        self.label_pred_img.setObjectName("label_pred_img")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(190, 80, 691, 101))
        self.widget.setObjectName("widget")
        self.frame_4 = QtWidgets.QFrame(self.widget)
        self.frame_4.setGeometry(QtCore.QRect(450, 0, 241, 51))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_21 = QtWidgets.QLabel(self.frame_4)
        self.label_21.setGeometry(QtCore.QRect(30, 0, 81, 51))
        self.label_21.setStyleSheet("font: 11pt \"Adobe 黑体 Std R\";")
        self.label_21.setObjectName("label_21")
        self.State = QtWidgets.QLabel(self.frame_4)
        self.State.setGeometry(QtCore.QRect(150, 0, 61, 51))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.State.setFont(font)
        self.State.setObjectName("State")
        self.frame_11 = QtWidgets.QFrame(self.widget)
        self.frame_11.setGeometry(QtCore.QRect(0, 0, 221, 101))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        self.frame_12.setGeometry(QtCore.QRect(0, 0, 221, 51))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.label_24 = QtWidgets.QLabel(self.frame_12)
        self.label_24.setGeometry(QtCore.QRect(0, 0, 71, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_36 = QtWidgets.QLabel(self.frame_12)
        self.label_36.setGeometry(QtCore.QRect(150, 10, 61, 30))
        self.label_36.setObjectName("label_36")

        self.Blink_num = QtWidgets.QLCDNumber(self.frame_12)
        self.Blink_num.setGeometry(QtCore.QRect(80, 10, 61, 31))
        self.Blink_num.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.Blink_num.setFont(font)
        self.Blink_num.setObjectName("Blink_num")
        self.Blink_num.setSegmentStyle(QLCDNumber.Flat)
        self.Blink_num.setStyleSheet("QLCDNumber { font-family: SimSun; font-size: 24px; }")

        self.frame_10 = QtWidgets.QFrame(self.frame_11)
        self.frame_10.setGeometry(QtCore.QRect(0, 50, 221, 51))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_17 = QtWidgets.QLabel(self.frame_10)
        self.label_17.setGeometry(QtCore.QRect(0, 0, 71, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_37 = QtWidgets.QLabel(self.frame_10)
        self.label_37.setGeometry(QtCore.QRect(150, 10, 61, 30))
        self.label_37.setObjectName("label_37")

        self.Blink_fre = QtWidgets.QLCDNumber(self.frame_10)
        self.Blink_fre.setGeometry(QtCore.QRect(80, 10, 61, 31))
        self.Blink_fre.setMaximumSize(QtCore.QSize(100, 50))
        self.Blink_fre.setObjectName("Blink_fre")
        self.Blink_fre.setSegmentStyle(QLCDNumber.Flat)
        self.Blink_fre.setStyleSheet("QLCDNumber { font-family: SimSun; font-size: 24px; }")
        self.frame_7 = QtWidgets.QFrame(self.widget)
        self.frame_7.setGeometry(QtCore.QRect(450, 50, 241, 51))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.PERCLOS = QtWidgets.QLCDNumber(self.frame_7)
        self.PERCLOS.setGeometry(QtCore.QRect(140, 10, 65, 31))
        self.PERCLOS.setMaximumSize(QtCore.QSize(100, 50))
        self.PERCLOS.setObjectName("PERCLOS")
        self.label_16 = QtWidgets.QLabel(self.frame_7)
        self.label_16.setGeometry(QtCore.QRect(30, 0, 81, 50))
        self.label_16.setMinimumSize(QtCore.QSize(0, 40))
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_16.setStyleSheet("font: 11pt \"Adobe 黑体 Std R\";")
        self.label_16.setObjectName("label_16")
        self.frame_13 = QtWidgets.QFrame(self.widget)
        self.frame_13.setGeometry(QtCore.QRect(230, 0, 221, 101))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.frame_14 = QtWidgets.QFrame(self.frame_13)
        self.frame_14.setGeometry(QtCore.QRect(0, 0, 221, 51))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.label_25 = QtWidgets.QLabel(self.frame_14)
        self.label_25.setGeometry(QtCore.QRect(0, 0, 71, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_38 = QtWidgets.QLabel(self.frame_14)
        self.label_38.setGeometry(QtCore.QRect(150, 10, 61, 30))
        self.label_38.setObjectName("label_38")

        self.Yawn_num = QtWidgets.QLCDNumber(self.frame_14)
        self.Yawn_num.setGeometry(QtCore.QRect(80, 10, 61, 31))
        self.Yawn_num.setMaximumSize(QtCore.QSize(100, 50))
        self.Yawn_num.setObjectName("Yawn_num")
        self.Yawn_num.setSegmentStyle(QLCDNumber.Flat)
        self.Yawn_num.setStyleSheet("QLCDNumber { font-family: SimSun; font-size: 24px; }")
        self.frame_15 = QtWidgets.QFrame(self.frame_13)
        self.frame_15.setGeometry(QtCore.QRect(0, 50, 221, 51))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.label_26 = QtWidgets.QLabel(self.frame_15)
        self.label_26.setGeometry(QtCore.QRect(0, 0, 71, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_39 = QtWidgets.QLabel(self.frame_15)
        self.label_39.setGeometry(QtCore.QRect(150, 10, 61, 30))
        self.label_39.setObjectName("label_39")

        self.Yawn_fre = QtWidgets.QLCDNumber(self.frame_15)
        self.Yawn_fre.setGeometry(QtCore.QRect(80, 10, 61, 31))
        self.Yawn_fre.setMaximumSize(QtCore.QSize(100, 50))
        self.Yawn_fre.setObjectName("Yawn_fre")
        self.Yawn_fre.setSegmentStyle(QLCDNumber.Flat)
        self.Yawn_fre.setStyleSheet("QLCDNumber { font-family: SimSun; font-size: 24px; }")
        self.frame_18 = QtWidgets.QFrame(self.centralwidget)
        self.frame_18.setGeometry(QtCore.QRect(880, 80, 271, 91))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.label_30 = QtWidgets.QLabel(self.frame_18)
        self.label_30.setGeometry(QtCore.QRect(80, 0, 121, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.Danger_state1 = QtWidgets.QLabel(self.frame_18)
        self.Danger_state1.setGeometry(QtCore.QRect(16, 40, 251, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Danger_state1.setFont(font)
        self.Danger_state1.setObjectName("Danger_state1")

        self.frame_19 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_19.setGeometry(QtCore.QRect(0, 260, 221, 51))
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.label_31 = QtWidgets.QLabel(self.frame_19)
        self.label_31.setGeometry(QtCore.QRect(16, 0, 81, 51))
        self.label_31.setStyleSheet("font: 11pt \"Adobe 黑体 Std R\";")
        self.label_31.setObjectName("label_31")
        self.Emotion = QtWidgets.QLabel(self.frame_19)
        self.Emotion.setGeometry(QtCore.QRect(120, 0, 61, 51))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Emotion.setFont(font)
        self.Emotion.setObjectName("Emotion")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1163, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        ##按钮样式设置
        self.btn_start.setStyleSheet(''' 
                             QPushButton
                             {text-align : center;
                             background-color : white;
                             font: bold;
                             border-color: gray;
                             border-width: 2px;
                             border-radius: 10px;
                             padding: 6px;
                             height : 14px;
                             border-style: outset;
                             font : 14px;}
                             QPushButton:pressed
                             {text-align : center;
                             background-color : light gray;
                             font: bold;
                             border-color: gray;
                             border-width: 2px;
                             border-radius: 10px;
                             padding: 6px;
                             height : 14px;
                             border-style: outset;
                             font : 14px;}
                             ''')

        self.btnexit.setStyleSheet(''' 
                     QPushButton
                     {text-align : center;
                     background-color : red;
                     font: bold;
                     color:white;
                     border-color: gray;
                     border-width: 2px;
                     border-radius: 10px;
                     padding: 6px;
                     height : 14px;
                     border-style: outset;
                     font : 14px;}
                     QPushButton:pressed
                     {text-align : center;
                     background-color : light gray;
                     font: bold;
                     border-color: gray;
                     border-width: 2px;
                     border-radius: 10px;
                     padding: 6px;
                     height : 14px;
                     border-style: outset;
                     font : 14px;}
                     ''')
        self.btntestcamera.setStyleSheet(''' 
                     QPushButton
                     {text-align : center;
                     background-color : yellow;
                     font: bold;
                     border-color: gray;
                     border-width: 2px;
                     border-radius: 10px;
                     padding: 6px;
                     height : 14px;
                     border-style: outset;
                     font : 14px;}
                     QPushButton:pressed
                     {text-align : center;
                     background-color : light gray;
                     font: bold;
                     border-color: gray;
                     border-width: 2px;
                     border-radius: 10px;
                     padding: 6px;
                     height : 14px;
                     border-style: outset;
                     font : 14px;}
                     ''')
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "安驰万里·危险驾驶行为分析系统V1.0"))
        self.label_9.setText(_translate("MainWindow", "安驰万里·驾驶"))
        self.groupBox_3.setTitle(_translate("MainWindow", "系统信息"))
        self.label_10.setText(_translate("MainWindow", "当前时间："))
        self.label_13.setText(_translate("MainWindow", "FPS"))
        self.label_12.setText(_translate("MainWindow", "当前帧频："))
        self.label_14.setText(_translate("MainWindow", ":"))
        self.label_15.setText(_translate("MainWindow", ":"))
        self.groupBox_5.setTitle(_translate("MainWindow", "实时预测"))

        self.label_22.setText(_translate("MainWindow", "%"))
        self.label_23.setText(_translate("MainWindow", "高兴"))
        self.label_27.setText(_translate("MainWindow", "自然"))
        self.label_19.setText(_translate("MainWindow", "%"))

        self.groupBox_4.setTitle(_translate("MainWindow", "菜单"))
        self.btntestcamera.setText(_translate("MainWindow", "测试相机"))
        self.btn_start.setText(_translate("MainWindow", "开始运行"))
        self.btnexit.setText(_translate("MainWindow", "退出程序"))
        self.groupBox.setTitle(_translate("MainWindow", "状态记录"))

        self.label_32.setText(_translate("MainWindow", "%"))
        self.label_34.setText(_translate("MainWindow", "惊讶"))
        self.label_28.setText(_translate("MainWindow", "生气"))
        self.label_29.setText(_translate("MainWindow", "%"))
        self.label_36.setText(_translate("MainWindow", "次数"))
        self.label_37.setText(_translate("MainWindow", "次数/分"))
        self.label_38.setText(_translate("MainWindow", "次数"))
        self.label_39.setText(_translate("MainWindow", "次数/分"))

        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#0000ff;\">安驰·驾驶</span></p></body></html>"))
        self.label_30.setText(_translate("MainWindow", "危险行为预测"))
        self.groupBox_2.setTitle(_translate("MainWindow", "情绪预测"))
        self.label_21.setText(_translate("MainWindow", "当前状态"))
        self.State.setText(_translate("MainWindow", "清醒"))
        self.label_31.setText(_translate("MainWindow", "当前情绪"))
        self.Emotion.setText(_translate("MainWindow", "自然"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">眨眼次数</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">眨眼频率</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "PERCLOS"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">哈欠次数</span></p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">哈欠频率</span></p></body></html>"))

    # 消息框显示函数
    def printf(self, mes, n=1):
        if n == 1:
            formatted_time = time.strftime("%H:%M:%S ", time.localtime(time.time()))
            self.State_record.append(formatted_time+mes)  # 在指定的区域显示提示信息
        else:
            self.Msg.setText(mes)
