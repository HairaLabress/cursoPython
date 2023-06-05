# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicacao(*args):
    calculo = 1
    for numeros in args:
        calculo = calculo * numeros
    print (calculo)


resultado = multiplicacao(1,2,3,4,5)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(numero):
    if numero % 2 == 0:
        return print(f'O número {numero} é par')
    return print(f'O número {numero} é impar')
    
par_impar(4)
