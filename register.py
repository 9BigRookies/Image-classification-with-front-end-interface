"""
项目名称：python图书管理系统
作者：bhml
时间：2023/1/28
代码功能：注册界面与功能实现
"""
import os
import subprocess

from PyQt5.Qt import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import sys
from QCandyUi import CandyWindow
import login


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)

    # 界面设计
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(887, 651)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 10, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 120, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(430, 120, 211, 51))

        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(430, 210, 211, 51))
        self.lineEdit_2.setPlaceholderText("请输入密码")
        from PyQt5.Qt import QLineEdit
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 210, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(430, 300, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setPlaceholderText("请再次输入密码")
        self.lineEdit_3.setEchoMode(QLineEdit.Password)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 300, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 410, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 887, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.actiont3 = QtWidgets.QAction(MainWindow)
        self.actiont3.setObjectName("actiont3")
        self.actiont4 = QtWidgets.QAction(MainWindow)
        self.actiont4.setObjectName("actiont4")
        self.menu.addAction(self.action1)
        self.menu.addAction(self.action2)
        self.menubar.addAction(self.menu.menuAction())

        # 事件绑定
        self.pushButton.clicked.connect(self.register_user)
        self.action1.triggered.connect(self.login)
        self.action2.triggered.connect(self.quit_sys)
        self.actiont3.triggered.connect(self.login)
        self.actiont4.triggered.connect(self.quit_sys)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "中药饮片识别系统"))
        self.label.setText(_translate("MainWindow", "  注册"))
        self.label_2.setText(_translate("MainWindow", "学号："))
        self.label_3.setText(_translate("MainWindow", "密 码："))
        self.label_4.setText(_translate("MainWindow", "确认密码："))
        self.pushButton.setText(_translate("MainWindow", "注 册"))
        self.menu.setTitle(_translate("MainWindow", "菜单栏"))
        self.action1.setText(_translate("MainWindow", "登陆"))
        self.action2.setText(_translate("MainWindow", "退出系统"))
#  注册
    def register_user(self):
        user = self.lineEdit.text()
        pwd = self.lineEdit_2.text()
        pwd1 = self.lineEdit_3.text()

        if user == "" or pwd == "" or pwd1 == "":
            QMessageBox.warning(self, "警告", "用户名和密码不可为空!", QMessageBox.Yes, QMessageBox.Yes)
            return

        if pwd != pwd1:
            QMessageBox.warning(self, '警告', "密码不一致！", QMessageBox.Yes)
            return

        try:
            file_path = os.path.join(os.path.dirname(__file__), 'users.txt')

            # Check if the user already exists in the file
            with open(file_path, 'r') as file:
                existing_users = [line.split(',')[0] for line in file.readlines()]
                if user in existing_users:
                    QMessageBox.warning(self, '警告', "该用户已存在", QMessageBox.Yes)
                    return

            # Append the new user to the file
            with open(file_path, 'a') as file:
                file.write(f"{user},{pwd}\n")

            QMessageBox.warning(self, '标题', '已成功注册,可继续注册', QMessageBox.Yes)
            self.hide()
            self.log = Ui_MainWindow()
            self.log.show()
            # sys.exit()  # 退出应用程序
        except Exception as e:
            QMessageBox.warning(self, '警告', f"发生异常: {str(e)}", QMessageBox.Yes)
            return

    # 刷新（去除数据）
    def flush(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()

    # 登录界面
    def login(self):
        self.hide()  # 主界面的隐藏
        # self.log = login.Ui_MainWindow()
        # self.log.show()
        subprocess.run(["python", "login.py"])

    # 退出系统
    def quit_sys(self):
        self.hide()
        sys.exit()


# 测试
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 创建一个应用程序
    ui1 = Ui_MainWindow()  # 创建设计好的窗口对象
    ui1 = CandyWindow.createWindow(ui1, 'blueGreen')
    ui1.show()
    sys.exit(app.exec_())
