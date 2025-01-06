import io
import sys
import sqlite3

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

design1 = '''<?xml version="1.0" encoding="UTF-8"?>
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
  <property name="minimumSize">
   <size>
    <width>500</width>
    <height>500</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>500</width>
    <height>500</height>
   </size>
  </property>
  <property name="font">
   <font>
    <pointsize>12</pointsize>
   </font>
  </property>
  <property name="windowTitle">
   <string>Каталог библиотеки</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QComboBox" name="comboBox">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>30</y>
      <width>191</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>90</y>
      <width>191</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="btn">
    <property name="geometry">
     <rect>
      <x>280</x>
      <y>30</y>
      <width>151</width>
      <height>91</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>18</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Искать</string>
    </property>
   </widget>
   <widget class="QTableWidget" name="table">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>140</y>
      <width>501</width>
      <height>361</height>
     </rect>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

design2 = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>300</width>
    <height>400</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>300</width>
    <height>400</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>300</width>
    <height>400</height>
   </size>
  </property>
  <property name="font">
   <font>
    <pointsize>12</pointsize>
   </font>
  </property>
  <property name="windowTitle">
   <string>Информация о произведении</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>0</y>
      <width>100</width>
      <height>100</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>110</y>
      <width>301</width>
      <height>20</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Название</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="title">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>130</y>
      <width>291</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>170</y>
      <width>251</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Автор</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignHCenter|Qt::AlignTop</set>
    </property>
   </widget>
   <widget class="QLabel" name="author">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>200</y>
      <width>221</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_6">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>245</y>
      <width>211</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Год выпуска</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="year">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>270</y>
      <width>221</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_8">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>290</y>
      <width>201</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Жанр</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="genre">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>330</y>
      <width>191</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class MyWidget1(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(design1)
        uic.loadUi(f, self)  # Загружаем дизайн

        self.comboBox.addItem('Название')
        self.comboBox.addItem('Автор')

        # Подключение к БД
        con = sqlite3.connect('database.sqlite')

        # Создание курсора
        cur = con.cursor()

        # Выполнение запроса и получение всех результатов
        self.data = cur.execute("""SELECT Works.title, Authors.name, Works.year, Genres.name FROM Works
                    JOIN Authors ON Works.author_id = Authors.id 
                    JOIN Genres ON Works.genre_id = Genres.id""").fetchall()

        con.close()

        self.btn.clicked.connect(self.act)

    def act(self):
        if self.comboBox.currentText() == 'Название':
            A = [i for i in self.data if self.lineEdit.text().lower() in i[0].lower()]
        else:
            A = [i for i in self.data if self.lineEdit.text().lower() in i[1].lower()]

        self.table.setColumnCount(1)  # Установите количество столбцов
        self.table.setRowCount(len(A))

        self.table.horizontalHeader().setVisible(False)
        self.table.verticalHeader().setVisible(False)

        # Устанавливаем ширину столбца
        self.table.setColumnWidth(0, 500)  # Устанавливаем ширину столбца в 400 пикселей

        # Заполняем таблицу элементами
        for i in range(len(A)):
            btn = QPushButton(A[i][0])
            btn.clicked.connect(lambda checked: self.act1())

            self.table.setCellWidget(i, 0, btn)

    def act1(self):
        el = [i for i in self.data if i[0] == self.sender().text()]
        self.widget = MyWidget2(el[0][0], el[0][1], el[0][2], el[0][3])
        self.widget.show()


class MyWidget2(QMainWindow):
    def __init__(self, title, author, year, genre):
        super().__init__()
        f = io.StringIO(design2)
        uic.loadUi(f, self)  # Загружаем дизайн

        self.title.setText(title)
        self.author.setText(author)
        self.year.setText(year)
        self.genre.setText(genre)

        if title == 'Сказка о золотом петушке':
            self.pixmap = QPixmap('1.jpg')
        elif title == 'Руслан и Людмила':
            self.pixmap = QPixmap('2.jpg')
        elif title == 'Ревизор':
            self.pixmap = QPixmap('3.jpg')
        elif title == 'Тарас Бульба':
            self.pixmap = QPixmap('4.jpg')
        self.label.setPixmap(self.pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget1()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

