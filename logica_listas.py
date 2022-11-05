# BASICO DE LOGICA DE PROGRAMAÇÃO (EXEMPLOS EM PYTHON)#
# ------------------------------------------------------------#
## ---Listas--- ##

# >>EXEMPLO 1<< #
# nomes

nomes = ['levi', 'eren', 'mikasa', 'reiner']
# nome representa cada item de nomes e mostra na tela cada um deles
for nome in nomes:
    print(nome)

# >>EXEMPLO 2<< #
# index

preco_1 = 20
preco_2 = 50
preco_3 = 200
# cria lista com os
precos = [20, 50, 200]
# utiliza-se o index para saber o indice de contagem
# 20, no index, seria 0 // 50, no index, seria 1// assim por diante
# colocando a posição no index dentro de [] em um print,
# mostra na tela o valor da posição especificada
print(precos[0])
print(precos.index(200))

# >>EXEMPLO 3<< #
# imprimir de maneira não individual, utilizando laço de repetição
# em iteráveis

for preco in precos:
    print(preco)

# >>EXEMPLO 4<< #
# imprimir a soma de idades

idades = [14, 18, 21, 44, 48]
total = 0
for idade in idades:
    total = total + idade
print(total)
