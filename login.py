import os
import subprocess
import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel
from QCandyUi import CandyWindow
import register


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.ut = 0
        self.setupUi(self)

        label = QLabel(self)
        label.setGeometry(20, 180, 400, 400)
        label.setAlignment(Qt.AlignCenter)
        # 加载图片并设置为 QLabel 的背景
        image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img.png")
        pixmap = QPixmap(image_path).scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label.setPixmap(pixmap)

    # 界面设计
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(887, 651)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setStyleSheet('''
            color:red;
            font-size:36px;
        ''')
        self.label1.setGeometry(QtCore.QRect(200, 0, 600, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(590, 160, 211, 41))
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit1.setPlaceholderText("请输入用户名")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(470, 160, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(590, 230, 211, 41))
        self.lineEdit2.setPlaceholderText("请输入密码")
        from PyQt5.Qt import QLineEdit
        self.lineEdit2.setEchoMode(QLineEdit.Password)
        self.lineEdit2.setObjectName("lineEdit2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(470, 230, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")

        self.radioButton1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton1.setGeometry(QtCore.QRect(530, 400, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton1.setFont(font)
        self.radioButton1.setObjectName("radioButton1")
        self.radioButton1.setChecked(True)

        self.radioButton2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton2.setGeometry(QtCore.QRect(680, 400, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton2.setFont(font)
        self.radioButton2.setObjectName("radioButton2")
        self.radioButton2.setChecked(False)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 490, 111, 41))
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
        self.menuview = QtWidgets.QMenu(self.menubar)
        self.menuview.setObjectName("menuview")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.menuview.addAction(self.action1)
        self.menuview.addAction(self.action2)
        self.menubar.addAction(self.menuview.menuAction())

        # 事件绑定
        self.pushButton.clicked.connect(self.login)
        self.radioButton1.toggled.connect(self.usertype)
        self.radioButton2.toggled.connect(self.usertype)
        self.action1.triggered.connect(self.regist_user)
        self.action2.triggered.connect(self.quit_sys)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基于深度学习的中药饮片识别系统"))
        self.label1.setText(_translate("MainWindow", "欢迎使用中药饮片识别系统"))
        self.label2.setText(_translate("MainWindow", "学号:"))
        self.label3.setText(_translate("MainWindow", "密 码:"))
        self.radioButton1.setText(_translate("MainWindow", "管理员"))
        self.radioButton2.setText(_translate("MainWindow", "用户"))
        self.pushButton.setText(_translate("MainWindow", "登  录"))
        self.menuview.setTitle(_translate("MainWindow", "菜单栏"))
        self.action1.setText(_translate("MainWindow", "注册"))
        self.action2.setText(_translate("MainWindow", "退出系统"))

        # 登录操作

    def login(self):
        from PyQt5.Qt import QMessageBox
        user = self.lineEdit1.text()
        pwd = self.lineEdit2.text()
        self.usertype()
        if user == "" or pwd == "":
            QMessageBox.warning(self, "警告", "用户名和密码不可为空!", QMessageBox.Yes, QMessageBox.Yes)
            return False
        # 管理员用户
        if self.ut == 1:
            if user == "user" and pwd == "123456":
                QMessageBox.information(self, '提示', "管理员登录成功！", QMessageBox.Yes)
                self.hide()
                # 转入主界面
                subprocess.run(["python", "root.py"])
                sys.exit()
            else:
                QMessageBox.warning(self, '提示', "您输入的账号或密码有误！", QMessageBox.Yes)
                self.lineEdit1.clear()
                self.lineEdit2.clear()
                return

        # 普通用户
        else:
            file_path = 'users.txt'  # 文件路径

            with open(file_path, 'r') as file:
                user_data = file.readlines()

            for line in user_data:
                line = line.strip().split(',')
                if user == line[0] and pwd == line[1]:
                    QMessageBox.information(self, '提示', "用户登录成功！", QMessageBox.Yes)
                    self.hide()
                    # 转入主界面
                    subprocess.run(["python", "clas.py"])
                    return

            QMessageBox.warning(self, '提示', "您输入的账号或密码有误！", QMessageBox.Yes)
            self.lineEdit1.clear()
            self.lineEdit2.clear()
            return

    # 用户类型选择（单选）
    def usertype(self):
        info = 0
        if self.radioButton1.isChecked():
            self.radioButton1.setChecked(True)
            info = 1
        else:
            self.radioButton1.setChecked(False)
            info = 0
        if self.radioButton2.isChecked():
            self.radioButton2.setChecked(True)
            info = 0
        else:
            self.radioButton2.setChecked(False)
            info = 1
        self.ut = info

    # 用户注册
    def regist_user(self):
        # 主界面的隐藏
        self.hide()
        # 注册界面打开
        self.regist = register.Ui_MainWindow()
        self.regist.show()

    # 刷新(清空输入框)
    def flush(self):
        self.lineEdit1.clear()
        self.lineEdit2.clear()
        # 默认选择
        if self.ut == 0:
            self.radioButton1.setChecked(True)

    # 退出系统（关闭界面）
    def quit_sys(self):
        self.close()
        sys.exit()


# 入口
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 创建一个应用程序
    ui1 = Ui_MainWindow()  # 创建设计好的窗口对象
    ui1 = CandyWindow.createWindow(ui1, 'blueGreen')
    ui1.show()
    sys.exit(app.exec_())
