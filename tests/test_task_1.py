#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from src.task_1 import Addition


class TestAddition(unittest.TestCase):

    def test_calculate_sum_with_integers(self):
        """
        Тест когда два целых числа.
        """

        obj = Addition("5", "10")
        result = obj.calculate_sum()
        self.assertEqual(result, 15)

    def test_calculate_sum_with_floats(self):
        """
        Тест когда два вещественных числа.
        """

        obj = Addition("2.5", "3.5")
        result = obj.calculate_sum()
        self.assertEqual(result, 6.0)

    def test_calculate_sum_with_invalid_numbers(self):
        """
        Тест когда одно из значений - строка.
        """

        obj = Addition("abc", "3")
        result = obj.calculate_sum()
        self.assertEqual(result, "abc3")

    def test_calculate_sum_with_strings(self):
        """
        Тест, когда оба значения - это строки.
        """

        obj = Addition("hello", "world")
        result = obj.calculate_sum()
        self.assertEqual(result, "helloworld")

    def test_calculate_sum_with_mixed_values(self):
        """
        Тест, когда второе значение - это строка.
        """

        obj = Addition("10", "world")
        result = obj.calculate_sum()
        self.assertEqual(result, "10world")


if __name__ == "__main__":
    unittest.main()
