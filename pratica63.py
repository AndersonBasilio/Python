"""
Exercicios com funções

Crie uma função que multiplica todos argumentos não nomeados
Retorne o total para uma variavél e mostre o valor da variavél.
Crie uma função fala se um numero é par ou ímpar.
Retorne se o número é par ou ímpar.
"""

def multiplicar(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total

mutltiplicacao = multiplicar(1, 5, 1, 5, 1)
print(mutltiplicacao)

def par_ou_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'{numero} é Par'
    return f'{numero} é Ímpar'


print(par_ou_impar(mutltiplicacao))