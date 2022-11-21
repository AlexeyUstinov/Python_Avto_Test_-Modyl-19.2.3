import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiplay_calculate_correctly(self): # Умножаем, позитивный тест
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculate_correctly(self): # Деление, позитивный тест
        assert self.calc.division(self, 6, 2) == 3

    def test_subtraction_calculate_correctly(self): # Вычитание, позитивный тест
        assert self.calc.subtraction(self, 4, 2) == 2

    def test_adding_calculate_correctly(selfs): # Сложение, позитивный тест
        assert selfs.calc.adding(self, 2, 2) == 4


    def test_multiply_calcalation_failed(self):
        assert self.clc.maltiply(self, 2, 2) == 5 # Умножение, нигативный тест

    def test_division_calculate_correctly(self):  # Деление, нигативный тест
        assert self.calc.division(self, 6, 2) == 5

    def test_subtraction_calculate_correctly(self):  # Вычитание, нигативный тест
        assert self.calc.subtraction(self, 4, 2) == 1

    def test_adding_calculate_correctly(selfs):  # Сложение, нигативный тест
        assert selfs.calc.adding(self, 2, 2) == 5


