import pyautogui
import random
import sys
import threading
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QSlider
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QFont

keys = list("abcdefghijklmnopqrstuvwxyz1234567890")
clicking = False
#H1ddenZ0ne
class Overlay(QWidget):
    def __init__(self):
        super().__init__()#H1ddenZ0ne

        self.circle_size = 300
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(600, 300, self.circle_size, self.circle_size)

        self.start_button = QPushButton("Start", self)
        self.start_button.setGeometry(self.circle_size//2 - 40, self.circle_size//2 - 20, 80, 30)
        self.start_button.setStyleSheet("background-color:black; color:white; border:none;")
        self.start_button.clicked.connect(self.start_clicking)

        self.stop_button = QPushButton("Close", self)#H1ddenZ0ne

        self.stop_button.setGeometry(10, 10, 50, 20)
        self.stop_button.setStyleSheet("background-color:red; color:white; border:none;")
        self.stop_button.clicked.connect(self.stop_and_close)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(10, self.circle_size - 30, self.circle_size - 20, 20)
        self.slider.setMinimum(150)
        self.slider.setMaximum(600)
        self.slider.setValue(self.circle_size)
        self.slider.valueChanged.connect(self.resize_circle)

        self.branding = QLabel("H1ddenZ0ne", self)
        self.branding.setFont(QFont("Arial", 9, QFont.StyleItalic))
        self.branding.setStyleSheet("color:white;")
        self.branding.move(self.circle_size - 90, self.circle_size - 45)

        self.offset = None#H1ddenZ0ne
#H1ddenZ0ne
#H1ddenZ0ne


    def resize_circle(self, value):
        self.circle_size = value
        self.setGeometry(self.x(), self.y(), value, value)
        self.start_button.setGeometry(value//2 - 40, value//2 - 20, 80, 30)
        self.slider.setGeometry(10, value - 30, value - 20, 20)
        self.branding.move(value - 90, value - 45)
        self.update()
#H1ddenZ0ne

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(0, 255, 0, 100))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(0, 0, self.circle_size, self.circle_size)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()
#H1ddenZ0ne

    def mouseMoveEvent(self, event):
        if self.offset:
            self.move(self.pos() + event.pos() - self.offset)

    def start_clicking(self):
        global clicking
        if not clicking:
            clicking = True
            thread = threading.Thread(target=self.auto_click)
            thread.start()#H1ddenZ0ne

#H1ddenZ0ne

    def auto_click(self):
        global clicking
        x_min, y_min = self.x(), self.y()
        x_max, y_max = x_min + self.circle_size, y_min + self.circle_size

        print("Started! Move mouse to top-left to stop.")
        try:
            while clicking:
                if pyautogui.position() == (0, 0):
                    print("Stopped.")
                    clicking = False
                    break

                key = random.choice(keys)
                pyautogui.press(key)
                print(f"Key: {key}")

                x = random.randint(x_min, x_max)
                y = random.randint(y_min, y_max)
                pyautogui.moveTo(x, y)

                click_type = random.choice(['left', 'right'])
                pyautogui.click(button=click_type)
                print(f"{click_type.capitalize()} click at ({x}, {y})")

                time.sleep(2)

        except Exception as e:
            print("Error:", e)

    def stop_and_close(self):
        global clicking
        clicking = False
        self.close()

app = QApplication(sys.argv)
overlay = Overlay()
overlay.show()
sys.exit(app.exec_())#H1ddenZ0ne

#H1ddenZ0ne
