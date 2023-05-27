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
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)# Nao retorna nada.
print(lista_a)

print('--' * 30)

"""
Cuidado com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memoria(mutável)
"""

lista_d = ['Anderson', 'Maria', 1, True, 1.2]
lista_e = lista_d.copy()

lista_d[0] = 'Qualquer coisa'
print(lista_d)
print(lista_e)