from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QLabel, QVBoxLayout, QLineEdit)
import random

answers = ['Да', 'Нет', 'Скорее всего да', 'Скорее всего нет', 'Возможно', 'Имеются перспективы',
           'Вопрос задан неверно']


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.button = QPushButton('Спроси меня о чем-то и нажми на кнопку!', self)
        self.label = QLabel(self)
        self.button.clicked.connect(self.handleButton)
        self.textbox = QLineEdit(self)
        self.textbox.move(167, 2)
        self.textbox.size()

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

    def handleButton(self):
        self.label.setText(random.choice(answers))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
