# ----------------------------------------------------------------------------
# File Name:    Show_MedRec_Search_Results.py
# Project Name: Patient Registration System
# Author:       Georgios Zafeiropoulos
# Created:      23/03/2020
# Modified:     23/03/2020
# Copyright:    (c) Georgios Zafeiropoulos, 2020
# License:      CC-BY
# ----------------------------------------------------------------------------
import sys

from PyQt5 import QtCore, Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import (QDialog, QPushButton, QVBoxLayout, QTextEdit, QFrame, QDesktopWidget)


class PrintMedRec(QDialog):
    def __init__(self, a):
        super().__init__()
        self.texts = a
        self.textbox = QTextEdit('Your name')
        self.textbox.setReadOnly(True)
        self.textbox.setFont(QFont('Arial', 12, QFont.Bold))
        self.textbox.setText(self.texts)
        self.textbox.setFrameShape(QFrame.Panel)
        self.textbox.setFrameShadow(QFrame.Sunken)
        self.textbox.setLineWidth(2)

        self.btn_Close = QPushButton('Close')
        self.btn_Close.setToolTip('Close Window')
        self.btn_Close.setStyleSheet('QPushButton {background-color: #FF0000; color: white;}')
        self.btn_Close.setFont(QFont('Arial', 14, QFont.Bold))
        self.btn_Close.setFixedWidth(300)
        self.btn_Close.setFixedHeight(40)
        self.btn_Close.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.textbox)
        layout.addWidget(self.btn_Close, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(layout)
        self.setWindowTitle('Notes')
        self.setWindowIcon(QIcon('Resized_logo.png'))
        self.left = 0
        self.top = 0
        self.width = 640
        self.height = 480
        self.setGeometry(self.left, self.top, self.width, self.height)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def btn_close_clicked(self):
        self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            if self.btn_Close.hasFocus():
                self.btn_close_clicked()
