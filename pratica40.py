"""
Exercicio
Exiba os indices da lista
"""
import os

os. system('cls')

lista = ['Maria', 'Helena', 'Anderson']
lista.append('Juarez')
lista.append('Mercês')
lista.append(True)
lista.append(1.5)

cont = 0
for nome in lista:
    print(cont, nome, type(nome))
    cont += 1

print()