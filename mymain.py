import sys
import os
from PyQt5.QtWidgets import (QWidget, QGridLayout, QApplication,QLabel,QHBoxLayout,QMessageBox)
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtCore import Qt,pyqtSignal
import random

def getSource():
    filelist = os.listdir("source/face")
    return filelist
fileList = getSource()
len = len(fileList)

messList=["我没有笑","俺真的没笑","找出可爱的笑脸哦","我看到一个笑脸","你看，他在笑","要笑哦","找笑笑","改变笑容"]
err =0
class MyLabel(QLabel):
    sendMsg = pyqtSignal()
    def __init__(self):
        super().__init__()
    def mousePressEvent(self, e):
        global err
        objectname = self.objectName()
        index = objectname.find('x')
        if index!=-1:
            err = 0
            self.sendMsg.emit()
        else:
            if err==3:
                self.sendMsg.emit()
                err =0
                return
            err +=1
            num1 = random.sample(range(0, 7), 1)
            str = messList[num1[0]]
            print(str)
            msgBox = QMessageBox(QMessageBox.NoIcon,"友情提示", str)
            msgBox.setIconPixmap(QPixmap("source/ico.jpg").scaled(50,50))
            msgBox.exec()






class basicWindow(QWidget):
    filename=''
    def __init__(self,height,width):
        super().__init__()
        self.height = height/5
        self.width = width/10
        self.grid_layout = QGridLayout()
        self.InitUI()

    def InitUI(self):
        self.setLayout(self.grid_layout)
        self.setQImage()

    def setQImage(self):
        num=random.sample(range(0, len-1), 32)
        i =0
        for x in range(4):
            for y in range(8):
                label = MyLabel()
                label.sendMsg.connect(self.changeImage)
                pixmap = QPixmap("./source/face/"+fileList[num[i]]).scaled(self.height-3, self.width-3)
                label.setPixmap(pixmap)
                label.setObjectName(str(fileList[num[i]]))
                label.setMouseTracking(True)
                self.grid_layout.addWidget(label, x, y)
                i+=1
    def changeImage(self):
        print(self.filename)
        self.setQImage()



class Mymain(QWidget):
    def __init__(self):
        super().__init__()
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()
        self.initUI()
    def initUI(self):
        self.showMaximized()
        self.move(10, 0)
        self.resize(self.width-10, self.height)
        self.setWindowTitle("笑口常开好运来!笑一个，哈哈哈--找出笑脸哦")
        self.setWindowIcon(QIcon("source/ico.jpg"))
        self.layout = QHBoxLayout()
        windowExample = basicWindow(self.height,self.width)
        # windowExample.resize(self.width-100,self.width-100)
        self.layout.addWidget(windowExample)
        self.setLayout(self.layout)


app = QApplication(sys.argv)
Mymain = Mymain()
Mymain.setWindowFlags(Qt.WindowMinimizeButtonHint)
Mymain.setWindowFlags(Qt.WindowCloseButtonHint)
# Mymain.setFixedSize(Mymain.width(), Mymain.height())


Mymain.show()
sys.exit(app.exec_())