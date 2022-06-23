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
