#
# 3 - crie uma classe numero que tenha um
# método construtor (inicializador) que receba dois
# números, crie uma instancia.
class Numero:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def imprime(self):
        print(f"valor1 = {self.num1}, valor2 = {self.num2}")   # imprime os dois números