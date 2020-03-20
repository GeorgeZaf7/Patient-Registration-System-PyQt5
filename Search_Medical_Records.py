# ----------------------------------------------------------------------------
# File Name:    Search_Medical_Records.py
# Project Name: Patient Registration System
# Author:       Georgios Zafeiropoulos
# Created:      16/03/2020
# Modified:     19/03/2020
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
    QPushButton, QComboBox, QDialog, QTextEdit, QVBoxLayout, QHBoxLayout, QMessageBox
import Show_MedRec_Search_Results


class Search_MedRec(QWidget):
    def __init__(self,pat):  # pat
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

        self.lbl_pag_title = QLabel('Search by dates')
        self.lbl_pag_title.setFont(QtGui.QFont("Arial", 25, QFont.Bold))
        self.lbl_pag_title.setAlignment(QtCore.Qt.AlignCenter)
        # self.lbl_pag_title.setFixedWidth(100)
        self.lbl_pag_title.setFixedHeight(50)
        grid_layout.addWidget(self.lbl_pag_title, 0, 0, 1, 2)

        self.empty = QLabel('')
        self.empty.setFixedHeight(40)
        grid_layout.addWidget(self.empty, 1, 0, 1, 2)
        # ================================
        self.lbl_guide_txt = QLabel('Choose the time frame you want to search:')
        self.lbl_guide_txt.setFont(QtGui.QFont("Arial", 12, QFont.Bold))
        # self.lbl_pag_title.setFixedWidth(100)
        self.lbl_guide_txt.setFixedHeight(50)
        grid_layout.addWidget(self.lbl_guide_txt, 2, 0, 1, 2, Qt.AlignCenter)

        '''self.lbl_month = QLabel('Choose month:')
        self.lbl_month.setFont(QtGui.QFont("Arial", 12, QFont.Bold))
        # self.lbl_pag_title.setFixedWidth(100)
        self.lbl_month.setFixedHeight(50)
        grid_layout.addWidget(self.lbl_month, 3, 0, Qt.AlignRight)

        self.lbl_year = QLabel('Choose year:')
        self.lbl_year.setFont(QtGui.QFont("Arial", 12, QFont.Bold))
        # self.lbl_pag_title.setFixedWidth(100)
        self.lbl_year.setFixedHeight(50)
        grid_layout.addWidget(self.lbl_year, 4, 0, Qt.AlignRight)

        self.txt_month = QComboBox(self)
        self.txt_month.addItems(["01", "02", "03", "04", "05", "06","07", "08", "09", "10", "11", "12"])
        self.txt_month.setFixedWidth(100)
        self.txt_month.setFont(QtGui.QFont("Arial", 12))
        grid_layout.addWidget(self.txt_month, 3, 1, Qt.AlignLeft)

        self.txt_year = QComboBox(self)
        self.txt_year.addItems(["2017", "2018", "2019", "2020", "2021", "2022"])
        self.txt_year.setFixedWidth(100)
        self.txt_year.setFont(QtGui.QFont("Arial", 12))
        grid_layout.addWidget(self.txt_year, 4, 1, Qt.AlignLeft)
        #self.txt_year.currentIndexChanged.connect(self.selectionchange)'''

        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.setStyleSheet('QCalendarWidget {background-color: rgb(90,31,0)}')
        self.calendar.setStyleSheet('QCalendarWidget QWidget {alternate-background-color: rgb(100,100,100)}')
        self.calendar.setMinimumDate(QDate(currentYear - 90, currentMonth, 1))
        self.calendar.setMaximumDate(QDate(currentYear, currentMonth, currentDay))
        self.calendar.clicked[QDate].connect(self.showDate)
        grid_layout.addWidget(self.calendar, 3, 0, 1, 2, Qt.AlignJustify)

        # BUTTONS===============================================
        self.btn_Submit = QPushButton('Submit')
        self.btn_Submit.setToolTip('Add Medical Notes')
        self.btn_Submit.setStyleSheet('QPushButton {background-color: #FF0000; color: white;}')
        self.btn_Submit.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Submit.setFixedWidth(300)
        self.btn_Submit.setFixedHeight(40)
        self.btn_Submit.clicked.connect(self.btn_submit_clicked)
        grid_layout.addWidget(self.btn_Submit, 4, 0, 1, 2, Qt.AlignCenter)

        self.btn_Exit = QPushButton('Exit')
        self.btn_Exit.setToolTip('Go to previous window')
        self.btn_Exit.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Exit.setStyleSheet('QPushButton {color: #FF0000;}')
        self.btn_Exit.setFixedWidth(300)
        self.btn_Exit.setFixedHeight(40)
        self.btn_Exit.clicked.connect(self.close)
        grid_layout.addWidget(self.btn_Exit, 5, 0, 1, 2, Qt.AlignCenter)

        # ===============================
        self.empty = QLabel('')
        self.empty.setFixedHeight(70)
        grid_layout.addWidget(self.empty, 6, 0, 1, 2)

        self.lbl_ariston = QLabel('© AristonAQ Ltd, 2020')
        self.lbl_ariston.setFont(QtGui.QFont("Times", 8))
        self.lbl_ariston.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ariston.setFrameShape(QFrame.Panel)
        self.lbl_ariston.setFrameShadow(QFrame.Sunken)
        self.lbl_ariston.setLineWidth(2)  # lbl_user.setFixedWidth(100)
        self.lbl_ariston.setFixedHeight(20)
        grid_layout.addWidget(self.lbl_ariston, 6 + 1, 0, 1, 2)

    # ===================Functions==============================

    '''def selectionchange(self, i):
        print("Items in the list are :")
        for count in range(self.txt_year.count()):
            print(self.txt_year.itemText(count))
        print("Current index", i, "selection changed ", self.txt_year.currentText())'''

    def showDate(self, date):
        global search_date
        search_date = date.toString('yyyy-MM-dd')

    def btn_submit_clicked(self):
        db_url = self.pat
        try:
            conn = sqlite3.connect(db_url)
                #"C:/Users/Georgios/PycharmProjects/Patient_Registration_System/Patient_Medical_Records/Nick_Smith.db")
            cur = conn.cursor()
            check_date = QDate.currentDate().toString('yyyy-MM-dd')
            if search_date == check_date:
                QMessageBox.warning(self, 'Warning', 'You need to choose an older date')
                return
            else:
                cur.execute('''SELECT * from pat_med_rec WHERE date > ?''', (search_date,))
                columns = cur.fetchall()
                if not columns:
                    QMessageBox.information(self, 'Warning', 'No records for that time period.')
                    return
                else:
                    self.showRes = Show_MedRec_Search_Results.Show_MedRec_Srch_Res(columns)
                    self.showRes.show()
                    #print(len(columns))
        except sqlite3.Error as e:
                QMessageBox.warning(self,'Warning', 'A problem Occured')


        '''desc = cur.description
        print("{0} {1:>10} {2:>15} {3:>15}".format(desc[0][0], desc[1][0], desc[2][0], desc[3][0]))

        for column in columns:
            print("{0:>5} {1:>10} {2:>20} {3:>18}".format(column[0], column[1], column[2], column[3]))'''



        '''for column in cur.execute("SELECT * FROM pat_med_rec").description:
            print(column)'''


        conn.commit()
        conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Search_MedRec()
    ex.show()
    sys.exit(app.exec())
