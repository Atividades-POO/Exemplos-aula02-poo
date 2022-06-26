# 
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 26/06/2022
#
# Recrie a classe pessoa do ex2 que
# tenha o método de inicialização.
class Pessoa:
  def __init__(self, nome): # inicializador
    self.nome = nome # atributo
  def olaMundo(self): # método de instância
    print(f"Olá Mundo do POO! sou o {self.nome}")