"""
Listas em Python
Tipo de List - Mutavel
Suporta vários valores de qualque tipo
Conhecimentos reutilizaveis - índices e fatiamento
Métodos uteis: 
append - Adiciona um item ao final 
insert - Adiciona um item no indice escolhido
pop - Remove do final ou do indice escolhido
del - Apaga um indice
clear - Limpa a lista
extend - Estende a lista
+ - Concatena listas
Create Read Update Delete
Criar, Ler, alterar, apagar = lista[i] (CRUD)
"""

#........0...1...2...3
lista = [10, 20, 30, 40]
lista.append('Anderson')# Qualquer coisa que quiser.
nome = lista.pop()# pop remove o ultimo item da lista
lista.append(1233)
del lista[-1]
#lista.clear() Limpa a lista
lista.insert(0, 5)# Recebe dois argumentos.
print(lista, nome)