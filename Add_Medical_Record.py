# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# File Name:    Add_Medical_Record.py
# Project Name: Patient Registration System
# Author:       Georgios Zafeiropoulos
# Created:      16/03/2020
# Modified:     16/03/2020
# Copyright:    (c) Georgios Zafeiropoulos, 2020
# License:      CC-BY
# ----------------------------------------------------------------------------
import sqlite3
import sys
import os
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, qApp, QTextEdit, QMessageBox, \
    QFontDialog, QStatusBar, QFileDialog, QGridLayout, QLabel, QDesktopWidget, QFrame
from PyQt5.QtGui import QIcon, QFont, QPalette, QLinearGradient, QColor, QBrush
from PyQt5 import QtCore, QtWidgets, QtGui


class Add_Med_Rec(QWidget):
    def __init__(self,pat): #pat
        super().__init__()
        self.title = "Patient Registration System"
        self.left = 0
        self.top = 0
        self.width = 640
        self.height = 480
        self.patient = pat
        self.initUI(self.patient) #self.patient

    def initUI(self,a): #a
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

        self.pat = a

        grid_layout = QGridLayout()
        self.setLayout(grid_layout)


        self.lbl_pag_title = QLabel('Add Notes')
        self.lbl_pag_title.setFont(QtGui.QFont("Arial", 25, QFont.Bold))
        self.lbl_pag_title.setAlignment(QtCore.Qt.AlignCenter)
        # self.lbl_pag_title.setFixedWidth(100)
        self.lbl_pag_title.setFixedHeight(50)
        grid_layout.addWidget(self.lbl_pag_title, 0, 0, 1, 2)

        self.empty = QLabel('')
        self.empty.setFixedHeight(40)
        grid_layout.addWidget(self.empty, 1, 0, 1, 2)


        pat_id = 'Patient ID: ' + str(self.pat[0])
        self.lbl_pat_id = QLabel(pat_id)
        self.lbl_pat_id.setFont(QtGui.QFont("Arial", 12, QFont.Bold))
        self.lbl_pat_id.setAlignment(QtCore.Qt.AlignCenter)
        # self.lbl_pag_title.setFixedWidth(100)
        self.lbl_pat_id.setFixedHeight(20)
        grid_layout.addWidget(self.lbl_pat_id, 2, 0, 1, 2, Qt.AlignLeft)

        pat_det = 'Patient Details: ' + str(self.pat[1]) + ' ' + str(self.pat[2])
        self.lbl_pat_id_1 = QLabel(pat_det)
        self.lbl_pat_id_1.setFont(QtGui.QFont("Arial", 12, QFont.Bold))
        #self.lbl_pat_id_1.setFixedWidth(10)
        self.lbl_pat_id_1.setFixedHeight(20)
        grid_layout.addWidget(self.lbl_pat_id_1, 3, 0, 1, 2, Qt.AlignLeft)

        self.date_now =  QDate.currentDate().toString('yyyy-MM-dd')
        self.date_visual = QDate.currentDate().toString('dd/MM/yyyy')
        self.date_now_1 = 'Date: ' + self.date_visual
        self.lbl_pat_id = QLabel(self.date_now_1)
        self.lbl_pat_id.setFont(QtGui.QFont("Arial", 12, QFont.Bold))
        self.lbl_pat_id.setAlignment(QtCore.Qt.AlignCenter)
        # self.lbl_pag_title.setFixedWidth(100)
        self.lbl_pat_id.setFixedHeight(20)
        grid_layout.addWidget(self.lbl_pat_id, 4, 0, 1, 2, Qt.AlignLeft)

        '''self.lbl_notes = QLabel('Notes:')
        self.lbl_notes.setFont(QtGui.QFont("Arial", 12, QFont.Bold))
        self.lbl_notes.setAlignment(QtCore.Qt.AlignCenter)
        # self.lbl_pag_title.setFixedWidth(100)
        self.lbl_notes.setFixedHeight(20)
        grid_layout.addWidget(self.lbl_notes, 5, 0, 1, 2, Qt.AlignLeft)'''


        self.txt_pat_info = QTextEdit(self)
        self.txt_pat_info.setReadOnly(False)
        self.txt_pat_info.setFont(QFont('Arial', 12))
        self.txt_pat_info.setText('')
        self.txt_pat_info.setPlaceholderText('Add Notes')
        self.txt_pat_info.setFrameShape(QFrame.WinPanel)
        self.txt_pat_info.setFrameShadow(QFrame.Sunken)
        self.txt_pat_info.setLineWidth(3)
        self.txt_pat_info.setFixedWidth(620)
        self.txt_pat_info.setFixedHeight(300)
        grid_layout.addWidget(self.txt_pat_info, 5, 0, 1, 2, Qt.AlignLeft)

        # BUTTONS===============================================
        self.btn_Submit = QPushButton('Submit')
        self.btn_Submit.setToolTip('Add Medical Notes')
        self.btn_Submit.setStyleSheet('QPushButton {background-color: #FF0000; color: white;}')
        self.btn_Submit.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Submit.setFixedWidth(150)
        self.btn_Submit.setFixedHeight(40)
        self.btn_Submit.clicked.connect(self.btn_submit_clicked)
        grid_layout.addWidget(self.btn_Submit, 6, 0, 1, 2, Qt.AlignCenter)


        # ===============================
        self.empty = QLabel('')
        self.empty.setFixedHeight(70)
        grid_layout.addWidget(self.empty, 7, 0, 1, 2)

        self.lbl_ariston = QLabel('© AristonAQ Ltd, 2020')
        self.lbl_ariston.setFont(QtGui.QFont("Times", 8))
        self.lbl_ariston.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ariston.setFrameShape(QFrame.Panel)
        self.lbl_ariston.setFrameShadow(QFrame.Sunken)
        self.lbl_ariston.setLineWidth(2)  # lbl_user.setFixedWidth(100)
        self.lbl_ariston.setFixedHeight(20)
        grid_layout.addWidget(self.lbl_ariston, 7 + 1, 0, 1, 2)


    def btn_submit_clicked(self):
        path_name = str(self.patient[1]) + "_" + str(self.patient[2]) + ".db"
        look_up_folder = "C:/Users/Georgios/PycharmProjects/Patient_Registration_System/Patient_Medical_Records/" + path_name
        print(look_up_folder)
        try:
            conn = sqlite3.connect(look_up_folder)
            #print(sqlite3.version)
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS pat_med_rec (
                                                medrec_id integer PRIMARY KEY NOT NULL,
                                                pat_id text NOT NULL,
                                                pat_name text NOT NULL,
                                                date text NOT NULL,
                                                notes text NOT NULL
                                        )""")

            patient_id = """INSERT INTO pat_med_rec (pat_id, pat_name, date, notes) VALUES (?, ?, ?, ?) """

            cur.execute(patient_id,
                        (self.patient[0], self.patient[1] + ' ' +self.patient[2], self.date_now, self.txt_pat_info.toPlainText()))
            conn.commit()
            conn.close()
            QMessageBox.information(self, 'Success!', 'Notes have been added.')
        except sqlite3.Error as e:
            print(e)
        finally:
            if conn:
                conn.close()


'''if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Add_Med_Rec()
    ex.show()
    sys.exit(app.exec())'''
