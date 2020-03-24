# ----------------------------------------------------------------------------
# File Name:    Show_MedRec_Search_Results.py
# Project Name: Patient Registration System
# Author:       Georgios Zafeiropoulos
# Created:      20/03/2020
# Modified:     20/03/2020
# Copyright:    (c) Georgios Zafeiropoulos, 2020
# License:      CC-BY
# Comments:     N/A
# ----------------------------------------------------------------------------

import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QLinearGradient, QBrush, QColor, QPalette, QFont, QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QDesktopWidget, QLabel, QFrame, QPushButton, QTableWidget, \
    QTableWidgetItem
import Print_Selected_MedRec_Result


class Show_MedRec_Srch_Res(QWidget):
    def __init__(self, pat):  # pat
        super().__init__()
        self.title = "Patient Registration System"
        self.left = 0
        self.top = 0
        self.width = 640
        self.height = 480
        self.patient = pat
        self.initUI(self.patient)  # self.patient

    def initUI(self, a):  # a
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.setWindowIcon(QIcon('Resized_logo.png'))

        p = QPalette()
        gradient = QLinearGradient(0, 50, 0, 300)
        gradient.setColorAt(1.0, QColor(204, 240, 240))  # 204, 240, 240
        gradient.setColorAt(0.0, QColor(233, 112, 112))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)  #

        self.pat = a  # read data from previous window

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

        self.myTableWidget = QTableWidget(self)
        self.myTableWidget.setRowCount(len(self.pat))  # set number of rows
        self.myTableWidget.setColumnCount(5)
        # row = 0
        header_data = 'Patient ID', 'Patient Details', 'Note Date', 'Note' , 'Added By'
        self.myTableWidget.setHorizontalHeaderLabels(header_data)
        self.myTableWidget.setFont(QtGui.QFont("Arial", 12, QFont.Bold))
        for row in range(0, len(self.pat)):
            for col in range(0, 5):
                if col < 3:
                    self.items = QTableWidgetItem(self.pat[row][col + 1])
                    self.items.setTextAlignment(Qt.AlignHCenter)
                    self.myTableWidget.setItem(row, col, self.items)
                else:
                    self.items = QTableWidgetItem(self.pat[row][col + 1])
                    self.myTableWidget.setItem(row, col, self.items)
        header = self.myTableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.myTableWidget.setFrameShape(QFrame.Panel)
        self.myTableWidget.setFrameShadow(QFrame.Sunken)
        self.myTableWidget.setLineWidth(2)
        self.myTableWidget.setSortingEnabled(True)
        self.myTableWidget.sortByColumn(2, Qt.AscendingOrder)
        self.myTableWidget.cellDoubleClicked.connect(self.print_text)
        grid_layout.addWidget(self.myTableWidget, 2, 0, 1, 2)

        self.btn_Exit = QPushButton('Back')
        self.btn_Exit.setToolTip('Close Application')
        self.btn_Exit.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Exit.setStyleSheet('QPushButton {background-color: #FF0000; color: white;}')
        self.btn_Exit.setFixedWidth(400)
        self.btn_Exit.setFixedHeight(40)
        self.btn_Exit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_Exit.clicked.connect(self.btn_exit_clicked)
        grid_layout.addWidget(self.btn_Exit, 3, 0, 1, 2, Qt.AlignCenter)
        # ===============================
        self.empty = QLabel('')
        self.empty.setFixedHeight(70)
        grid_layout.addWidget(self.empty, 4, 0, 1, 2)

        self.lbl_ariston = QLabel('© AristonAQ Ltd, 2020')
        self.lbl_ariston.setFont(QtGui.QFont("Arial", 9, QFont.Bold))
        self.lbl_ariston.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ariston.setFrameShape(QFrame.Panel)
        self.lbl_ariston.setFrameShadow(QFrame.Sunken)
        self.lbl_ariston.setLineWidth(2)  # lbl_user.setFixedWidth(100)
        self.lbl_ariston.setFixedHeight(20)
        grid_layout.addWidget(self.lbl_ariston, 4 + 1, 0, 1, 2)

    def print_text(self, row, column):
        item = self.myTableWidget.item(row, column)
        # print(item.text())
        self.alpha = Print_Selected_MedRec_Result.PrintMedRec(item.text())
        self.alpha.show()

    def btn_exit_clicked(self):
        self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            if self.btn_Exit.hasFocus():
                self.btn_exit_clicked()


'''if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Show_MedRec_Srch_Res()
    ex.show()
    sys.exit(app.exec())'''
