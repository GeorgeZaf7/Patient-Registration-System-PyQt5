# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# File Name:    Register.py
# Project Name: Patient Registration System
# Author:       Georgios Zafeiropoulos
# Created:      22/02/2020
# Modified:     10/03/2020
# Copyright:    (c) Georgios Zafeiropoulos, 2020
# License:      CC-BY
# ----------------------------------------------------------------------------
import sys
import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox, QLabel, QFrame, QDesktopWidget, \
    QGridLayout, QLineEdit, QRadioButton, QCalendarWidget
from PyQt5.QtGui import QIcon, QFont, QPalette, QLinearGradient, QColor, QBrush
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QDate


class Reg(QWidget):
    def __init__(self, usr):
        super().__init__()
        self.title = "Patient Registration System"
        self.left = 0
        self.top = 0
        self.width = 640
        self.height = 480

        global currentYear, currentMonth, currentDay
        currentDay = datetime.now().day
        currentMonth = datetime.now().month
        currentYear = datetime.now().year

        self.user = usr
        self.initUI(self.user)

    def initUI(self, a):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.setWindowIcon(QIcon('./icons/Resized_logo.png'))

        p = QPalette()
        gradient = QLinearGradient(0, 200, 0, 400)
        gradient.setColorAt(1.0, QColor(204, 240, 255))  # 204, 240, 240
        gradient.setColorAt(0.0, QColor(233, 112, 112))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)  #

        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        self.usr = a

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

        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.setStyleSheet('QCalendarWidget {background-color: rgb(90,31,0)}')
        self.calendar.setStyleSheet('QCalendarWidget QWidget {alternate-background-color: rgb(100,100,100)}')
        self.calendar.setMinimumDate(QDate(currentYear - 90, currentMonth, 1))
        self.calendar.setMaximumDate(QDate(currentYear, currentMonth, currentDay))
        self.calendar.clicked[QDate].connect(self.showDate)
        grid_layout.addWidget(self.calendar, 9, 1, 1, 2)


        '''self.dateedit = QDateEdit(self)
        self.dateedit.setDate(QDate.currentDate())
        self.dateedit.setMinimumDate(QDate(1900, 1, 1))
        self.dateedit.setMaximumDate(QDate(2100, 12, 31))
        self.dateedit.setFixedHeight(30)
        grid_layout.addWidget(self.dateedit, 9, 1, 1, 2)

        # Read date
        b = self.dateedit.date()
        var = b.toPyDate()
        print(var)'''

        self.lbl_gend = QLabel('Gender:')
        self.lbl_gend.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.DemiBold))
        self.lbl_gend.setAlignment(QtCore.Qt.AlignCenter)
        grid_layout.addWidget(self.lbl_gend, 10, 0)

        self.rd_btn_male = QRadioButton("Male")
        self.rd_btn_male.setChecked(True)
        self.rd_btn_male.setIcon(QIcon('icons/man24.png'))
        # self.rd_btn_male.toggled.connect(lambda: self.btnState(self.rd_btn_male))
        grid_layout.addWidget(self.rd_btn_male, 10, 1, QtCore.Qt.AlignJustify)

        self.rd_btn_female = QRadioButton("Female")
        self.rd_btn_female.setIcon(QIcon('icons/female24.png'))
        # self.rd_btn_female.toggled.connect(lambda: self.btnState(self.rd_btn_female))
        grid_layout.addWidget(self.rd_btn_female, 10, 2, QtCore.Qt.AlignJustify)

        self.empty = QLabel('')
        self.empty.setFixedHeight(30)
        grid_layout.addWidget(self.empty, 11, 0)

        self.btn_Register = QPushButton('Register')
        self.btn_Register.setToolTip('Register')
        self.btn_Register.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Register.setStyleSheet('QPushButton {background-color: #FF0000; color: white;}')
        self.btn_Register.setFixedWidth(300)
        self.btn_Register.setFixedHeight(40)
        self.btn_Register.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_Register.clicked.connect(self.btn_Reg_clicked)
        grid_layout.addWidget(self.btn_Register, 12, 1, 1, 2, QtCore.Qt.AlignJustify)

        self.btn_Exit = QPushButton('Exit')
        self.btn_Exit.setToolTip('Clear Sections')
        self.btn_Exit.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Exit.setFixedWidth(300)
        self.btn_Exit.setFixedHeight(40)
        self.btn_Exit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_Exit.clicked.connect(self.btn_exit_clicked)
        grid_layout.addWidget(self.btn_Exit, 13, 1, 1, 2, QtCore.Qt.AlignJustify)

        # ===============================
        self.empty = QLabel('')
        self.empty.setFixedHeight(70)
        grid_layout.addWidget(self.empty, 14, 0)

        self.lbl_ariston = QLabel('© AristonAQ Ltd, 2020')
        self.lbl_ariston.setFont(QtGui.QFont("Arial", 9, QFont.Bold))
        self.lbl_ariston.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ariston.setFrameShape(QFrame.Panel)
        self.lbl_ariston.setFrameShadow(QFrame.Sunken)
        self.lbl_ariston.setLineWidth(2)  # lbl_user.setFixedWidth(100)
        self.lbl_ariston.setFixedHeight(20)
        grid_layout.addWidget(self.lbl_ariston, 15, 0, 1, 3)

        # Functions for buttons

    def showDate(self, date):
        global new
        new = date.toString('yyyy-MM-dd')
        print(new)


    def btn_Reg_clicked(self):
        if self.rd_btn_male.isChecked() == True:
            gen = self.rd_btn_male.text()
        elif self.rd_btn_female.isChecked() == True:
            gen = self.rd_btn_female.text()
        '''b = self.dateedit.date()
        var = b.toPyDate()'''
        user_name = str(self.usr)
        print(user_name)

        conn = sqlite3.connect('Patient_DB.db')
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS patients (
                                    pat_id integer PRIMARY KEY NOT NULL,
                                    first_name text NOT NULL,
                                    last_name text NOT NULL,
                                    address text NOT NULL,
                                    postcode text NOT NULL,
                                    city text NOT NULL,
                                    mobile text NOT NULL,
                                    email txt NOT NULL,
                                    DoB text NOT NULL,
                                    gender text NOT NULL,
                                    user text NOT NULL
                            )""")

        patient_id = """INSERT INTO patients (first_name, last_name, address, postcode, city, mobile, email, DoB, 
                gender, user) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """

        cur.execute(patient_id,
                    (self.txt_name.text(), self.txt_sname.text(), self.txt_addr.text(), self.txt_post.text(),
                     self.txt_city.text(), self.txt_mob.text(), self.txt_email.text(), new, gen, user_name))
        self.txt_name.clear()
        self.txt_sname.clear()
        self.txt_addr.clear()
        self.txt_post.clear()
        self.txt_city.clear()
        self.txt_mob.clear()
        self.txt_email.clear()
        QMessageBox.information(self, 'Successful', 'All Done!')
        for row in cur.execute('SELECT * FROM patients'):
            print(row)
        conn.commit()
        conn.close()

    def btn_exit_clicked(self):
        self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            if self.btn_Register.hasFocus():
                self.btn_Reg_clicked()
            if self.btn_Exit.hasFocus():
                self.btn_exit_clicked()

'''if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Reg()
    ex.show()
    sys.exit(app.exec())'''
