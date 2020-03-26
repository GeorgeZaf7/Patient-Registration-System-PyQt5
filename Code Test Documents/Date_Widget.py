import sys
from datetime import datetime
import calendar
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget
from PyQt5.QtCore import QDate


class CalendarDemo(QWidget):
    global currentYear, currentMonth, currentDay

    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    currentYear = datetime.now().year

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calendar Demo')
        self.setGeometry(300,300,450,450)
        self.initUI()

    def initUI(self):
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(False)
        self.calendar.setMinimumDate(QDate(currentYear - 90, currentMonth, 1))
        self.calendar.setMaximumDate(QDate(currentYear, currentMonth, currentDay))
        self.calendar.clicked[QDate].connect(self.showDate)

    def showDate(self, date):
        new = date.toString('dd-MM-yyyy')
        print(new)

def main():
    app = QApplication(sys.argv)
    demo = CalendarDemo()
    demo.show()
    sys.exit(app.exec())

main()

