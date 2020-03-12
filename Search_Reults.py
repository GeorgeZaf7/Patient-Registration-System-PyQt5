# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# File Name:    Search_Results.py
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


class Search_Res(QWidget):
    def __init__(self, pat):
        super().__init__()
        self.title = "Patient Registration System"
        self.left = 0
        self.top = 0
        self.width = 640
        self.height = 480
        self.patient = pat
        self.initUI(self.patient)

    def initUI(self, a):
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

        self.lbl_pag_title = QLabel('Search Results')
        self.lbl_pag_title.setFont(QtGui.QFont("Arial", 25, QFont.Bold))
        self.lbl_pag_title.setAlignment(QtCore.Qt.AlignCenter)
        # self.lbl_pag_title.setFixedWidth(100)
        self.lbl_pag_title.setFixedHeight(50)
        grid_layout.addWidget(self.lbl_pag_title, 0, 0, 1, 2)

        self.patient = a
        print_Data = 'Patient ID: ' + str(self.patient[0]) + '\nName: ' + str(self.patient[1]) + "\nSurname: " + str(self.patient[2]) + "\nAddress: " + str(
            self.patient[3]) + "\nPostcode: " + str(self.patient[4]) + "\nCity: " + str(self.patient[5]) + \
                     "\nMobile: " + str(self.patient[6]) + "\nEmail: " + str(self.patient[7]) + "\nDate of Birth: " + str(
            self.patient[8]) + "\nGender: " + str(self.patient[9] + '\n')
        self.txt_pat_info = QTextEdit(self)
        self.txt_pat_info.setReadOnly(True)
        self.txt_pat_info.setFont(QFont('Arial', 12, QFont.Bold))
        self.txt_pat_info.setText(str(print_Data))
        grid_layout.addWidget(self.txt_pat_info, 1, 0, 1, 2, Qt.AlignJustify)
        #self.txt_pat_info.resize(100, 100)

        self.btn_MedRec = QPushButton('Add Medical')
        self.btn_MedRec.setToolTip('Add Medical Data')
        self.btn_MedRec.setStyleSheet('QPushButton {background-color: #FF0000; color: white;}')
        self.btn_MedRec.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_MedRec.setFixedWidth(300)
        self.btn_MedRec.setFixedHeight(40)
        self.btn_MedRec.clicked.connect(self.close)
        grid_layout.addWidget(self.btn_MedRec, 3, 0, 1, 2, Qt.AlignJustify)

        self.btn_Clr = QPushButton('Print')
        self.btn_Clr.setToolTip('Print')
        self.btn_Clr.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Clr.setStyleSheet('QPushButton {color: #FF0000;}')
        self.btn_Clr.setFixedWidth(300)
        self.btn_Clr.setFixedHeight(40)
        #self.btn_Clr.clicked.connect(self.btn_clr_clicked)
        grid_layout.addWidget(self.btn_Clr, 4, 0, 1, 2, Qt.AlignJustify)

        self.btn_Back = QPushButton('Back')
        self.btn_Back.setToolTip('Clear Sections')
        self.btn_Back.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Back.setFixedWidth(300)
        self.btn_Back.setFixedHeight(40)
        self.btn_Back.clicked.connect(self.close)
        grid_layout.addWidget(self.btn_Back, 5, 0, 1, 2, Qt.AlignJustify)

        # ===============================
        self.empty = QLabel('')
        self.empty.setFixedHeight(70)
        grid_layout.addWidget(self.empty, 6, 0)

        self.lbl_ariston = QLabel('© AristonAQ Ltd, 2020')
        self.lbl_ariston.setFont(QtGui.QFont("Times", 8))
        self.lbl_ariston.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ariston.setFrameShape(QFrame.Panel)
        self.lbl_ariston.setFrameShadow(QFrame.Sunken)
        self.lbl_ariston.setLineWidth(2)  # lbl_user.setFixedWidth(100)
        self.lbl_ariston.setFixedHeight(20)
        grid_layout.addWidget(self.lbl_ariston, 7, 0, 1, 2)

        # Functions for buttons



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Search_Res()
    ex.show()
    sys.exit(app.exec())