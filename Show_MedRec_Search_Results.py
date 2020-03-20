# ----------------------------------------------------------------------------
# File Name:    Show_MedRec_Search_Results.py
# Project Name: Patient Registration System
# Author:       Georgios Zafeiropoulos
# Created:      20/03/2020
# Modified:     20/03/2020
# Copyright:    (c) Georgios Zafeiropoulos, 2020
# License:      CC-BY
# ----------------------------------------------------------------------------
import sqlite3
import time
from datetime import datetime
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QLinearGradient, QBrush, QColor, QPalette, QFont, QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QDesktopWidget, QLabel, QFrame, QApplication, QCalendarWidget, \
    QPushButton, QComboBox, QDialog, QTextEdit, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem, \
    QTableView


class Show_MedRec_Srch_Res(QWidget):
    def __init__(self, pat):  # pat
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

        self.patient = pat
        self.initUI(self.patient)  # self.patient

    def initUI(self,a):  # a
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

        self.lbl_pag_title = QLabel('Medical Records Search Results')
        self.lbl_pag_title.setFont(QtGui.QFont("Arial", 25, QFont.Bold))
        self.lbl_pag_title.setAlignment(QtCore.Qt.AlignCenter)
        # self.lbl_pag_title.setFixedWidth(100)
        self.lbl_pag_title.setFixedHeight(50)
        grid_layout.addWidget(self.lbl_pag_title, 0, 0, 1, 2)

        self.empty = QLabel('')
        self.empty.setFixedHeight(40)
        grid_layout.addWidget(self.empty, 1, 0, 1, 2)
        # ================================

        self.myTableWidget = QTableWidget()
        self.myTableWidget.setRowCount(len(self.pat))  ##set number of rows
        self.myTableWidget.setColumnCount(4)  ##this is fixed for myTableWidget, ensure that both of your tables, sql and qtablewidged have the same number of columns

        #row = 0
        header_data = 'Patient ID', 'Patient Details', 'Note Date', 'Note'
        self.myTableWidget.setHorizontalHeaderLabels(header_data)
        self.myTableWidget.setFont(QtGui.QFont("Arial", 12, QFont.Bold))
        for row in range(0, len(self.pat)):
            for col in range(0, 4):
                self.myTableWidget.setItem(row, col, QTableWidgetItem(self.pat[row][col+1]))
        self.myTableWidget.setSortingEnabled(True)
        self.myTableWidget.sortByColumn(3, Qt.AscendingOrder)
        grid_layout.addWidget(self.myTableWidget, 2, 0, 1, 2)


        # ===============================
        self.empty = QLabel('')
        self.empty.setFixedHeight(70)
        grid_layout.addWidget(self.empty, 3, 0, 1, 2)

        self.lbl_ariston = QLabel('© AristonAQ Ltd, 2020')
        self.lbl_ariston.setFont(QtGui.QFont("Times", 8))
        self.lbl_ariston.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ariston.setFrameShape(QFrame.Panel)
        self.lbl_ariston.setFrameShadow(QFrame.Sunken)
        self.lbl_ariston.setLineWidth(2)  # lbl_user.setFixedWidth(100)
        self.lbl_ariston.setFixedHeight(20)
        grid_layout.addWidget(self.lbl_ariston, 3 + 1, 0, 1, 2)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Show_MedRec_Srch_Res()
    ex.show()
    sys.exit(app.exec())
