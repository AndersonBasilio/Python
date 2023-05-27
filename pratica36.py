"""
Listas em Python
Tipo de List - Mutavel
Suporta vários valores de qualque tipo
Conhecimentos reutilizaveis - índices e fatiamento
Métodos uteis: append, insert, pop, del, clear, extend, +
Create, Read, Ler, alterar, apagar = lista[i] (CRUD)
"""
import os
os.system('cls')

lista = [10, 20, 30, 40]
#numero = lista[2]# Pegando o dado da lista em uma variavel Read
#lista[2] = 300# Alterando
#del lista[2]# Python deleta e reorganiza o indice da lista.
lista.append(50)# irá adicionar o valor escolhido(50), pode ser executado quantos valores quiser
lista.pop()# Remove o valor adicionado, no caso o cinquenta.
lista.append(50)
lista.append(60)
lista.append(70)
lista.append(80)
ultimo_valor = lista.pop(3)# Retorna o inteiro porque a lista é inteiro remove por indice
#OBS: Se a lista for muito grande evitar de mexer no meio da lista.
lista.append(90)
lista. append(100)
print(lista, 'Removido, ', ultimo_valor, '\n')
