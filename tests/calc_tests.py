import pytest
from app.Calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_is_correct(self):
        assert self.calc.multiply(self, 3, 3) == 9

    def test_division_is_correct(self):
        assert self.calc.division(self, 20, 5) == 4

    def test_subtraction_is_correct(self):
        assert self.calc.subtraction(self, 10, 6) == 4

    def test_adding_is_correct(self):
        assert self.calc.adding(self, 13, 5) == 18

