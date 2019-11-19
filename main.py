import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 325)
        self.setWindowTitle('Git и случайные окружности')

        self.btn = QPushButton('Кнопка', self)
        self.btn.resize(50, 20)
        self.btn.move(25, 10)

        self.label = QLabel(self)
        self.label.move(25, 50)
        self.btn.clicked.connect(self.circle)
        canvas = QPixmap(250, 250)
        self.label.setPixmap(canvas)

    def circle(self):
        x, y = randint(0, 250), randint(0, 250)
        s = randint(10, 50)
        painter = QPainter(self.label.pixmap())
        painter.brush
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        painter.setPen(pen)
        painter.drawEllipse(x, y - s, s, s)
        painter.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())