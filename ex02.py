
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 26/06/2022
#
#
# Crie uma classe para o
# departamento pessoal.
class DepartamentoPessoal:

  def __init__(self, nome, cargo, CPF, salario): # inicializador
    self.nome = nome # atributo
    self.cargos = cargo
    self.CPF = CPF
    self.salario = salario

  def imprime(self): # método de instância
    print(f"Nome: {self.nome}") 
    print(f"Cargos: {self.cargos}")
    print(f"CPF: {self.CPF}")
    print(f"Salário: {self.salario}") 
