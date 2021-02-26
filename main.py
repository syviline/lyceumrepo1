import sys
import random

import PyQt5
from PyQt5.QtGui import QPainter, QColor
from PyQt5.Qt import QPoint
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QMainWindow
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.circles = []
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        if self.do_paint:
            qp.setBrush(QColor(255, 255, 0))
            qp.setPen(PyQt5.QtCore.Qt.NoPen)
            radius = random.randint(10, 100)
            self.circles.append([QPoint(random.randint(radius, self.width() - radius), random.randint(radius, self.height() - radius)), radius, radius])
            for i in self.circles:
                qp.drawEllipse(*i)
            self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())