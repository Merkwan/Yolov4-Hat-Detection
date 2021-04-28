import sys
import time
import cv2
import ctypes
import inspect
import threading
import random
import os
import numpy as np
from PyQt5.QtCore import QFile, QTimer, QDateTime, QThread
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDialog, QLabel, QGraphicsPixmapItem, QGraphicsScene
from PyQt5.QtGui import QImage, QPixmap, QPalette, QFont
from PyQt5 import QtGui, QtCore, QtWidgets
from time import sleep
import datetime


class Display:

    def __init__(self, ui, mainWnd):
        self.ui = ui
        self.mainWnd = mainWnd
        img1 = cv2.imread("title2.jpg")  # 读取图像
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)  # 转换图像通道
        x = img1.shape[1]  # 获取图像大小
        y = img1.shape[0]
        self.zoomscale = 1  # 图片放缩尺度
        img2 = QImage(img1, x, y, QImage.Format_RGB888)
        self.ui.title.setPixmap(QPixmap.fromImage(img2))
        # 定时器，实时更新数据
        #self.timer = QTimer()
        #self.timer.timeout.connect(self.showdata)
       # self.timer.start(100)
        ui.Open.clicked.connect(self.Open)#打开视频的信号槽
        ui.openPic.clicked.connect(self.openPic)  # 打开图片的信号槽
        ui.openVt.clicked.connect(self.openVt)  # 打开视频检测的信号槽
        ui.openPt.clicked.connect(self.openPt)  # 打开图片检测的信号槽
        ui.openCv.clicked.connect(self.openCv)  # 打开摄像头的信号槽
       # ui.Close.clicked.connect(self.Close)
        self.stopEvent = threading.Event()
        self.stopEvent.clear()

    # 打开视频检测
    def openVt(self):
        self.fileName, self.fileType = QFileDialog.getOpenFileName(self.mainWnd, 'Choose file', '', '*.mp4')
        # print(self.fileName)#self.fileName就是路径加文件名
        if(self.fileName):
            with open('video_detect.bat','w') as writer:
                writer.write("F:\n")
                writer.write("cd F:\\ComputerParctice\\yolov4\\darknet-master\\build\darknet\\x64\n")
                writer.write("darknet.exe detector demo  data\\voc_hat.data  cfg\\yolov4-test.cfg backup\\yolov4-custom_final-old-520.weights "+self.fileName+" -thresh 0.2 -ext_output -out_filename  F:\\ComputerParctice\\yolov4\\ui\\resultVideo.mp4\n")
                writer.write("exit")
                writer.close()
             # print(ord(self.fileName))
            # print("nihao")
            def stop_Thread(self, tid, exctype):
                tid = ctypes.c_long(tid)
                if not inspect.isclass(exctype):
                    exctype = type(exctype)
                res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
                if res == 0:
                    raise ValueError("invaid thread id")
                elif res != 1:
                    ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
                    raise SystemError("PyThreadState_SetAsyncExc failed")
            # self.fileName, self.fileType = QFileDialog.getOpenFileName(self.mainWnd, 'Choose file', '', '*.mp4')
            # print(self.fileName)  # self.fileName就是路径加文件名
            # print(int(self.fileType))
            th=threading.Thread(target=self.handle_openVt)
            th.start()
            while(1):
                if((cv2.waitKey(1) & 0xFF )== 27):
                    stop_Thread(th.ident,SystemExit)
                    break

    def handle_openVt(self):
        os.system('video_detect.bat')


    #打开图片检测
    def openPt(self):
        self.fileName,self.fileType= QFileDialog.getOpenFileName(self.mainWnd, 'Choose file', '', 'Image files(*.jpg)')
        if (self.fileName):
            with open('img_detect.bat', 'w') as writer:
                writer.write("F:\n")
                writer.write("cd F:\\ComputerParctice\\yolov4\\darknet-master\\build\darknet\\x64\n")
                writer.write("darknet.exe detector test  data\\voc_hat.data  cfg\\yolov4-test.cfg backup\\yolov4-custom_final-old-520.weights "+self.fileName+"\n")
                writer.write("copy F:\ComputerParctice\yolov4\darknet-master\\build\darknet\\x64\predictions.jpg F:\ComputerParctice\yolov4\\ui\n")
                #writer.write("Y\n")
                writer.write("exit")
                writer.close()

            def stop_Thread(self, tid, exctype):
                tid = ctypes.c_long(tid)
                if not inspect.isclass(exctype):
                    exctype = type(exctype)
                res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
                if res == 0:
                    raise ValueError("invaid thread id")
                elif res != 1:
                    ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
                    raise SystemError("PyThreadState_SetAsyncExc failed")
                # self.fileName, self.fileType = QFileDialog.getOpenFileName(self.mainWnd, 'Choose file', '', '*.mp4')
                # print(self.fileName)  # self.fileName就是路径加文件名
                # print(int(self.fileType))

            th = threading.Thread(target=self.handle_openPt)
            th.start()
            while (1):
                if ((cv2.waitKey(1) & 0xFF) == 27):
                    stop_Thread(th.ident, SystemExit)
                    break

            # print(int(self.fileType))
            # th=threading.Thread(target=self.handle_Detect,args=(self,))
            # th.start()

    def handle_openPt(self):
        os.system('img_detect.bat')


    # def stop_Thread(self,tid,exctype):
    #     tid=ctypes.c_long(tid)
    #     if not inspect.isclass(exctype):
    #         exctype=type(exctype)
    #     res=ctypes.pythonapi.PyThreadState_SetAsyncExc(tid,ctypes.py_object(exctype))
    #     if res==0:
    #         raise ValueError("invaid thread id")
    #     elif res!=1:
    #         ctypes.pythonapi.PyThreadState_SetAsyncExc(tid,None)
    #         raise SystemError("PyThreadState_SetAsyncExc failed")

    # 打开摄像头检测的函数
    def openCv(self):
        def stop_Thread(self, tid, exctype):
            tid = ctypes.c_long(tid)
            if not inspect.isclass(exctype):
                exctype = type(exctype)
            res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
            if res == 0:
                raise ValueError("invaid thread id")
            elif res != 1:
                ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
                raise SystemError("PyThreadState_SetAsyncExc failed")
        # self.fileName, self.fileType = QFileDialog.getOpenFileName(self.mainWnd, 'Choose file', '', '*.mp4')
        # print(self.fileName)  # self.fileName就是路径加文件名
        # print(int(self.fileType))
        th=threading.Thread(target=self.handle_Detect)
        th.start()
        while(1):
            if((cv2.waitKey(1) & 0xFF )== 27):
                stop_Thread(th.ident,SystemExit)
                break
    #线程处理函数
    def handle_Detect(self):
        with open('cap_detect.bat', 'w') as writer:
            writer.write("F:\n")
            writer.write("cd F:\\ComputerParctice\\yolov4\\darknet-master\\build\darknet\\x64\n")
            writer.write("darknet.exe detector demo  data\\voc_hat.data  cfg\\yolov4-test.cfg backup\\yolov4-custom_final-old-520.weights  -thresh 0.2 -ext_output -out_filename  F:\\ComputerParctice\\yolov4\\ui\\resultCap.mp4>F:\\ComputerParctice\\yolov4\\ui\\output.txt\n")
            writer.write("exit")
            writer.close()
        os.system("cap_detect.bat")
        # print(self.filename)



#打开视频
    def Open(self):

        self.fileName, self.fileType = QFileDialog.getOpenFileName(self.mainWnd, 'Choose file', '', '*.mp4')
        if (self.fileName):
            self.cap = cv2.VideoCapture(self.fileName)
            self.frameRate = self.cap.get(cv2.CAP_PROP_FPS)
            def fps():
                cap = cv2.VideoCapture(self.fileName)  # file path
                start_time = time.time()
                counter = 0
                fps = cap.get(cv2.CAP_PROP_FPS)
                while cap.isOpened():
                    ret, frame = cap.read()

                    key = cv2.waitKey(1) & 0xff

                    if key == ord(" "):
                        cv2.waitKey(0)

                    if key == 27:
                        break
                    counter += 1
                    if (time.time() - start_time) != 0:
                        cv2.putText(frame, "FPS {0}".format(float('%.1f' % (counter / (time.time() - start_time)))), (500, 50),
                                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),
                                    3)
                        cv2.imshow('frame', frame)
                        print("FPS: ", counter / (time.time() - start_time))
                        counter = 0
                        start_time = time.time()
                    time.sleep(1 / fps)
                cap.release()
                cv2.destroyAllWindows()
        # 创建视频显示线程
            fps()
            th = threading.Thread(target=self.Display)
            th.start()
                # 显示标题
        #def Close(self):
                # 关闭事件设为触发，关闭视频播放
            #self.stopEvent.set()

    #打开图片
    def openPic(self):
        print("load--file")
        # QFileDialog就是系统对话框的那个类第一个参数是上下文，第二个参数是弹框的名字，第三个参数是开始打开的路径，第四个参数是需要的格式
        fname, _ = QFileDialog.getOpenFileName(self.mainWnd, 'Choose file', '','Image files(*.jpg *.gif *.png)')
        if(fname):
            img = cv2.imread(fname)
            #cv2.resizeWindow('photo_show',1000,1000) #固定图像大小
            cv2.moveWindow('photo_show', 0, 200)#改变位置，但是不能实现
            cv2.imshow('photo_show', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.destroyWindow('photo_show')
            #self.ui.DisplayLabel.setPixmap(QPixmap(fname))
            #print(fname)
            #self.frameRate = self.cap.get(cv2.CAP_PROP_FPS)

            # 创建图片显示线程





    def Display(self):
       # self.ui.Open.setEnabled(False)
        #self.ui.Close.setEnabled(True)

        #self.cap = cv2.VideoCapture("final.mp4")
       # self.frameRate = self.cap.get(cv2.CAP_PROP_FPS)
        #success, frame = self.cap.read()
        while self.cap.isOpened():
            success, frame = self.cap.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
           # self.ui.DisplayLabel.setPixmap(QPixmap.fromImage(img))

            cv2.waitKey(int(1000 / self.frameRate))
            # 判断关闭事件是否已触发
