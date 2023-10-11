# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import qdarkstyle
from PyQt5.QtCore import pyqtSlot, QPoint, QUrl, Qt
from PyQt5.QtGui import QImage, QPixmap, QPalette, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import QtCore
from Ui_clas import Ui_MainWindow
from PIL import Image
from QCandyUi import CandyWindow
from classification import Classification


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
        # # 设置主题颜色
        # palette = QPalette()
        # palette.setColor(QPalette.Window, QColor(48, 25, 52))  # 设置窗口背景颜色为紫黑色
        # palette.setColor(QPalette.Button, QColor(48, 25, 52))  # 设置按钮背景颜色为紫黑色
        # app.setPalette(palette)
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.file_names = None
        self.class_name = None
    
    @pyqtSlot(QPoint)
    def on_centralWidget_customContextMenuRequested(self, pos):
        """
        Slot documentation goes here.
        
        @param pos DESCRIPTION
        @type QPoint
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSlot(QUrl)
    def on_textBrowser_anchorClicked(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type QUrl
        """
        # TODO: not implemented yet
        raise NotImplementedError

    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.file_names, _ = QFileDialog.getOpenFileName(self, "选择文件", "",
                                                         "All Files (*);;Image Files (*.png *.jpg *.bmp)")
        if self.file_names:
            try:
                # 打开文件并显示图片
                result_image = QImage(self.file_names)
                img = result_image.scaled(self.label.width(), self.label.height(), Qt.KeepAspectRatio,
                                          Qt.SmoothTransformation)
                pixmap = QPixmap(img)
                self.label.setPixmap(pixmap)
            except Exception as e:
                print(f"Error: {e}")

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.class_name == 'Biejia':
            font = self.label_2.font()  # 获取当前字体
            font.setPointSize(16)  # 设置字体大小为10
            self.label_2.setFont(font)  # 应用新的字体
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)  # 将文本水平居中对齐
            N ='Biejia, also known as Turtle Shell, is a type of traditional Chinese medicinal material derived from ' \
               'the shells of turtles, particularly the shells of the Chinese softshell turtle (Pelodiscus sinensis). ' \
               'Biejia has a long history of use in Traditional Chinese Medicine (TCM) and is known for its ' \
               'nourishing and tonifying properties. In TCM, biejia is classified as a "supplementing" herb and is ' \
               'believed to nourish the yin, tonify the kidneys, and strengthen the yang energy. It is commonly used ' \
               'to treat conditions related to kidney deficiency, such as lower back and knee weakness, impotence, ' \
               'and premature ejaculation in men. Biejia is also used in the treatment of gynecological disorders, ' \
               'including irregular menstruation and abnormal vaginal discharge. ' \
               'In addition to its internal use, biejia is sometimes prepared as an external application, such as in ' \
               'ointments or poultices, to address skin conditions and promote wound healing. '
            self.label.setWordWrap(True)  # 设置label文本自动换行
            # 设置英文文字行间距为1.5倍
            style_sheet = "QLabel { line-height: 150%; }"
            self.label.setStyleSheet(style_sheet)
            self.label.setText(N)
        elif self.class_name == 'Baizhi':
            font = self.label_2.font()  # 获取当前字体
            font.setPointSize(16)  # 设置字体大小为10
            self.label_2.setFont(font)  # 应用新的字体
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)  # 将文本水平居中对齐
            N ='Bai Zhi, also known as Radix Angelicae Dahuricae, is a commonly used traditional Chinese medicinal ' \
               'herb. It is the dried root of the Angelica dahurica plant, which belongs to the Apiaceae family. Bai ' \
               'Zhi has been an essential herb in Chinese medicine for centuries due to its various therapeutic ' \
               'properties.Bai Zhi is renowned for its ability to dispel wind and relieve pain. It is often used to ' \
               'treat conditions related to wind-cold dampness, such as headaches, sinus congestion, ' \
               'and nasal congestion. Bai Zhi is also considered effective for treating toothaches, facial swelling, ' \
               'and skin disorders like boils and abscesses. In Traditional Chinese Medicine (TCM), Bai Zhi is ' \
               'believed to have acrid and warm properties, which help promote blood circulation and relieve ' \
               'stagnation. It is commonly used in herbal formulations and can be prepared as a decoction, powder, ' \
               'or external application, such as an ointment or poultice. As with any herbal remedy, it is important ' \
               'to seek guidance from a qualified healthcare professional or TCM practitioner before using Bai Zhi. ' \
               'They can provide appropriate dosage recommendations and consider potential herb-drug interactions or ' \
               'contraindications. '
            self.label.setWordWrap(True)  # 设置label文本自动换行
            # 设置英文文字行间距为1.5倍
            style_sheet = "QLabel { line-height: 150%; }"
            self.label.setStyleSheet(style_sheet)
            self.label.setText(N)
        elif self.class_name == 'Cangzhu':
            font = self.label_2.font()  # 获取当前字体
            font.setPointSize(16)  # 设置字体大小为10
            self.label_2.setFont(font)  # 应用新的字体
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)  # 将文本水平居中对齐
            N ='Cang Zhu, or Atractylodes rhizome, is a widely used herb in traditional Chinese medicine. It is known ' \
               'for its ability to strengthen the spleen, promote digestion, and eliminate dampness. Cang Zhu is ' \
               'often used to treat digestive disorders, such as poor appetite and bloating. It can be prepared as a ' \
               'decoction or powder, and it is advisable to consult a healthcare professional before use. '
            self.label.setWordWrap(True)  # 设置label文本自动换行
            # 设置英文文字行间距为1.5倍
            style_sheet = "QLabel { line-height: 150%; }"
            self.label.setStyleSheet(style_sheet)
            self.label.setText(N)
        elif self.class_name == 'Chenxiang':
            font = self.label_2.font()  # 获取当前字体
            font.setPointSize(16)  # 设置字体大小为10
            self.label_2.setFont(font)  # 应用新的字体
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)  # 将文本水平居中对齐
            N ='Chen Xiang is known for its warm and aromatic nature. It is believed to have calming and soothing ' \
               'effects on the mind and body. In traditional Chinese medicine, it is often used to treat conditions ' \
               'such as abdominal pain, bloating, and vomiting. It is also used to relieve pain, promote digestion, ' \
               'and invigorate the spleen and stomach. Furthermore, Chen Xiang is highly regarded for its use in ' \
               'incense and perfumes due to its distinct and pleasant fragrance. Its aromatic properties are also ' \
               'believed to have a calming and spiritual influence, making it popular for meditation and relaxation ' \
               'practices. It is advisable to consult with a qualified healthcare professional or traditional Chinese ' \
               'medicine practitioner before using Chen Xiang to ensure proper usage and dosage. '
            self.label.setWordWrap(True)  # 设置label文本自动换行
            # 设置英文文字行间距为1.5倍
            style_sheet = "QLabel { line-height: 150%; }"
            self.label.setStyleSheet(style_sheet)
            self.label.setText(N)
        elif self.class_name == 'Dafupi':
            font = self.label_2.font()  # 获取当前字体
            font.setPointSize(16)  # 设置字体大小为10
            self.label_2.setFont(font)  # 应用新的字体
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)  # 将文本水平居中对齐
            N ='In addition to its digestive benefits, Da Fu Pi is also used in the treatment of skin conditions. It ' \
               'is believed to have a drying effect and can be used externally for conditions such as excessive ' \
               'sweating and weeping eczema. Da Fu Pi can be prepared as a decoction, powder, or used externally as a ' \
               'topical application. However, it is important to consult with a qualified healthcare professional or ' \
               'traditional Chinese medicine practitioner for proper dosage and guidance. Please note that further ' \
               'research is needed to fully understand the pharmacological effects and potential interactions of Da ' \
               'Fu Pi with other medications. Therefore, it is advisable to seek professional advice before using Da ' \
               'Fu Pi or any other herbal remedies. '
            self.label.setWordWrap(True)  # 设置label文本自动换行
            # 设置英文文字行间距为1.5倍
            style_sheet = "QLabel { line-height: 150%; }"
            self.label.setStyleSheet(style_sheet)
            self.label.setText(N)
        elif self.class_name == 'Guizhi':
            font = self.label_2.font()  # 获取当前字体
            font.setPointSize(16)  # 设置字体大小为10
            self.label_2.setFont(font)  # 应用新的字体
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)  # 将文本水平居中对齐
            N ='Gui Zhi, also known as Cinnamomum twig, is a commonly used Chinese medicinal herb. It is the dried ' \
               'branch of the Cinnamomum cassia tree and has been used in traditional Chinese medicine for thousands ' \
               'of years. Gui Zhi is known for its warm and acrid properties. It is widely used to promote ' \
               'circulation, warm the body, and relieve pain. It is commonly used in the treatment of conditions such ' \
               'as the common cold, flu, and chronic pain disorders. Gui Zhi is believed to open the body meridians, ' \
               'improve blood flow, and alleviate muscle aches and stiffness. In addition to its circulation-boosting ' \
               'effects, Gui Zhi is also recognized for its ability to induce sweating. This property is particularly ' \
               'useful in treating early-stage colds or conditions associated with "wind-cold" patterns. Gui Zhi is ' \
               'often combined with other herbs to enhance its therapeutic effects. It is worth noting that Gui Zhi ' \
               'contains compounds that may interact with certain medications or have adverse effects in some ' \
               'individuals. Therefore, it is crucial to seek professional advice before using Gui Zhi or any other ' \
               'herbal remedies, especially if you have any underlying health conditions or are taking medications. '
            self.label.setWordWrap(True)  # 设置label文本自动换行
            # 设置英文文字行间距为1.5倍
            style_sheet = "QLabel { line-height: 150%; }"
            self.label.setStyleSheet(style_sheet)
            self.label.setText(N)
        else:
            font = self.label_2.font()  # 获取当前字体
            font.setPointSize(16)  # 设置字体大小为10
            self.label_2.setFont(font)  # 应用新的字体
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)  # 将文本水平居中对齐
            N = 'Traditional Chinese medicine (TCM) herbs exhibit a wide range of pharmacological effects and ' \
                'therapeutic properties. They have been used to regulate emotions, promote blood circulation, ' \
                'clear heat and toxins, nourish Yin and tonify the Kidneys, boost Qi and nourish Blood, and reduce ' \
                'swelling and relieve pain. These herbs work holistically to restore balance and harmony in the body, ' \
                'addressing various health conditions and promoting overall well-being. It is important to consult ' \
                'with a qualified healthcare professional or TCM practitioner for personalized guidance on the ' \
                'appropriate use and dosage of TCM herbs. TCM herbs possess anti-inflammatory and analgesic ' \
                'properties, making them effective in reducing swelling and relieving pain. They can be used ' \
                'topically or internally to alleviate various types of pain, including musculoskeletal pain, ' \
                'headaches, and menstrual cramps. It is important to note that TCM herbs are typically prescribed in ' \
                'combination, as part of a holistic treatment approach. The selection and formulation of herbs depend ' \
                'on the individual specific condition and constitution, as well as the underlying pattern of ' \
                'imbalance. Therefore, it is essential to consult with a qualified healthcare professional or TCM ' \
                'practitioner to receive personalized guidance on the appropriate use, dosage, and formulation of TCM ' \
                'herbs. '
            self.label.setWordWrap(True)  # 设置label文本自动换行
            # 设置英文文字行间距为1.5倍
            style_sheet = "QLabel { line-height: 150%; }"
            self.label.setStyleSheet(style_sheet)
            self.label.setText(N)

    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        classfication = Classification()

        while True:
            img = self.file_names
            try:
                image = Image.open(img)
            except:
                print('Open Error! Try again!')
                continue
            else:
                self.class_name = classfication.detect_image(image)
                font = self.label_2.font()  # 获取当前字体
                font.setPointSize(16)  # 设置字体大小为16
                self.label_2.setFont(font)  # 应用新的字体
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)  # 将文本水平居中对齐
                self.label_2.setText(self.class_name)
                break


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ui = MainWindow()
    ui = CandyWindow.createWindow(ui, 'blueGreen')
    ui.show()
    sys.exit(app.exec_())
