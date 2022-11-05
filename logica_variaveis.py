# BASICO DE LOGICA DE PROGRAMAÇÃO (EXEMPLOS EM PYTHON)#
# ------------------------------------------------------------------------------#
## ---Variaveis--- ##
# NUMEROS
id_funcionario = 1
print(id_funcionario)

# VALORES BOOLEANOS
# (>>EM PYTHON<< True e False devem ter a primeira letra maiuscula)
funcionario_presenca = True

# STRINGS
nome_do_curso = "Lógica de Programação"

# >>CALCULAR VALOR/HORA DE UM FUNCIONARIO COM BASE NO SEU SALARIO MENSAL<<#

# string para introduzir dado salario
salario_mensal = input('Qual o seu salario mmensal? ')
# string para introduzir dado horas trabalhadas
horas_trabalhadas_mensal = input('Quantas horas voce trabalha por mes? ')
# convertendo string em int para digitar números
valor_hora = int(salario_mensal) / int(horas_trabalhadas_mensal)
print(valor_hora)
# fim do código
