import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap, QImage

from test import *


class GUI(QMainWindow):

    def __init__(self, parent =None):
        super(GUI, self).__init__(parent)
        self.initUI()


    def initUI(self):
        self.resize(1500,500)
        self.setWindowTitle('imageProcessing')
        self.statusBar().showMessage('Author: Fei')
        self.horizontaol_vertical_box_layout()



    def horizontaol_vertical_box_layout(self):
        # label

        self.label_1 = QLabel('Input Image')
        self.label_1.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel('Output Image')
        self.label_2.setAlignment(Qt.AlignCenter)

        # button
        button_1 = QPushButton('The Original image')
        button_1.clicked.connect(self.btn1_clicked)

        button_2 = QPushButton('Use this image')
        button_2.clicked.connect(self.btn2_clicked)

        button_31 = QPushButton('Salt-Pepper')
        button_31.clicked.connect(self.btn31_clicked)
        button_32 = QPushButton('Avg Smooth')
        button_32.clicked.connect(self.btn32_clicked)
        button_33 = QPushButton('Median Smooth')
        button_33.clicked.connect(self.btn33_clicked)
        button_34 = QPushButton('T Binary')
        button_34.clicked.connect(self.btn34_clicked)
        button_35 = QPushButton('P-Tile Binary')
        button_35.clicked.connect(self.btn35_clicked)
        button_36 = QPushButton('Iterative Binary')
        button_36.clicked.connect(self.btn36_clicked)
        button_37 = QPushButton('Label Component')
        button_37.clicked.connect(self.btn37_clicked)

        vbox_1 = QVBoxLayout()
        vbox_1.addWidget(self.label_1)
        vbox_1.addWidget(button_1)

        vbox_2 = QVBoxLayout()
        vbox_2.addWidget(self.label_2)
        vbox_2.addWidget(button_2)

        vbox_3 = QVBoxLayout()
        vbox_3.addWidget(button_31)
        vbox_3.addWidget(button_32)
        vbox_3.addWidget(button_33)
        vbox_3.addWidget(button_34)
        vbox_3.addWidget(button_35)
        vbox_3.addWidget(button_36)
        vbox_3.addWidget(button_37)

        hbox_1 = QHBoxLayout()
        hbox_1.addLayout(vbox_1)
        hbox_1.addLayout(vbox_2)
        hbox_1.addLayout(vbox_3)

        layout_widget = QWidget()
        layout_widget.setLayout(hbox_1)

        self.setCentralWidget(layout_widget)


    # def btn1_clicked(self,checked):
    #     self.img1 = QFileDialog.getOpenFileName(self, 'OpenFile','.','Image Files(*.jpg *.jpeg *.png)')[0]
    #
    #     image1 = QImage(self.img1)
    #     self.label_1.setPixmap(QPixmap.fromImage(image1))



    def btn1_clicked(self,checked):
        self.img1 = mpimg.imread('sample.jpeg')
        self.img1.flags.writeable = True
        self.row, self.column, self.channel = self.img1.shape
        self.bytesPerLine = 3 * self.column
        qImg = QImage(self.img1.data, self.column, self.row, self.bytesPerLine, QImage.Format_RGB888)
        self.label_1.setPixmap(QPixmap.fromImage(qImg))
        plt.imshow(self.img1)
        # plt.savefig('sample4.png')
        plt.show()


    def btn31_clicked(self,checked):
        t = test(self.row, self.column, self.channel)
        self.img2 = t.salt_pepper(self.img1)
        qImg = QImage(self.img2.data, self.column, self.row, self.bytesPerLine, QImage.Format_RGB888)
        self.label_2.setPixmap(QPixmap.fromImage(qImg))

    def btn32_clicked(self,checked):
        t = test(self.row, self.column, self.channel)
        self.img2 = t.smooth_avg(self.img1)
        qImg = QImage(self.img2.data, self.column, self.row, self.bytesPerLine, QImage.Format_RGB888)
        self.label_2.setPixmap(QPixmap.fromImage(qImg))


    def btn33_clicked(self,checked):
        t = test(self.row, self.column, self.channel)
        self.img2 = t.smooth_median(self.img1)
        qImg = QImage(self.img2.data, self.column, self.row, self.bytesPerLine, QImage.Format_RGB888)
        self.label_2.setPixmap(QPixmap.fromImage(qImg))

    def btn34_clicked(self,checked):
        t = test(self.row, self.column, self.channel)
        self.img2 = t.binary_thresholding(self.img1)
        qImg = QImage(self.img2.data, self.column, self.row, self.bytesPerLine, QImage.Format_RGB888)
        self.label_2.setPixmap(QPixmap.fromImage(qImg))

    def btn35_clicked(self,checked):
        t = test(self.row, self.column, self.channel)
        self.img2 = t.binary_ptile(self.img1)
        qImg = QImage(self.img2.data, self.column, self.row, self.bytesPerLine, QImage.Format_RGB888)
        self.label_2.setPixmap(QPixmap.fromImage(qImg))

    def btn36_clicked(self,checked):
        t = test(self.row, self.column, self.channel)
        self.img2 = t.binary_iterative(self.img1)
        qImg = QImage(self.img2.data, self.column, self.row, self.bytesPerLine, QImage.Format_RGB888)
        self.label_2.setPixmap(QPixmap.fromImage(qImg))

    def btn37_clicked(self,checked):
        t = test(self.row, self.column, self.channel)
        self.img2 = t.labelComponents(self.img1)
        qImg = QImage(self.img2.data, self.column, self.row, self.bytesPerLine, QImage.Format_RGB888)
        self.label_2.setPixmap(QPixmap.fromImage(qImg))


    def btn2_clicked(self,checked):
        self.img1 = self.img2
        qImg = QImage(self.img1.data, self.column, self.row, self.bytesPerLine, QImage.Format_RGB888)
        self.label_1.setPixmap(QPixmap.fromImage(qImg))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())

