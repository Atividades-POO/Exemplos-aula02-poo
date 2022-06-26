#

# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 26/06/2022
#

# 1 - importar a classe vazia e crie um alias para ela
from classevazia import ClasseVazia as CV
# 1.1 crie uma instância da classe vazia
cv1 = CV()

# 2  importar a classe pessoa e crie um alias para ela
from pessoa import Pessoa as P
# 2.1 crie uma instância da classe pessoa
p1 = P()
p2 = P()
p3 = P()
print(p1, p2, p3) # vai imprimir tres objetos da classe pessoa, com respectivos endereços de memória
# imprima o nome da pessoa 1
print(p1.nome)
# imprima o nome da pessoa 2
print(p2.nome)
# imprima o nome da pessoa 3
print(p3.nome)

# altere o nome da pessoa 1
p1.nome = "João" # altera o nome da pessoa 1
# altere o nome da pessoa 2
p2.nome = "Maria" # altera o nome da pessoa 2
# altere o nome da pessoa 3
p3.nome = "Pedro" # altera o nome da pessoa 3

# imprima o nome da pessoa 1
print(p1.nome) # vai imprimir "João"
# imprima o nome da pessoa 2
print(p2.nome) # vai imprimir "Maria"
# imprima o nome da pessoa 3
print(p3.nome) # vai imprimir "Pedro"

# chame o método olaMundo da pessoa 1
p1.olaMundo() # vai imprimir "Olá Mundo do POO! sou o João"
# chame o método olaMundo da pessoa 2
p2.olaMundo() # vai imprimir "Olá Mundo do POO! sou o Maria"
# chame o método olaMundo da pessoa 3
p3.olaMundo() # vai imprimir "Olá Mundo do POO! sou o Pedro"


# 3 - impportar a classe numero e crie um alias para ela
from numero import Numero as N
# 3.1 crie uma instância da classe numero
n1 = N(10, 20) # cria um objeto da classe numero com valores 10 e 20
# chame o método imprime da instância criada
n1.imprime() # vai imprimir "valor1 = 10, valor2 = 20"
# fazer a soma dos dois números
print(f"a soma = {n1.num1 + n1.num2}") # vai imprimir "a soma = 30"

# 4 - importar a classe DepartamentoPessoal do ex02 e crie um alias para ela
from ex02 import DepartamentoPessoal as DP
# 4.1 crie uma instância da classe DepartamentoPessoal
dp1 = DP('david', 'vendedor', '123456789', 1000)
#  chame o método imprime da instância criada
dp1.imprime() # vai imprimir "nome = david, cargo = vendedor, cpf = 123456789, salário = 1000"
#  altere o nome da pessoa
dp1.nome = "joão" # altera o nome da pessoa
#  chame o método imprime da instância criada
dp1.imprime() # vai imprimir "nome = joão, cargo = vendedor, cpf = 123456789, salário = 1000"

