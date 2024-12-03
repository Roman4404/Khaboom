import sys
import io
import os
from random import randint
from math import cos, pi, sin

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtWidgets import QApplication, QMainWindow

SCREEN_SIZE = [500, 500]
# Задаём длину стороны и количество углов
SIDES_COUNT = 100

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>500</width>
    <height>500</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton_paint">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>450</y>
      <width>93</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Нарисовать</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

class DrawStar(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.setGeometry(300, 300, *SCREEN_SIZE)
        self.setWindowTitle('Рисуем звезду')
        self.do_paint = False
        self.pushButton_paint.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            self.SIDE_LENGTH = randint(10, 250)
            qp = QPainter()
            qp.begin(self)
            self.draw_star(qp)
            qp.end()

        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()


    def xs(self, x):
        return x + SCREEN_SIZE[0] // 2

    def ys(self, y):
        return SCREEN_SIZE[1] // 2 - y

    def draw_star(self, qp):

        # Считаем координаты и переводим их в экранные
        nodes = [(self.SIDE_LENGTH * cos(i * 2 * pi / SIDES_COUNT),
                  self.SIDE_LENGTH * sin(i * 2 * pi / SIDES_COUNT))
                 for i in range(SIDES_COUNT)]
        nodes2 = [(int(self.xs(node[0])),
                   int(self.ys(node[1]))) for node in nodes]

        pen = QPen(QColor(255, randint(0, 255), randint(0, 255)), 2)
        qp.setPen(pen)
        # Рисуем пятиугольник
        for i in range(-1, len(nodes2) - 1):
            qp.drawLine(*nodes2[i], *nodes2[i + 1])

        # Изменяем цвет линии
        pen = QPen(Qt.GlobalColor.red, 2)
        qp.setPen(pen)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawStar()
    ex.show()
    sys.exit(app.exec())