from unittest import TestCase
from PracticaScrum import *


class TestSumar(TestCase):
    def test_sumar(self):
        resultado = sumar("1,2")
        self.assertEqual(resultado,3)
