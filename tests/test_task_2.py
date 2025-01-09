#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch

from src.task_2 import MatrixGenerator


class TestMatrixGenerator(unittest.TestCase):
    def setUp(self):
        """Инициализация объекта перед каждым тестом."""
        self.generator = MatrixGenerator()

    def test_read_size_correct_input(self):
        """Тест корректного ввода размеров матрицы."""
        with patch("builtins.input", side_effect=["3", "4"]):
            self.generator.read_size()
            self.assertEqual(self.generator.num_rows, 3)
            self.assertEqual(self.generator.num_columns, 4)

    def test_read_size_invalid_input(self):
        """Тест на некорректный ввод размеров матрицы."""
        with patch("builtins.input", side_effect=["-2", "5"]):
            with self.assertRaises(ValueError) as cm:
                self.generator.read_size()
            self.assertEqual(str(cm.exception), "Размеры матрицы должны быть положительными числами!")

    def test_read_range_correct_input(self):
        """Тест корректного ввода диапазона."""
        with patch("builtins.input", side_effect=["3.5", "7.9"]):
            self.generator.read_range()
            self.assertEqual(self.generator.range_start, 4)  # Округление вверх
            self.assertEqual(self.generator.range_end, 8)  # Округление вверх

    def test_read_range_reversed_input(self):
        """Тест диапазона, где начало больше конца."""
        with patch("builtins.input", side_effect=["10", "5"]):
            self.generator.read_range()
            self.assertEqual(self.generator.range_start, 5)
            self.assertEqual(self.generator.range_end, 10)

    def test_read_range_invalid_input(self):
        """Тест на некорректный ввод диапазона."""
        with patch("builtins.input", side_effect=["abc", "7"]):
            with self.assertRaises(ValueError) as cm:
                self.generator.read_range()
            self.assertEqual(str(cm.exception), "Неверный ввод диапазона! Диапазон должен быть числом.")

    def test_generate_matrix(self):
        """Тест генерации матрицы."""
        self.generator.num_rows = 3
        self.generator.num_columns = 3
        self.generator.range_start = 1
        self.generator.range_end = 5
        self.generator.generate_matrix()
        self.assertEqual(len(self.generator.matrix), 3)
        self.assertTrue(all(len(row) == 3 for row in self.generator.matrix))
        self.assertTrue(
            all(
                self.generator.range_start <= value <= self.generator.range_end
                for row in self.generator.matrix
                for value in row
            )
        )

    def test_display_matrix(self):
        """Тест отображения матрицы."""
        self.generator.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        with patch("builtins.print") as mock_print:
            self.generator.display_matrix()
            mock_print.assert_any_call("1 2 3")
            mock_print.assert_any_call("4 5 6")
            mock_print.assert_any_call("7 8 9")


if __name__ == "__main__":
    unittest.main()
