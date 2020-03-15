
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# File Name:    Search.py
# Project Name: Patient Registration System
# Author:       Georgios Zafeiropoulos
# Created:      21/02/2020
# Modified:     10/03/2020
# Copyright:    (c) Georgios Zafeiropoulos, 2020
# License:      CC-BY
# ----------------------------------------------------------------------------
import sys
import sqlite3
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, qApp, QTextEdit, QMessageBox, \
    QFontDialog, QStatusBar, QFileDialog, QLabel, QVBoxLayout, QFrame, QSizePolicy, QDesktopWidget, QHBoxLayout, \
    QGridLayout, QLineEdit
from PyQt5.QtGui import QIcon, QFont, QPalette, QLinearGradient, QColor, QBrush
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
import Register, Search_Reults


class Search(QWidget):
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
        gradient = QLinearGradient(0, 50, 0, 300)
        gradient.setColorAt(1.0, QColor(204, 240, 240))  # 204, 240, 240
        gradient.setColorAt(0.0, QColor(233, 112, 112))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)  #

        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        self.lbl_pag_title = QLabel('Search Patient Database')
        self.lbl_pag_title.setFont(QtGui.QFont("Arial", 25, QFont.Bold))
        self.lbl_pag_title.setAlignment(QtCore.Qt.AlignCenter)
        #self.lbl_pag_title.setFixedWidth(100)
        self.lbl_pag_title.setFixedHeight(50)
        grid_layout.addWidget(self.lbl_pag_title, 0, 0, 1, 2)

        self.empty = QLabel('')
        self.empty.setFixedHeight(30)
        grid_layout.addWidget(self.empty, 1, 0)

        self.lbl_name = QLabel('Name:')
        self.lbl_name.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        self.lbl_name.setFixedWidth(100)
        self.lbl_name.setAlignment(QtCore.Qt.AlignCenter)
        grid_layout.addWidget(self.lbl_name, 2, 0)

        self.txt_name = QLineEdit()
        self.txt_name.setFont(QFont('Arial', 14))
        self.txt_name.setPlaceholderText("Enter your name...")
        self.txt_name.setFixedWidth(400)
        self.txt_name.setFixedHeight(30)
        grid_layout.addWidget(self.txt_name, 2, 1)  # row, column, rowSpan, columnSpan,

        self.lbl_sname = QLabel('Surname:')
        self.lbl_sname.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        self.lbl_sname.setAlignment(QtCore.Qt.AlignCenter)
        # lbl_pass.setFixedWidth(100)
        grid_layout.addWidget(self.lbl_sname, 3, 0)

        self.txt_sname = QLineEdit()
        self.txt_sname.setFont(QFont('Arial', 14))
        self.txt_sname.setFixedWidth(400)
        self.txt_sname.setFixedHeight(30)
        self.txt_sname.setPlaceholderText("Enter your surname...")
        grid_layout.addWidget(self.txt_sname, 3, 1)

        self.lbl_post = QLabel('Postcode:')
        self.lbl_post.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        self.lbl_post.setAlignment(QtCore.Qt.AlignCenter)
        #self.lbl_post.setFixedWidth(100)
        grid_layout.addWidget(self.lbl_post, 4, 0)

        self.txt_post = QLineEdit()
        self.txt_post.setFont(QFont('Arial', 14))
        self.txt_post.setFixedWidth(400)
        self.txt_post.setFixedHeight(30)
        self.txt_post.setPlaceholderText("Enter postcode...")
        grid_layout.addWidget(self.txt_post, 4, 1)

        self.lbl_mob = QLabel('Mobile:')
        self.lbl_mob.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        self.lbl_mob.setAlignment(QtCore.Qt.AlignCenter)
        #self.lbl_mob.setFixedWidth(100)
        grid_layout.addWidget(self.lbl_mob, 5, 0, Qt.AlignCenter)

        self.txt_mob = QLineEdit()
        self.txt_mob.setFont(QFont('Arial', 14))
        self.txt_mob.setFixedWidth(400)
        self.txt_mob.setFixedHeight(30)
        self.txt_mob.setPlaceholderText("Enter mobile number...")
        grid_layout.addWidget(self.txt_mob, 5, 1)

        # ========= Buttons==============
        self.btn_Search = QPushButton('Search')
        self.btn_Search.setToolTip('Login')
        self.btn_Search.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Search.setStyleSheet('QPushButton {background-color: #FF0000; color: white;}')

        self.btn_Search.setFixedWidth(300)
        self.btn_Search.setFixedHeight(40)
        self.btn_Search.clicked.connect(self.btn_search_clicked)
        grid_layout.addWidget(self.btn_Search, 6, 1, Qt.AlignCenter)

        self.btn_Reg = QPushButton('Register')
        self.btn_Reg.setToolTip('Clear Sections')
        self.btn_Reg.setStyleSheet('QPushButton {color: #FF0000;}')
        self.btn_Reg.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Reg.setFixedWidth(300)
        self.btn_Reg.setFixedHeight(40)
        self.btn_Reg.clicked.connect(self.btn_Reg_clicked)
        grid_layout.addWidget(self.btn_Reg, 7, 1, Qt.AlignCenter)

        self.btn_Clr = QPushButton('Clear')
        self.btn_Clr.setToolTip('Login')
        self.btn_Clr.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Clr.setFixedWidth(300)
        self.btn_Clr.setFixedHeight(40)
        self.btn_Clr.clicked.connect(self.btn_clr_clicked)
        grid_layout.addWidget(self.btn_Clr, 8, 1, Qt.AlignCenter)

        self.btn_Back = QPushButton('Back')
        self.btn_Back.setToolTip('Go to previous window')
        self.btn_Back.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Back.setFixedWidth(300)
        self.btn_Back.setFixedHeight(40)
        self.btn_Back.clicked.connect(self.close)
        grid_layout.addWidget(self.btn_Back, 9, 1, Qt.AlignCenter)

        # ===============================
        self.empty = QLabel('')
        self.empty.setFixedHeight(70)
        grid_layout.addWidget(self.empty, 10, 0)

        self.lbl_ariston = QLabel('© AristonAQ Ltd, 2020')
        self.lbl_ariston.setFont(QtGui.QFont("Times", 8))
        self.lbl_ariston.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ariston.setFrameShape(QFrame.Panel)
        self.lbl_ariston.setFrameShadow(QFrame.Sunken)
        self.lbl_ariston.setLineWidth(2)  # lbl_user.setFixedWidth(100)
        self.lbl_ariston.setFixedHeight(20)
        grid_layout.addWidget(self.lbl_ariston, 11, 0, 1, 2)

        # Functions for buttons

    def btn_search_clicked(self):
        if self.txt_name.text() =="" or self.txt_sname.text() == "" or self.txt_post.text() =="" or self.txt_mob.text() == "":
            QMessageBox.warning(self, "Error", "Please fill in the patient details.")
        else:
            conn = sqlite3.connect('Patient_DB.db')
            cur = conn.cursor()
            a = self.txt_name.text()
            b = self.txt_sname.text()
            c = self.txt_post.text()
            d = self.txt_mob.text()
            cur.execute('''SELECT first_name, last_name, postcode, mobile FROM patients WHERE first_name=? AND last_name=? AND postcode=? AND mobile=? ''', (a, b, c, d,))
            exists = cur.fetchall()
            #print(exists)
            if not exists:
                QMessageBox.warning(self, "Error", "Patient Does Not Exist.")
                self.txt_name.clear()
                self.txt_sname.clear()
                self.txt_post.clear()
                self.txt_mob.clear()
                return
            else:
                #QMessageBox.information(self, "Successful", 'Patient Exists')
                cur.execute('SELECT * FROM patients WHERE postcode=? AND mobile=?', (c, d,))
                pat = cur.fetchone()
                self.new = Search_Reults.Search_Res(pat)
                self.new.show()
                self.txt_name.clear()
                self.txt_sname.clear()
                self.txt_post.clear()
                self.txt_mob.clear()
            conn.commit()
            # Close connection
            conn.close()

    def btn_Reg_clicked(self):
        self.txt_name.setText("")
        self.txt_sname.setText("")
        self.txt_post.setText("")
        self.txt_mob.setText("")
        self.dialogs = Register.Reg()
        self.dialogs.show()

    def btn_clr_clicked(self):
        self.txt_name.setText("")
        self.txt_sname.setText("")
        self.txt_post.setText("")
        self.txt_mob.setText("")
        return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Search()
    ex.show()
    sys.exit(app.exec())
