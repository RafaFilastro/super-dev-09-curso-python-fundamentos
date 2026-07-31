from abc import ABC, abstractmethod
from math import pi


class FormaPagamento(ABC):

    @abstractmethod
    def pagar(self):
        pass

class Pix(FormaPagamento):
    def pagar(self):
        print("Pagamento realizado por Pix.")

class Cartao(FormaPagamento):
    def pagar(self):
        print("Pagamento realizado com cartão.")


pix = Pix()
cartao = Cartao()

pix.pagar()
cartao.pagar()

#Abstração é um conceito da programação orientada a objetos usado para criar uma classe-modelo que define regras para outras #classes.
#
#No Python, usamos ABC para criar uma classe abstrata e @abstractmethod para indicar métodos que devem ser obrigatoriamente #implementados pelas classes filhas.
#
#A classe abstrata serve como base e normalmente não é utilizada para criar objetos diretamente.

# (....) herança
class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self) -> float:
        """
        Toda forma geométrica deverá implementar
        uma função para calcular sua área
        """
        pass


class Circulo(FormaGeometrica):
    def __init__(self, raio: float):
        self.raio = raio

    def calcular_area(self) -> float:
        area = pi * self.raio ** 2
        return area


class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado * self.lado

circulo = Circulo(5)
print("Área do círculo: ", circulo.calcular_area())

quadrado = Quadrado(4)
print("Área do quadrado: ", quadrado.calcular_area())

