# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# File Name:    Add_User.py
# Project Name: Patient Registration System
# Author:       Georgios Zafeiropoulos
# Created:      23/02/2020
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


class AddUsr(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Patient Registration System"
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle(self.title)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.setWindowIcon(QIcon('Resized_logo.png'))

        p = QPalette()
        gradient = QLinearGradient(0, 100, 0, 300)
        gradient.setColorAt(1.0, QColor(204, 240, 255))  # 204, 240, 240
        gradient.setColorAt(0.0, QColor(240, 112, 112))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        self.lbl_pag_title = QLabel('Employee Registration')
        self.lbl_pag_title.setFont(QtGui.QFont("Arial", 25, QFont.Bold))
        self.lbl_pag_title.setAlignment(QtCore.Qt.AlignCenter)
        #self.lbl_pag_title.setFixedWidth(300)
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

        self.txt_Name = QLineEdit()
        self.txt_Name.setFont(QFont('Arial', 14))
        self.txt_Name.setPlaceholderText("Enter your name...")
        self.txt_Name.setFixedHeight(30)
        grid_layout.addWidget(self.txt_Name, 2, 1, 1, 2)  # row, column, rowSpan, columnSpan,
        # txt_User.setFixedWidth(250)

        self.lbl_Sname = QLabel('Surname:')
        self.lbl_Sname.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        self.lbl_Sname.setAlignment(QtCore.Qt.AlignCenter)
        # lbl_pass.setFixedWidth(100)
        grid_layout.addWidget(self.lbl_Sname, 3, 0)

        self.txt_Sname = QLineEdit()
        self.txt_Sname.setFont(QFont('Arial', 14))
        # txt_Pass.setFixedWidth(250)
        self.txt_Sname.setPlaceholderText("Enter your surname...")
        self.txt_Sname.setFixedHeight(30)
        grid_layout.addWidget(self.txt_Sname, 3, 1, 1, 2)


        self.lbl_user = QLabel('Username:')
        self.lbl_user.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        # lbl_user.setFixedWidth(100)
        self.lbl_user.setAlignment(QtCore.Qt.AlignCenter)
        grid_layout.addWidget(self.lbl_user, 4, 0)

        self.txt_User = QLineEdit()
        self.txt_User.setFont(QFont('Arial', 14))
        self.txt_User.setPlaceholderText("Enter your username...")
        self.txt_User.setFixedHeight(30)
        grid_layout.addWidget(self.txt_User, 4, 1, 1, 2)  # row, column, rowSpan, columnSpan,
        # txt_User.setFixedWidth(250)

        self.lbl_pass = QLabel('Password:')
        self.lbl_pass.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        self.lbl_pass.setAlignment(QtCore.Qt.AlignCenter)
        # lbl_pass.setFixedWidth(100)
        grid_layout.addWidget(self.lbl_pass, 5, 0)

        self.txt_Pass = QLineEdit()
        self.txt_Pass.setFont(QFont('Arial', 14))
        # txt_Pass.setFixedWidth(250)
        self.txt_Pass.setFixedHeight(30)
        self.txt_Pass.setPlaceholderText("Enter your password...")
        #self.txt_Pass.setEchoMode(QLineEdit.Password)
        #self.txt_Pass.setStyleSheet('lineedit-password-character: 9679')
        grid_layout.addWidget(self.txt_Pass, 5, 1, 1, 2)


        self.empty = QLabel('')
        self.empty.setFixedHeight(20)
        grid_layout.addWidget(self.empty, 7, 0, 1, 3)

        self.btn_Clear = QPushButton('Clear')
        self.btn_Clear.setToolTip('Clear Sections')
        self.btn_Clear.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Clear.setFixedWidth(150)
        self.btn_Clear.setFixedHeight(40)
        self.btn_Clear.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_Clear.clicked.connect(self.btn_clr_clicked)
        grid_layout.addWidget(self.btn_Clear, 8, 0)

        self.btn_Submit = QPushButton('Submit')
        self.btn_Submit.setToolTip('Login')
        self.btn_Submit.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Submit.setStyleSheet('QPushButton {background-color: #FF0000; color: white;}')
        self.btn_Submit.setFixedWidth(150)
        self.btn_Submit.setFixedHeight(40)
        self.btn_Submit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self. btn_Submit.clicked.connect(self.btn_submit_clicked)
        grid_layout.addWidget(self.btn_Submit, 8, 1)

        self.btn_Back = QPushButton('Back')
        self.btn_Back.setToolTip('Close Application')
        self.btn_Back.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Back.setFixedWidth(150)
        self.btn_Back.setFixedHeight(40)
        self.btn_Back.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_Back.clicked.connect(self.btn_back_clicked)
        grid_layout.addWidget(self.btn_Back, 8, 2)

        self.empty = QLabel('')
        self.empty.setFixedHeight(70)
        grid_layout.addWidget(self.empty, 9, 0, 1, 3)

        self.lbl_ariston = QLabel('© AristonAQ Ltd, 2020')
        self.lbl_ariston.setFont(QtGui.QFont("Times", 8))
        self. lbl_ariston.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ariston.setFrameShape(QFrame.Panel)
        self.lbl_ariston.setFrameShadow(QFrame.Sunken)
        self.lbl_ariston.setLineWidth(2)  # lbl_user.setFixedWidth(100)
        self.lbl_ariston.setFixedHeight(20)
        grid_layout.addWidget(self.lbl_ariston, 10, 0, 1, 3)


    def btn_clr_clicked(self):
        self.txt_User.setText("")
        self.txt_Pass.setText("")
        self.txt_Name.setText("")
        self.txt_Sname.setText("")

    def btn_submit_clicked(self):
        conn = sqlite3.connect('Login_Details_Database.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (name, surname, username, password)''')
        self.a1 = self.txt_Name.text()
        self.a2 = self.txt_Sname.text()
        self.a3 = self.txt_User.text()
        self.a4 = self.txt_Pass.text()
        self.add = [self.a1, self.a2, self.a3, self.a4]
        c.execute('''SELECT username FROM users WHERE username=?''', (self.txt_User.text(),))
        exists = c.fetchall()
        if not exists:
            c.execute('INSERT INTO users VALUES(?,?,?,?)', self.add)
            QMessageBox.information(self,'Successful', 'All Done!')
            self.txt_User.setText("")
            self.txt_Pass.setText("")
            self.txt_Name.setText("")
            self.txt_Sname.setText("")
            print(self.add)
        else:
            QMessageBox.warning(self, "Error", "Username already in use. Try again.")
            self.txt_User.setText("")
            self.txt_Pass.setText("")
            self.txt_Name.setText("")
            self.txt_Sname.setText("")
        conn.commit()

    def btn_back_clicked(self):
        self.close()

    def keyPressEvent(self, event):
        #if event.key() == Qt.Key_Return:
            #self.btn_submit_clicked()
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            if self.btn_Submit.hasFocus():
                self.btn_submit_clicked()
            if self.btn_Clear.hasFocus():
                self.btn_clr_clicked()
            if self.btn_Back.hasFocus():
                self.btn_back_clicked()

'''if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddUsr()
    ex.show()
    sys.exit(app.exec())'''