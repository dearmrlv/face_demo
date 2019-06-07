from Signin import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog,QMessageBox
from PyQt5.QtCore import QTimer, QCoreApplication
from PyQt5.QtGui import QPixmap
import cv2
import os
import csv
import qimage2ndarray
import time
import datetime
from facetool.frame import Frame
from facetool.imtools import get_group

def makeasocket(path):  # 创建文件夹
    if not os.path.exists(path):
        os.makedirs(path)


def check_name(objname, namelist):  # 检查签到是否有重复的
    for namecouple in namelist:
        if objname == namecouple[0]:
            return 0
    return 1


class CamShow(QMainWindow, Ui_MainWindow):
    def __del__(self):
        try:
            self.camera.release()  # 释放资源
        except:
            return
    def __init__(self, parent = None):
        super(CamShow, self).__init__(parent)
        self.setupUi(self)

        self.PrepWidgets()
        self.PrepParameters()
        self.CallBackFunctions()
        self.Timer = QTimer()
        self.Timer.timeout.connect(self.TimerOutFun)
        self.namelist = []
        self.date = ''
        self.curtime = ''
        self.outputpath = 'presentdata/'
        makeasocket(self.outputpath)  # 创建文件夹

    def PrepWidgets(self):  # 初始，“暂停”、“输出名单”、“清空当前名单”和“开始识别”为灰
        self.PrepCamera()
        self.StopBt.setEnabled(False)
        self.DiscernBt.setEnabled(False)
        self.csvout.setEnabled(False)
        self.clearlist.setEnabled(False)

    def PrepCamera(self):
        try:
            self.camera = cv2.VideoCapture(0)
            self.MsgTE.clear()  # 清空下方信息显示一栏
            self.MsgTE.append('Oboard camera connected.')
            self.MsgTE.setPlainText()
        except Exception as e:
            self.MsgTE.clear()
            self.MsgTE.append(str(e))

    def PrepParameters(self):

        self.Image_num = 0  # 计数器置零
        self.MsgTE.clear()

    def CallBackFunctions(self):

        self.ShowBt.clicked.connect(self.StartCamera)   # 点击“打开摄像头”，则链接StartCamera函数
        self.StopBt.clicked.connect(self.StopCamera)    # 点击“暂停”，则链接StopCamera函数
        self.DiscernBt.clicked.connect(self.DiscernCamera)  # 点击“开始识别”，则链接DiscernCamera函数
        self.ExitBt.clicked.connect(self.ExitApp)   # 点击“退出”，则链接ExitApp函数
        self.csvout.clicked.connect(self.save_to_csv)  # 点击“输出名单”，则将已签到成功的人输出到一个csv文件
        self.clearlist.clicked.connect(self.clearnamelist)  # 点击“清空当前名单”，则将当前的namelist清空

    def StartCamera(self):  # “打开摄像头”
        self.ShowBt.setEnabled(False)   # 相应“打开摄像头”变灰
        self.StopBt.setEnabled(True)    # 相应“暂停”由灰变亮
        self.DiscernBt.setEnabled(True)    # 相应“开始识别”由灰变亮
        self.csvout.setEnabled(True)  # 相应“输出名单”由灰变亮
        self.clearlist.setEnabled(True)

        self.Timer.start(1)
        # self.timelb = time.clock()
        self.timelb = time.process_time()

        now_time = datetime.datetime.now()
        time_str = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
        self.date = time_str[0:10]
        self.curtime = time_str[-8:]

    def TimerOutFun(self):
        success, img = self.camera.read()   # 从摄像头读取图像

        # newly edited
        checked_frame = Frame(img)                # create a Frame class
        checked_frame.name_checked()
        img = checked_frame.frame  # returns the frame detected
        self.PossibleNames = checked_frame.names

        if success:
            self.Image = img
            self.DispImg()
            self.Image_num += 1

        else:
            self.MsgTE.clear()
            self.MsgTE.setPlainText('Image obtaining failed.')

    def DispImg(self):  # 显示图像

        img = cv2.cvtColor(self.Image, cv2.COLOR_BGR2RGB)
        qimg = qimage2ndarray.array2qimage(img)
        self.DispLb.setPixmap(QPixmap(qimg))
        self.DispLb.show()

    def StopCamera(self):   # “暂停”
        if self.StopBt.text() == '暂停':
            self.StopBt.setText('继续')
            self.Timer.stop()
        elif self.StopBt.text() == '继续':
            self.StopBt.setText('暂停')
            self.Timer.start(1)

    def DiscernCamera(self):  # 识别部分
                            # 此处与其余部分连接

        # newly edited
        # self.PossibleNames is an array contains all possible names
        # the Counting function is not used here, and you can refer to facetool/demo.py
        if len(self.PossibleNames) != 0:
            self.Name = self.PossibleNames[0]
            self.Hint = self.Name + '\t签到成功'
            self.MsgTE.setText('\t\t\t\t' + self.Hint)
            now_time = datetime.datetime.now()
            time_str = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
            curtime = time_str[-9:]
            namecouple = [self.Name, curtime]
            if check_name(self.Name, self.namelist):
                self.namelist.append(namecouple)
                self.Hint = self.Name + '\t签到成功'
            else:
                self.Hint = '请勿重复签到'
                self.MsgTE.setText('\t\t\t\t' + self.Hint)
        else:
            self.MsgTE.setText('\t\t\t\t签到失败')

    def save_to_csv(self):  # 将签到名单输出到csv文件中

        with open(self.outputpath + '签到名单.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(['日期', self.date, '', '开始签到时间', self.curtime])
            writer.writerow(
                ['姓名', '签到时间'])
            for name in self.namelist:
                writer.writerow([name[0], name[1]])  # 分别输出名字和时间
        QMessageBox.information(self, "保存提示", "保存成功！", QMessageBox.Yes, QMessageBox.Yes)

    def clearnamelist(self):  # 清空当前的namelist
        self.namelist = []

    def ExitApp(self):  # “退出”

        self.camera.release()
        self.MsgTE.setPlainText('Exiting the application...')
        QCoreApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = CamShow()
    ui.show()
    sys.exit(app.exec_())
