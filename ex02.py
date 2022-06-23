#
# Crie uma classe para o
# departamento pessoal.
class DepartamentoPessoal:
  
  def __init__(self, nome, cargos, CPF, salario):
    self.nome = nome
    self.cargos = cargos
    self.CPF = CPF
    self.salario = salario

  def imprime(self):
    print(f"Nome: {self.nome}")
    print(f"Cargos: {self.cargos}")
    print(f"CPF: {self.CPF}")
    print(f"Salário: {self.salario}")
