# BASICO DE LOGICA DE PROGRAMAÇÃO (EXEMPLOS EM PYTHON)#
# ------------------------------------------------------------#
## ---Condicionais--- ##
# IF, ELSE e ELIF

# >>PODER SAIR DE CASA APENAS QUANDO TRABALHO ESTIVER TERMINADO<< #

trabalho_terminado = True
if trabalho_terminado == True:
    print('Pode sair de casa.')
else:
    print('Nao pode sair.')

# >>PODER ENTRAR NA SALA DE AULA ATRASADO APENAS SE NAO FOR O 3o DIA DE ATRASO<< #

atrasos = 2
if atrasos >= 3:  # executado primeiro
    print('Voce esta suspenso')
elif atrasos == 1:  # elif só é executado caso o if/elif anterior não tenha sido executado
    print('Caso tenha mais 2 ocorrencias, sera suspenso.')
elif atrasos == 2:
    print('Caso tenha mais 1 ocorrencia, sera suspenso')
else:
    print('Pode entrar')

# >>ENCONTRAR O NUMERO MAIOR ENTRE 2 NUMEROS COMPARADOS<< #

primeiro_valor = input('Digite o primeiro numero: ')
segundo_valor = input('Digite o segundo numero: ')

if int(primeiro_valor) > int(segundo_valor):
    print('O primeiro valor é maior!')
else:
    print('O segundo valor é maior!')
