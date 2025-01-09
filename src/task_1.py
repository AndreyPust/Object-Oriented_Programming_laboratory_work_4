#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Addition:
    """
    Класс предназначенный для сложения двух чисел или конкатенации строк.
    """

    def __init__(self, first=None, second=None):
        """
        Конструктор класса Addition(Сложения).

        :param first: Первое число;
        :param second: Второе число.
        """

        self.first = first
        self.second = second

    def input_values(self):
        """
        Метод для ввода значений с клавиатуры.
        """

        self.first = input("Введите первое значение: ")
        self.second = input("Введите второе значение: ")

    def calculate_sum(self):
        """
        Метод для сложения чисел.
        Сначала пробует преобразовать и сложить 2 числа, а если не получилось,
        выбрасывает исключение с конкатенацией строк.
        """

        try:
            first_num = float(self.first)
            second_num = float(self.second)
            return first_num + second_num
        except ValueError:
            print("Вы ввели строку.")
            return str(self.first) + str(self.second)


if __name__ == "__main__":
    obj = Addition()
    obj.input_values()
    result = obj.calculate_sum()
    print(f"Результат: {result}")
