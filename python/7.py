import math
import pytest


class bhaskara:
    def delta(self, a, b, c):
        return (b ** 2) - (4 * a * c)
    
    def obter_coeficientes(self):
        a_digitado = float(input("Digite o valor de a: "))
        b_digitado = float(input("Digite o valor de b: "))
        c_digitado = float(input("Digite o valor de c: "))
        print(self.calcular_raizes(a_digitado, b_digitado, c_digitado))
    def calcular_raizes(self, a, b, c):
        d = self.delta(a, b, c)
        if d == 0:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            return (1, raiz1)
        elif d > 0:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            raiz2 = (-b - math.sqrt(d)) / (2 * a)
            return (2, raiz1, raiz2)
        else:
            return (0,)


class TestBhaskara:
    @pytest.fixture
    def b(self):
        return bhaskara()
    

    def test_delta(self):
        assert self.b.delta(1, -3, 2) == 1
        assert self.b.delta(1, -2, 1) == 0
        assert self.b.delta(1, 0, -4) == 16

    def test_calcular_raizes(self):
        assert self.b.calcular_raizes(1, -3, 2) == (2, 2.0, 1.0)
        assert self.b.calcular_raizes(1, -2, 1) == (1, 1.0)
        assert self.b.calcular_raizes(1, 0, -4) == (2, 2.0, -2.0)