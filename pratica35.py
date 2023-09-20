"""
Tipos de lista (list) - Introdução a listas mutavéis em Python
Listas em Python
Tipos de List - Mutavél
Suporta varios valores de qualquer tipo conhecimentos reutilizaveis - indices, fatiamento
Metodos uteis: append, insert, pop, del, clear, extend, +
"""
#....... - 5 4 3 2 1
#....... + 1 2 3 4 5
lista = 'A B C D E'

# print(bool([]))
# print(lista, type(lista))

#........-5...-4.......-3.......-2..-1
#........0.....1........2........3...4
lista = [123, True, 'Anderson', 1.2, []]
lista[-3] = 'Metallica'

print(lista[-3].upper(), type(lista[2]))
print(lista[0], type(lista[3]))