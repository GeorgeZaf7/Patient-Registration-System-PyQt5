# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# File Name:    Medical_Records.py
# Project Name: Patient Registration System
# Author:       Georgios Zafeiropoulos
# Created:      11/03/2020
# Modified:     13/03/2020
# Copyright:    (c) Georgios Zafeiropoulos, 2020
# License:      CC-BY
# ----------------------------------------------------------------------------
import sys
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QMessageBox, QGridLayout, QLabel, QDesktopWidget, QFrame
from PyQt5.QtGui import QIcon, QFont, QPalette, QLinearGradient, QColor, QBrush
from PyQt5 import QtCore, QtGui
import Add_New_Medical_Note, Search_Patients_Medical_Records_By_Date


class Med_Rec(QWidget):
    def __init__(self, pat, usr):
        super().__init__()
        self.title = "Patient Registration System"
        self.left = 0
        self.top = 0
        self.width = 640
        self.height = 480
        self.patient = pat
        self.user = usr
        self.initUI(self.patient, self.user)  # self.patient

    def initUI(self, a, b):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.setWindowIcon(QIcon('./icons/Resized_logo.png'))
        # QMessageBox.about(self, 'AristonAQ Ltd', "\n   Welcome to AristonREG!\nA Patient Registering System")

        p = QPalette()
        gradient = QLinearGradient(0, 50, 0, 300)
        gradient.setColorAt(1.0, QColor(204, 240, 240))  # 204, 240, 240
        gradient.setColorAt(0.0, QColor(233, 112, 112))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)  #

        self.pat = a
        self.user_nam = b

        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        self.lbl_pag_title = QLabel('Patient Medical Records')
        self.lbl_pag_title.setFont(QtGui.QFont("Arial", 25, QFont.Bold))
        self.lbl_pag_title.setAlignment(QtCore.Qt.AlignCenter)
        # self.lbl_pag_title.setFixedWidth(100)
        self.lbl_pag_title.setFixedHeight(50)
        grid_layout.addWidget(self.lbl_pag_title, 0, 0, 1, 2)

        # ================================
        self.btn_Read = QPushButton('Retrieve\nPatient\nMedical\nRecords')
        self.btn_Read.setToolTip('Go to previous window')
        self.btn_Read.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Read.setStyleSheet('QPushButton {background-color: #FF0000; color: white;}')
        self.btn_Read.setFixedWidth(200)
        self.btn_Read.setFixedHeight(200)
        self.btn_Read.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_Read.clicked.connect(self.read_MedRec)
        grid_layout.addWidget(self.btn_Read, 1, 0, Qt.AlignCenter)

        self.btn_Add = QPushButton('Add\nPatient\nMedical\nRecords')
        self.btn_Add.setToolTip('Go to previous window')
        self.btn_Add.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Add.setStyleSheet('QPushButton {background-color: #FF0000; color: white;}')
        self.btn_Add.setFixedWidth(200)
        self.btn_Add.setFixedHeight(200)
        self.btn_Add.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_Add.clicked.connect(self.add_MedRec)
        grid_layout.addWidget(self.btn_Add, 1, 1, Qt.AlignCenter)

        self.btn_Exit = QPushButton('Exit')
        self.btn_Exit.setToolTip('Go to previous window')
        self.btn_Exit.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Exit.setFixedWidth(300)
        self.btn_Exit.setFixedHeight(40)
        self.btn_Exit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_Exit.clicked.connect(self.btn_exit_clicked)
        grid_layout.addWidget(self.btn_Exit, 2, 0, 1, 2, Qt.AlignCenter)

        # ===============================
        self.empty = QLabel('')
        self.empty.setFixedHeight(70)
        grid_layout.addWidget(self.empty, 3, 0, 1, 2)

        self.lbl_ariston = QLabel('© AristonAQ Ltd, 2020')
        self.lbl_ariston.setFont(QtGui.QFont("Arial", 9, QFont.Bold))
        self.lbl_ariston.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ariston.setFrameShape(QFrame.Panel)
        self.lbl_ariston.setFrameShadow(QFrame.Sunken)
        self.lbl_ariston.setLineWidth(2)  # lbl_user.setFixedWidth(100)
        self.lbl_ariston.setFixedHeight(20)
        grid_layout.addWidget(self.lbl_ariston, 3 + 1, 0, 1, 2)

    def read_MedRec(self):
        path_name = str(self.pat[1]) + "_" + str(self.pat[2]) + ".db"
        #look_up_folder = "C:/Users/Georgios/PycharmProjects/Patient_Registration_System/Patient_Medical_Records/" + path_name
        look_up_folder = "C:/Users/zafir/PycharmProjects/Patient_Registration_System/Patient_Medical_Records/" + path_name

        if os.path.isfile(look_up_folder):
            # print(self.calendar.date)
            #QMessageBox.information(self, 'Yeah', 'Douleuei!!')
            self.readMedRec = Search_Patients_Medical_Records_By_Date.Search_MedRec(look_up_folder)
            self.readMedRec.show()
        else:
            QMessageBox.warning(self, 'Warning', 'No Medical Records found.')
        return

    def add_MedRec(self):
        self.medrec = Add_New_Medical_Note.Add_Med_Rec(self.pat, self.user_nam)
        self.medrec.show()

    def btn_exit_clicked(self):
        self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            if self.btn_Read.hasFocus():
                self.read_MedRec()
            if self.btn_Add.hasFocus():
                self.add_MedRec()
            if self.btn_Exit.hasFocus():
                self.btn_exit_clicked()

'''if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Med_Rec()
    ex.show()
    sys.exit(app.exec())'''
