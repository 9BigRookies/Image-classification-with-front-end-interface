# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from IPython.external.qt_for_kernel import QtCore
from PyQt5.QtCore import pyqtSlot, QPoint, QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog, QMessageBox
from QCandyUi import CandyWindow
from Ui_root import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot(QPoint)
    def on_label_customContextMenuRequested(self, pos):
        """
        Slot documentation goes here.
        
        @param pos DESCRIPTION
        @type QPoint
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        with open('users.txt', 'r') as f:  # 替换为您的文本文件路径
            content = f.read()
        font = self.label.font()  # 获取当前字体
        font.setPointSize(16)  # 设置字体大小为16
        self.label.setFont(font)  # 应用新的字体
        self.label.setAlignment(QtCore.Qt.AlignCenter)  # 将文本水平居中对齐
        # 将文本内容显示在标签上
        self.label.setText(content)  # label是您要显示文本的标签对象名
    
    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        with open('model_data/cls_classes.txt', 'r') as f:  # 替换为您的文本文件路径
            content = f.read()
        content_with_spaces = ' '.join(content.split())
        font = self.label.font()  # 获取当前字体
        font.setPointSize(10)  # 设置字体大小为10
        self.label.setFont(font)  # 应用新的字体
        self.label.setAlignment(QtCore.Qt.AlignCenter)  # 将文本水平居中对齐
        self.label.setWordWrap(True)  # 自动换行
        # 将文本内容显示在标签上
        self.label.setText(content_with_spaces)  # label是您要显示文本的标签对象名
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        with open('users.txt', 'r') as f:  # 替换为您的文本文件路径
            lines = f.readlines()
        options = []
        for line in lines:
            username = line.split(',')[0].strip()  # 使用逗号分割行并提取第一个元素作为用户名
            options.append(username)

        selected_option, ok = QInputDialog.getItem(self, "删除用户", "选择一个待删用户:", options, editable=False)

        if ok and selected_option:
            with open('users.txt', 'w') as f:
                for line in lines:
                    if selected_option not in line:
                        f.write(line)
            QMessageBox.information(self, "用户删除", "此用户已完成删除.")
    
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        url = QUrl("http://www.zhongyoo.com/")
        QDesktopServices.openUrl(url)
    
    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        sys.exit()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui = CandyWindow.createWindow(ui, 'blueGreen')
    ui.show()
    sys.exit(app.exec_())
