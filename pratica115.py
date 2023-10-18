# Funções recursiva e recursividade
# funções que podem se chamar de volta
# úteis para dividir problemas graves em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em parte menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão 
#  - fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

#import sys
#sys.setrecursionlimit(1004)

#def recursiva(inicio=0, fim=4):
#    print(inicio, fim)
    # Caso base
#    if inicio >= fim:
#        return fim
        # Caso recursivo
    # Conta até chegar ao final.
#    inicio += 1
#    return recursiva(inicio, fim)

#print(recursiva(0, 1000))


def factorial(numero):
    if numero <= 1:
        return 1
       
    return numero * factorial(numero - 1)

print(factorial(5))
print(factorial(10))