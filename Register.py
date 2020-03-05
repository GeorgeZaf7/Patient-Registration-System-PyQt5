import sys
import sqlite3
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, qApp, QTextEdit, QMessageBox, \
    QFontDialog, QStatusBar, QFileDialog, QLabel, QVBoxLayout, QFrame, QSizePolicy, QDesktopWidget, QHBoxLayout, \
    QGridLayout, QLineEdit
from PyQt5.QtGui import QIcon, QFont, QPalette, QLinearGradient, QColor, QBrush
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt

class Reg(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Patient Registration System"
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        # self.setGeometry(self.left, self.top, self.width, self.height)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.center())
        self.setWindowIcon(QIcon('Resized_logo.png'))
        # QMessageBox.about(self, 'AristonAQ Ltd', "\n   Welcome to AristonREG!\nA Patient Registering System")

        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 300)
        gradient.setColorAt(1.0, QColor(204, 240, 255))  # 204, 240, 240
        gradient.setColorAt(0.0, QColor(240, 160, 160))
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
        self.txt_name.setPlaceholderText("Enter your name...")
        grid_layout.addWidget(self.txt_name, 2, 1, 1, 2)  # row, column, rowSpan, columnSpan,
        # txt_User.setFixedWidth(250)

        self.lbl_sname = QLabel('Surname:')
        self.lbl_sname.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        self.lbl_sname.setAlignment(QtCore.Qt.AlignCenter)
        # lbl_pass.setFixedWidth(100)
        grid_layout.addWidget(self.lbl_sname, 3, 0)

        self.txt_sname = QLineEdit()
        self.txt_sname.setFont(QFont('Arial', 14))
        # txt_Pass.setFixedWidth(250)
        self.txt_sname.setPlaceholderText("Enter your surname...")
        # self.txt_sname.setEchoMode(QLineEdit.Password)
        # self.txt_sname.setStyleSheet('lineedit-password-character: 9679')
        grid_layout.addWidget(self.txt_sname, 3, 1, 1, 2)

        self.lbl_addr = QLabel('Address:')
        self.lbl_addr.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        self.lbl_addr.setAlignment(QtCore.Qt.AlignCenter)
        # lbl_pass.setFixedWidth(100)
        grid_layout.addWidget(self.lbl_addr, 4, 0)

        self.txt_addr = QLineEdit()
        self.txt_addr.setFont(QFont('Arial', 14))
        # txt_Pass.setFixedWidth(250)
        self.txt_addr.setPlaceholderText("Enter your address...")
        grid_layout.addWidget(self.txt_addr, 4, 1, 1, 2)

        self.lbl_city = QLabel('City:')
        self.lbl_city.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        self.lbl_city.setAlignment(QtCore.Qt.AlignCenter)
        # lbl_pass.setFixedWidth(100)
        grid_layout.addWidget(self.lbl_city, 5, 0)

        self.txt_city = QLineEdit()
        self.txt_city.setFont(QFont('Arial', 14))
        # txt_Pass.setFixedWidth(250)
        self.txt_city.setPlaceholderText("Enter city name...")
        grid_layout.addWidget(self.txt_city, 5, 1, 1, 2)

        self.lbl_post = QLabel('Postcode:')
        self.lbl_post.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        self.lbl_post.setAlignment(QtCore.Qt.AlignCenter)
        # lbl_pass.setFixedWidth(100)
        grid_layout.addWidget(self.lbl_post, 6, 0)

        self.txt_post = QLineEdit()
        self.txt_post.setFont(QFont('Arial', 14))
        # txt_Pass.setFixedWidth(250)
        self.txt_post.setPlaceholderText("Enter postcode...")
        grid_layout.addWidget(self.txt_post, 6, 1, 1, 2)

        self.lbl_mob = QLabel('Mobile:')
        self.lbl_mob.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        self.lbl_mob.setAlignment(QtCore.Qt.AlignCenter)
        # lbl_pass.setFixedWidth(100)
        grid_layout.addWidget(self.lbl_mob, 7, 0)

        self.txt_mob = QLineEdit()
        self.txt_mob.setFont(QFont('Arial', 14))
        # txt_Pass.setFixedWidth(250)
        self.txt_mob.setPlaceholderText("Enter mobile number...")
        grid_layout.addWidget(self.txt_mob, 7, 1, 1, 2)

        self.lbl_email = QLabel('Email:')
        self.lbl_email.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        self.lbl_email.setAlignment(QtCore.Qt.AlignCenter)
        # lbl_pass.setFixedWidth(100)
        grid_layout.addWidget(self.lbl_email, 8, 0)

        self.txt_email = QLineEdit()
        self.txt_email.setFont(QFont('Arial', 14))
        # txt_Pass.setFixedWidth(250)
        self.txt_email.setPlaceholderText("Enter email...")
        grid_layout.addWidget(self.txt_email, 8, 1, 1, 2)


