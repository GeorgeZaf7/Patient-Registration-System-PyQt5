import sys
import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, qApp, QTextEdit, QMessageBox, \
    QFontDialog, QStatusBar, QFileDialog, QGridLayout, QLabel, QDesktopWidget, QFrame
from PyQt5.QtGui import QIcon, QFont, QPalette, QLinearGradient, QColor, QBrush
from PyQt5 import QtCore, QtWidgets, QtGui


class Med_Rec(QWidget):
    def __init__(self): #pat
        super().__init__()
        self.title = "Patient Registration System"
        self.left = 0
        self.top = 0
        self.width = 640
        self.height = 480
        #self.patient = pat
        self.initUI() #self.patient

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.setWindowIcon(QIcon('Resized_logo.png'))
        # QMessageBox.about(self, 'AristonAQ Ltd', "\n   Welcome to AristonREG!\nA Patient Registering System")

        p = QPalette()
        gradient = QLinearGradient(0, 50, 0, 300)
        gradient.setColorAt(1.0, QColor(204, 240, 240))  # 204, 240, 240
        gradient.setColorAt(0.0, QColor(233, 112, 112))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)  #


        grid_layout = QGridLayout()
        self.setLayout(grid_layout)


        self.lbl_pag_title = QLabel('Patient Medical Records')
        self.lbl_pag_title.setFont(QtGui.QFont("Arial", 25, QFont.Bold))
        self.lbl_pag_title.setAlignment(QtCore.Qt.AlignCenter)
        # self.lbl_pag_title.setFixedWidth(100)
        self.lbl_pag_title.setFixedHeight(50)
        grid_layout.addWidget(self.lbl_pag_title, 0, 0, 1, 2)

        #================================
        self.btn_Read = QPushButton('Retrieve\nPatient\nMedical\nRecords')
        self.btn_Read.setToolTip('Go to previous window')
        self.btn_Read.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Read.setFixedWidth(200)
        self.btn_Read.setFixedHeight(200)
        self.btn_Read.clicked.connect(self.close)
        grid_layout.addWidget(self.btn_Read, 1, 0, Qt.AlignCenter)

        self.btn_Add = QPushButton('Add\nPatient\nMedical\nRecords')
        self.btn_Add.setToolTip('Go to previous window')
        self.btn_Add.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Add.setFixedWidth(200)
        self.btn_Add.setFixedHeight(200)
        self.btn_Add.clicked.connect(self.close)
        grid_layout.addWidget(self.btn_Add, 1, 1, Qt.AlignCenter)

        self.btn_Exit = QPushButton('Exit')
        self.btn_Exit.setToolTip('Go to previous window')
        self.btn_Exit.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Exit.setFixedWidth(300)
        self.btn_Exit.setFixedHeight(40)
        self.btn_Exit.clicked.connect(self.close)
        grid_layout.addWidget(self.btn_Exit, 2, 0, 1, 2, Qt.AlignCenter)

        # ===============================
        self.empty = QLabel('')
        self.empty.setFixedHeight(70)
        grid_layout.addWidget(self.empty, 3, 0, 1, 2 )

        self.lbl_ariston = QLabel('© AristonAQ Ltd, 2020')
        self.lbl_ariston.setFont(QtGui.QFont("Times", 8))
        self.lbl_ariston.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ariston.setFrameShape(QFrame.Panel)
        self.lbl_ariston.setFrameShadow(QFrame.Sunken)
        self.lbl_ariston.setLineWidth(2)  # lbl_user.setFixedWidth(100)
        self.lbl_ariston.setFixedHeight(20)
        grid_layout.addWidget(self.lbl_ariston, 3+1, 0, 1, 2)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Med_Rec()
    ex.show()
    sys.exit(app.exec())