#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


class MatrixGenerator:
    """
    Класс для создания и вывода матрицы указанной размерности
    со случайными элементами в указанном диапазоне.
    """

    def __init__(self):
        """
        Конструктор класса MatrixGenerator,
        инициализирует размерность, диапазон и саму матрицу.
        """
        self.num_columns = 0
        self.num_rows = 0
        self.range_start = 0
        self.range_end = 0
        self.matrix = []

    def read_size(self):
        """
        Метод для ввода размеров матрицы от пользователя.
        """
        try:
            self.num_rows = int(input("Введите число строк: "))
            self.num_columns = int(input("Введите число столбцов: "))
            if self.num_rows <= 0 or self.num_columns <= 0:
                raise ValueError("Размеры матрицы должны быть положительными числами!")
        except ValueError as e:
            print(f"Ошибка: {e}")
            raise

    def read_range(self):
        """
        Метод для ввода диапазона значений матрицы.
        """
        try:
            self.range_start = float(input("Введите начало диапазона: "))
            self.range_end = float(input("Введите конец диапазона: "))

            # Проверяем и округляем до целого, если введены дробные значения
            if self.range_start != int(self.range_start) or self.range_end != int(self.range_end):
                print("Матрица состоит из целых чисел, диапазон будет округлен!")
                self.range_start = round(self.range_start)
                self.range_end = round(self.range_end)

            self.range_start = int(self.range_start)
            self.range_end = int(self.range_end)

            # Меняем местами начало и конец диапазона, если они введены наоборот
            if self.range_start > self.range_end:
                print("Начало диапазона больше конца. Меняем местами.")
                self.range_start, self.range_end = self.range_end, self.range_start

        except ValueError:
            raise ValueError("Неверный ввод диапазона! Диапазон должен быть числом.")
        except Exception:
            raise RuntimeError("Неизвестная ошибка при вводе диапазона.")

    def generate_matrix(self):
        """
        Метод для генерации матрицы заданной размерности и диапазона.
        """
        try:
            # Генерируем строки матрицы
            for i in range(self.num_rows):
                row = []  # Инициализируем новую строку
                for j in range(self.num_columns):
                    # Генерируем случайное число в заданном диапазоне
                    value = random.randint(self.range_start, self.range_end)
                    row.append(value)  # Добавляем значение в строку
                self.matrix.append(row)  # Добавляем строку в матрицу

        except Exception as e:
            print(f"Ошибка при создании матрицы: {e}")
            raise RuntimeError("Не удалось создать матрицу.")

    def display_matrix(self):
        """
        Метод для отображения матрицы.
        """
        for row in self.matrix:
            print(" ".join(map(str, row)))


if __name__ == "__main__":
    try:
        # Создадим объект матрицы
        generator = MatrixGenerator()

        # Введем значения размерности и диапазона
        generator.read_size()
        generator.read_range()

        # После указания атрибутов создадим матрицу
        generator.generate_matrix()

        # Выведем созданную матрицу
        print("Сформированная матрица:")
        generator.display_matrix()

    except Exception as error:
        # Если матрицу создать не удалось
        print(f"Программа завершилась с ошибкой: {error}")
