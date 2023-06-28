#!/usr/bin/env python3
# coding=utf-8

import sys
from random import randint

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


# noinspection DuplicatedCode
class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)

        self.setWindowTitle('Работа с визуальными табличными данными в Python')

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random_numbers(self):
        row = col = 0
        self.label_error.setText('')
        # заполняем таблицу случайными числами
        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                random_num = randint(0, 100)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                self.tableWidget.item(row, col).text()
                col += 1
            row += 1
            col = 0

        # находим максимальное число и его координаты
        # [0] - максимальное число, [1] - строка максимума, [2] - столбец максимума
        list_information_max_num = find_max(self.tableWidget)

        if not list_information_max_num:
            self.label_error.setText('Введены некорректные данные!')
        else:
            # выводим на экран информацию о расположении максимального числа
            self.label_max_el.setText('Максимальный элемент: ' + str(list_information_max_num[0]) + ' [' + str(
                list_information_max_num[1] + 1) + ';' + str(list_information_max_num[2] + 1) + ']')

    def solve(self):
        list_information_max_num = find_max(self.tableWidget)

        if list_information_max_num[1] == self.tableWidget.rowCount() - 1:
            self.label_max_el.setText('Максимальный элемент: ' + str(list_information_max_num[0]) + ' [' + str(
                list_information_max_num[1] + 1) + ';' + str(list_information_max_num[2] + 1) + ']')

            # Увеличиваем все элементы первого столбца в 2 раза
            for row in range(self.tableWidget.rowCount()):
                item = self.tableWidget.item(row, 0)
                if item is not None:
                    number = int(item.text())
                    new_number = number * 2
                    item.setText(str(new_number))

            self.label_error.setStyleSheet('color: blue')
            self.label_error.setText('Условие выполнено!')
        else:
            self.label_error.setStyleSheet('color: red')
            self.label_error.setText('Условие не выполнено!')


def find_max(table_widget):
    row_max_number = col_max_number = row = col = 0
    max_num = int(table_widget.item(row_max_number, col_max_number).text())

    try:
        while row < table_widget.rowCount():
            while col < table_widget.columnCount():
                number = int(table_widget.item(row, col).text())
                if number > max_num:
                    max_num = number
                    row_max_number = row
                    col_max_number = col
                col += 1
            row += 1
            col = 0
        return [max_num, row_max_number, col_max_number]
    except Exception:
        return None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
