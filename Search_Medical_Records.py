# ----------------------------------------------------------------------------
# File Name:    Search_Medical_Records.py
# Project Name: Patient Registration System
# Author:       Georgios Zafeiropoulos
# Created:      16/03/2020
# Modified:     16/03/2020
# Copyright:    (c) Georgios Zafeiropoulos, 2020
# License:      CC-BY
# ----------------------------------------------------------------------------
from datetime import datetime
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QLinearGradient, QBrush, QColor, QPalette, QFont, QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QDesktopWidget, QLabel, QFrame, QApplication, QCalendarWidget


class Search_MedRec(QWidget):
    def __init__(self): #pat
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

        #self.patient = pat
        self.initUI() #self.patient

    def initUI(self): #a
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

        #self.pat = a

        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        self.lbl_pag_title = QLabel('Search by dates')
        self.lbl_pag_title.setFont(QtGui.QFont("Arial", 25, QFont.Bold))
        self.lbl_pag_title.setAlignment(QtCore.Qt.AlignCenter)
        # self.lbl_pag_title.setFixedWidth(100)
        self.lbl_pag_title.setFixedHeight(50)
        grid_layout.addWidget(self.lbl_pag_title, 0, 0, 1, 2)

        self.empty = QLabel('')
        self.empty.setFixedHeight(40)
        grid_layout.addWidget(self.empty, 1, 0, 1, 2)
        #================================
        self.lbl_guide_txt = QLabel('Choose the date after which you want to search:')
        self.lbl_guide_txt.setFont(QtGui.QFont("Arial", 12, QFont.Bold))
        # self.lbl_pag_title.setFixedWidth(100)
        self.lbl_guide_txt.setFixedHeight(50)
        grid_layout.addWidget(self.lbl_guide_txt, 2, 0, 1, 2, Qt.AlignCenter)

        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.setStyleSheet('QCalendarWidget {background-color: rgb(90,31,0)}')
        self.calendar.setStyleSheet('QCalendarWidget QWidget {alternate-background-color: rgb(100,100,100)}')
        self.calendar.setMinimumDate(QDate(currentYear - 90, currentMonth, 1))
        self.calendar.setMaximumDate(QDate(currentYear, currentMonth, currentDay))
        self.calendar.clicked[QDate].connect(self.showDate)
        grid_layout.addWidget(self.calendar, 3, 0, 1, 2, Qt.AlignJustify)


        # ===============================
        self.empty = QLabel('')
        self.empty.setFixedHeight(70)
        grid_layout.addWidget(self.empty, 4, 0, 1, 2)

        self.lbl_ariston = QLabel('© AristonAQ Ltd, 2020')
        self.lbl_ariston.setFont(QtGui.QFont("Times", 8))
        self.lbl_ariston.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ariston.setFrameShape(QFrame.Panel)
        self.lbl_ariston.setFrameShadow(QFrame.Sunken)
        self.lbl_ariston.setLineWidth(2)  # lbl_user.setFixedWidth(100)
        self.lbl_ariston.setFixedHeight(20)
        grid_layout.addWidget(self.lbl_ariston, 5 + 1, 0, 1, 2)

    # ===================Functions==============================

    def showDate(self, date):
        global search_date
        search_date = date.toString('dd-MM-yyyy')
        #print(search_date)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Search_MedRec()
    ex.show()
    sys.exit(app.exec())
