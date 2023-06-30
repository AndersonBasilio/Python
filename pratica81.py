# List comprehension em Pyhton
# List comprehesion é uma forma rápida para criar listas
# a partir de iteraveis
# print(list(range(10)))

import pprint

def mostrar_na_tela(v):
    pprint.pprint(v, sort_dicts=False, width=40)
    

lista = []
for numero in range(10):
    lista.append(numero)
#print(lista)

lista = [numero * 2 for numero in range(10)]
#print(list(range(10)))
#print(lista)

# Mapeamento de dados em list comprehension

produtos = [
    {'nome': 'p1', 'preco':  20,},
    {'nome': 'p2', 'preco':  10,},
    {'nome': 'p3', 'preco':  30,},
]

#novos_produtos = [
#    {**produto, 'preco': produto['preco'] * 1.05}
#    if produto['preco'] > 20 else{**produto}
#    for produto in produtos
#]
#print(*novos_produtos, sep='\n')

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else{**produto}
    for produto in produtos
    if (produto['preco'] > 20 and produto['preco'] * 1.05) > 10
]
mostrar_na_tela(novos_produtos)