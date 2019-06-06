from Signin import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QTimer, QCoreApplication
from PyQt5.QtGui import QPixmap
import cv2
import qimage2ndarray
import time
from facetool.frame import Frame
from facetool.imtools import get_group

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

    def PrepWidgets(self):  # 初始，“暂停”和“开始识别”为灰
        self.PrepCamera()
        self.StopBt.setEnabled(False)
        self.DiscernBt.setEnabled(False)

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

    def StartCamera(self):  # “打开摄像头”
        self.ShowBt.setEnabled(False)   # 相应“打开摄像头”变灰
        self.StopBt.setEnabled(True)    # 相应“暂停”由灰变亮
        self.DiscernBt.setEnabled(True)    # 相应“开始识别”由灰变亮

        self.Timer.start(1)
        # self.timelb = time.clock()
        self.timelb = time.process_time()

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
        else:
            self.MsgTE.setText('\t\t\t\t签到失败')

    def ExitApp(self):  # “退出”

        self.camera.release()
        self.MsgTE.setPlainText('Exiting the application..')
        QCoreApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = CamShow()
    ui.show()
    sys.exit(app.exec_())