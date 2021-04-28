import random
import sys
from time import sleep

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, QDateTime, QThread
from PyQt5.QtGui import QPalette, QFont

import DisplayUI
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLabel
from VideoDisplay import Display

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWnd = QMainWindow()
    ui = DisplayUI.Ui_MainWindow()
    # 可以理解成将创建的 ui 绑定到新建的 mainWnd 上
    ui.setupUi(mainWnd)
    display = Display(ui, mainWnd)

    # -------------------
    mainWnd.show()
    sys.exit(app.exec_())
