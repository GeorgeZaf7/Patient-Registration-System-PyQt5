# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# File Name:    Main.py
# Project Name: Patient Registration System
# Author:       Georgios Zafeiropoulos
# Created:      20/02/2020
# Modified:     10/03/2020
# Copyright:    (c) Georgios Zafeiropoulos, 2020
# License:      CC-BY
# ----------------------------------------------------------------------------
import sys
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, qApp, QTextEdit, QMessageBox, \
    QFontDialog, QStatusBar, QFileDialog, QLabel, QVBoxLayout, QFrame, QSizePolicy, QDesktopWidget, QHBoxLayout, \
    QGridLayout, QLineEdit
from PyQt5.QtGui import QIcon, QFont, QPalette, QLinearGradient, QColor, QBrush
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
import Add_User
import Search


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Patient Registration System"
        # self.left = 0
        # self.top = 0
        # self.width = 500
        # self.height = 300
        self.initUI()
        # self.dialog = Welcome_Window.welc()
        # self.dialog.show()

    def initUI(self):
        self.setWindowTitle(self.title)
        # self.setGeometry(self.left, self.top, self.width, self.height)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.setWindowIcon(QIcon('Resized_logo.png'))
        QMessageBox.about(self, 'AristonAQ Ltd', "\n   Welcome to AristonREG!\nA Patient Registering System")

        p = QPalette()
        gradient = QLinearGradient(0, 50, 0, 300)
        gradient.setColorAt(1.0, QColor(204, 240, 255))  # 204, 240, 240
        gradient.setColorAt(0.0, QColor(240,112, 112)) #240, 160, 160
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)  #

        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        self.lbl_pag_title = QLabel('Please Login')
        self.lbl_pag_title.setFont(QtGui.QFont("Arial", 25, QFont.Bold))
        self.lbl_pag_title.setAlignment(QtCore.Qt.AlignCenter)
        # lbl_user.setFixedWidth(100)
        self.lbl_pag_title.setFixedHeight(50)
        grid_layout.addWidget(self.lbl_pag_title, 0, 0, 1, 3)

        self.empty = QLabel('')
        self.empty.setFixedHeight(30)
        grid_layout.addWidget(self.empty, 1, 0, 1, 3)

        self.lbl_user = QLabel('Username:')
        self.lbl_user.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        # lbl_user.setFixedWidth(100)
        self.lbl_user.setAlignment(QtCore.Qt.AlignCenter)
        grid_layout.addWidget(self.lbl_user, 2, 0)

        self.txt_User = QLineEdit()
        self.txt_User.setFont(QFont('Arial', 14))
        self.txt_User.setPlaceholderText("Enter your username...")
        self.txt_User.setFixedHeight(30)
        grid_layout.addWidget(self.txt_User, 2, 1, 1, 2)  # row, column, rowSpan, columnSpan,
        # txt_User.setFixedWidth(250)

        self.lbl_pass = QLabel('Password:')
        self.lbl_pass.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        self.lbl_pass.setAlignment(QtCore.Qt.AlignCenter)
        # lbl_pass.setFixedWidth(100)
        grid_layout.addWidget(self.lbl_pass, 3, 0)

        self.txt_Pass = QLineEdit()
        self.txt_Pass.setFont(QFont('Arial', 14))
        # txt_Pass.setFixedWidth(250)
        self.txt_Pass.setFixedHeight(30)
        self.txt_Pass.setPlaceholderText("Enter your password...")
        self.txt_Pass.setEchoMode(QLineEdit.Password)
        self.txt_Pass.setStyleSheet('lineedit-password-character: 9679')
        grid_layout.addWidget(self.txt_Pass, 3, 1, 1, 2)

        self.empty = QLabel('')
        self.empty.setFixedHeight(30)
        grid_layout.addWidget(self.empty, 4, 0, 1, 3)

        self.btn_Submit = QPushButton('Submit')
        self.btn_Submit.setToolTip('Login')
        self.btn_Submit.setStyleSheet('QPushButton {background-color: #FF0000; color: white;}')
        self.btn_Submit.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Submit.setFixedWidth(150)
        self.btn_Submit.setFixedHeight(40)
        self.btn_Submit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self. btn_Submit.clicked.connect(self.btn_submit_clicked)
        grid_layout.addWidget(self.btn_Submit, 5, 1)

        self.btn_Clear = QPushButton('Clear')
        self.btn_Clear.setToolTip('Clear Sections')
        self.btn_Clear.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Clear.setFixedWidth(150)
        self.btn_Clear.setFixedHeight(40)
        self.btn_Clear.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_Clear.clicked.connect(self.btn_clr_clicked)
        grid_layout.addWidget(self.btn_Clear, 5, 0)

        self.btn_Exit = QPushButton('Exit')
        self.btn_Exit.setToolTip('Close Application')
        self.btn_Exit.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Exit.setFixedWidth(150)
        self.btn_Exit.setFixedHeight(40)
        self.btn_Exit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_Exit.clicked.connect(self.btn_exit_clicked)
        grid_layout.addWidget(self.btn_Exit, 5, 2)

        self.btn_AddUser = QPushButton('Add User')
        self.btn_AddUser.setToolTip('Add New User')
        self.btn_AddUser.setStyleSheet('QPushButton {color: #FF0000;}')
        self.btn_AddUser.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_AddUser.setFixedWidth(150)
        self.btn_AddUser.setFixedHeight(40)
        self.btn_AddUser.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_AddUser.clicked.connect(self.btn_addusr_clicked)
        self.dialogs = list()
        grid_layout.addWidget(self.btn_AddUser, 6, 1)

        self.empty = QLabel('')
        self.empty.setFixedHeight(70)
        grid_layout.addWidget(self.empty, 7, 0, 1, 3)

        self.lbl_ariston = QLabel('© AristonAQ Ltd, 2020')
        self.lbl_ariston.setFont(QtGui.QFont("Times", 8))
        self. lbl_ariston.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ariston.setFrameShape(QFrame.Panel)
        self.lbl_ariston.setFrameShadow(QFrame.Sunken)
        self.lbl_ariston.setLineWidth(2)  # lbl_user.setFixedWidth(100)
        self.lbl_ariston.setFixedHeight(20)
        grid_layout.addWidget(self.lbl_ariston, 8, 0, 1, 3)

    # vvvvvvvvvvvvvvvv Functions for buttons vvvvvvvvvvvvvvvvvvvvvvv

    def btn_exit_clicked(self):
        sys.exit()

    def btn_clr_clicked(self):
        self.txt_User.clear()#setText("")
        self.txt_Pass.clear()#setText("")

    def btn_submit_clicked(self):
        conn = sqlite3.connect('Login_Details_Database.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (username, password)''')
        user = self.txt_User.text()
        pas = self.txt_Pass.text()
        c.execute('''SELECT username, password FROM users WHERE username=? AND password=?''', (user, pas,))
        exists = c.fetchall()
        print(exists)
        if not exists:
            QMessageBox.warning(self, "Error", "Invalid Login Details.\n\n   Please try again.")
            self.txt_User.clear()#setText("")
            self.txt_Pass.clear()#setText("")
            return
        else:
            self.txt_User.setText("")
            self.txt_Pass.setText("")
            self.dialogs = Search.Search()
            #self.dialogs.append(self.dialogs)
            self.dialogs.show()
        conn.commit()
        conn.close()
        self.showMinimized()


    def btn_addusr_clicked(self):
        conn = sqlite3.connect('Login_Details_Database.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (name, surname, username, password)''')
        user = self.txt_User.text()
        pas = self.txt_Pass.text()
        c.execute('''SELECT username, password FROM users WHERE username=? AND password=?''', (user, pas,))
        exists = c.fetchall()
        print(exists)
        if not exists:
            QMessageBox.warning(self, "Error", "Verified User Required.\n\nAdd Login Details.")
            self.txt_User.setText("")
            self.txt_Pass.setText("")
            return
        else:
            self.txt_User.setText("")
            self.txt_Pass.setText("")
            self.dialogs = Add_User.AddUsr()
            #self.dialogs.append(self.dialogs)
            self.dialogs.show()
        conn.commit()
        # Close connection
        conn.close()
        self.showMinimized()

    def keyPressEvent(self, event):
        #if event.key() == Qt.Key_Return:
            #self.btn_submit_clicked()
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            if self.btn_Submit.hasFocus():
                self.btn_submit_clicked()
            if self.btn_Exit.hasFocus():
                self.btn_exit_clicked()
            if self.btn_AddUser.hasFocus():
                self.btn_addusr_clicked()
            if self.btn_Clear.hasFocus():
                self.btn_clr_clicked()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('Resize_Logo.png'))
    ex = Main()
    ex.show()
    sys.exit(app.exec())
