# Exercicio unir listas
# Crie uma funcao
# O trabalho dessa função será unir duas listas na ordem
# Use todos valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']

from itertools import zip_longest

cidades = [
    'Salvador',
    'Ubatuba', 
    'Belo Horizonte',
]

estados = [
    'BA',
    'SP',
    'MG',
    'RJ',
]

# Crie uma função zipper
#def zipper(cidades, estados):
#    intervalo = min(len(cidades), len(estados))
#    for indice in range(intervalo):
#        return [
#            (cidades[indice], estados[indice]) for indice in range(intervalo)
#        ]

#print(zipper(cidades, estados))

# Modo Pythonico.
print(list(zip(cidades, estados)))# Importando itertools
print(list(zip_longest(cidades, estados, fillvalue='SEM CIDADE')))