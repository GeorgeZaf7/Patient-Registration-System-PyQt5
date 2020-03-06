import sys
import sqlite3
import os
from datetime import datetime
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, qApp, QTextEdit, QMessageBox, \
    QFontDialog, QStatusBar, QFileDialog, QLabel, QVBoxLayout, QFrame, QSizePolicy, QDesktopWidget, QHBoxLayout, \
    QGridLayout, QLineEdit, QComboBox, QSpinBox, QDateEdit, QRadioButton
from PyQt5.QtGui import QIcon, QFont, QPalette, QLinearGradient, QColor, QBrush
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QDate


class Reg(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Patient Registration System"
        self.left = 0
        self.top = 0
        self.width = 640
        self.height = 480
        self.initUI()

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
        gradient = QLinearGradient(0, 0, 0, 400)
        gradient.setColorAt(1.0, QColor(204, 240, 255))  # 204, 240, 240
        gradient.setColorAt(0.0, QColor(255, 160, 160))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)  #

        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        self.lbl_pag_title = QLabel('Register A Patient')
        self.lbl_pag_title.setFont(QtGui.QFont("Arial", 25, QFont.Bold))
        self.lbl_pag_title.setAlignment(QtCore.Qt.AlignCenter)
        # lbl_user.setFixedWidth(100)
        self.lbl_pag_title.setFixedHeight(50)
        grid_layout.addWidget(self.lbl_pag_title, 0, 0, 1, 3)

        self.empty = QLabel('')
        self.empty.setFixedHeight(30)
        grid_layout.addWidget(self.empty, 1, 0, 1, 3)

        self.lbl_name = QLabel('Name:')
        self.lbl_name.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        # lbl_user.setFixedWidth(100)
        self.lbl_name.setAlignment(QtCore.Qt.AlignCenter)
        grid_layout.addWidget(self.lbl_name, 2, 0)

        self.txt_name = QLineEdit()
        self.txt_name.setFont(QFont('Arial', 14))
        self.txt_name.setFixedHeight(30)
        self.txt_name.setPlaceholderText("Enter your name...")
        grid_layout.addWidget(self.txt_name, 2, 1, 1, 2)  # row, column, rowSpan, columnSpan,

        self.lbl_sname = QLabel('Surname:')
        self.lbl_sname.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        self.lbl_sname.setAlignment(QtCore.Qt.AlignCenter)
        # lbl_pass.setFixedWidth(100)
        grid_layout.addWidget(self.lbl_sname, 3, 0)

        self.txt_sname = QLineEdit()
        self.txt_sname.setFont(QFont('Arial', 14))
        self.txt_sname.setFixedHeight(30)
        self.txt_sname.setPlaceholderText("Enter your surname...")
        grid_layout.addWidget(self.txt_sname, 3, 1, 1, 2)

        self.lbl_addr = QLabel('Address:')
        self.lbl_addr.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        self.lbl_addr.setAlignment(QtCore.Qt.AlignCenter)
        # lbl_pass.setFixedWidth(100)
        grid_layout.addWidget(self.lbl_addr, 4, 0)

        self.txt_addr = QLineEdit()
        self.txt_addr.setFont(QFont('Arial', 14))
        self.txt_addr.setFixedHeight(30)
        self.txt_addr.setPlaceholderText("Enter your address...")
        grid_layout.addWidget(self.txt_addr, 4, 1, 1, 2)

        self.lbl_city = QLabel('City:')
        self.lbl_city.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        self.lbl_city.setAlignment(QtCore.Qt.AlignCenter)
        # lbl_pass.setFixedWidth(100)
        grid_layout.addWidget(self.lbl_city, 5, 0)

        self.txt_city = QLineEdit()
        self.txt_city.setFont(QFont('Arial', 14))
        self.txt_city.setFixedHeight(30)
        self.txt_city.setPlaceholderText("Enter city name...")
        grid_layout.addWidget(self.txt_city, 5, 1, 1, 2)

        self.lbl_post = QLabel('Postcode:')
        self.lbl_post.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        self.lbl_post.setAlignment(QtCore.Qt.AlignCenter)
        # lbl_pass.setFixedWidth(100)
        grid_layout.addWidget(self.lbl_post, 6, 0)

        self.txt_post = QLineEdit()
        self.txt_post.setFont(QFont('Arial', 14))
        self.txt_post.setFixedHeight(30)
        self.txt_post.setPlaceholderText("Enter postcode...")
        grid_layout.addWidget(self.txt_post, 6, 1, 1, 2)

        self.lbl_mob = QLabel('Mobile:')
        self.lbl_mob.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        self.lbl_mob.setAlignment(QtCore.Qt.AlignCenter)
        # lbl_pass.setFixedWidth(100)
        grid_layout.addWidget(self.lbl_mob, 7, 0)

        self.txt_mob = QLineEdit()
        self.txt_mob.setFont(QFont('Arial', 14))
        self.txt_mob.setFixedHeight(30)
        self.txt_mob.setPlaceholderText("Enter mobile number...")
        grid_layout.addWidget(self.txt_mob, 7, 1, 1, 2)

        self.lbl_email = QLabel('Email:')
        self.lbl_email.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        self.lbl_email.setAlignment(QtCore.Qt.AlignCenter)
        # lbl_pass.setFixedWidth(100)
        grid_layout.addWidget(self.lbl_email, 8, 0)

        self.txt_email = QLineEdit()
        self.txt_email.setFont(QFont('Arial', 14))
        self.txt_email.setFixedHeight(30)
        self.txt_email.setPlaceholderText("Enter email...")
        grid_layout.addWidget(self.txt_email, 8, 1, 1, 2)

        self.lbl_dob = QLabel('Date of Birth:')
        self.lbl_dob.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        self.lbl_dob.setAlignment(QtCore.Qt.AlignCenter)
        # lbl_pass.setFixedWidth(100)
        grid_layout.addWidget(self.lbl_dob, 9, 0)

        self.dateedit = QDateEdit(self)
        self.dateedit.setDate(QDate.currentDate())
        self.dateedit.setMinimumDate(QDate(1900, 1, 1))
        self.dateedit.setMaximumDate(QDate(2100, 12, 31))
        self.dateedit.setFixedHeight(30)
        grid_layout.addWidget(self.dateedit, 9, 1, 1, 2)

        '''# Read date
        b = self.dateedit.date()
        var = b.toPyDate()
        print(var)'''

        self.lbl_gend = QLabel('Gender:')
        self.lbl_gend.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        self.lbl_gend.setAlignment(QtCore.Qt.AlignCenter)
        grid_layout.addWidget(self.lbl_gend, 10, 0)

        self.rd_btn = QRadioButton("Male")
        self.rd_btn.setChecked(True)
        self.rd_btn.gender = 'Male'
        self.rd_btn.setIcon(QIcon('icons/man24.png'))
        self.rd_btn.toggled.connect(self.onClicked)
        grid_layout.addWidget(self.rd_btn, 10, 1, QtCore.Qt.AlignJustify)

        self.rd_btn = QRadioButton("Female")
        self.rd_btn.gender = 'Female'
        self.rd_btn.setIcon(QIcon('icons/female24.png'))
        self.rd_btn.toggled.connect(self.onClicked)
        grid_layout.addWidget(self.rd_btn, 10, 2, QtCore.Qt.AlignJustify)

        self.empty = QLabel('')
        self.empty.setFixedHeight(30)
        grid_layout.addWidget(self.empty, 11, 0)

        self.btn_Register = QPushButton('Register')
        self.btn_Register.setToolTip('Register')
        self.btn_Register.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Register.setFixedWidth(300)
        self.btn_Register.setFixedHeight(40)
        self.btn_Register.clicked.connect(self.btn_Reg_clicked)
        grid_layout.addWidget(self.btn_Register, 12, 1, 1, 2, QtCore.Qt.AlignJustify)

        self.btn_Back = QPushButton('Back')
        self.btn_Back.setToolTip('Clear Sections')
        self.btn_Back.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Back.setFixedWidth(300)
        self.btn_Back.setFixedHeight(40)
        self.btn_Back.clicked.connect(self.close)
        grid_layout.addWidget(self.btn_Back, 13, 1, 1, 2, QtCore.Qt.AlignJustify)

        # ===============================
        self.empty = QLabel('')
        self.empty.setFixedHeight(70)
        grid_layout.addWidget(self.empty, 14, 0)

        self.lbl_ariston = QLabel('© AristonAQ Ltd, 2020')
        self.lbl_ariston.setFont(QtGui.QFont("Times", 8))
        self.lbl_ariston.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ariston.setFrameShape(QFrame.Panel)
        self.lbl_ariston.setFrameShadow(QFrame.Sunken)
        self.lbl_ariston.setLineWidth(2)  # lbl_user.setFixedWidth(100)
        self.lbl_ariston.setFixedHeight(20)
        grid_layout.addWidget(self.lbl_ariston, 15, 0, 1, 3)

        # Functions for buttons

    def onClicked(self):
        self.rd_btn = self.sender()
        if self.rd_btn.isChecked():
            print("Gender is %s" % (self.rd_btn.gender))

    def btn_Reg_clicked(self):
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('Resize_Logo.png'))
    ex = Reg()
    ex.show()
    sys.exit(app.exec())
