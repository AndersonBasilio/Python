# reduce - faz a redução de um iteravel em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 2', 'preco': 22},
    {'nome': 'Produto 1', 'preco': 2},
    {'nome': 'Produto 3', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

#def funcao_do_reduce(acumulador, produto):
#   print('Acumulador: ', acumulador)
#   print('Produto: ', produto)
#   print()
#   return acumulador + produto['preco']


total = reduce(
    #funcao_do_reduce, 
    lambda acumulador, produto: acumulador + produto['preco'],
    produtos,
    0
)

print('Total é ', total)

#total = 0
#for produto in produtos:
#    total += produto['preco']

#print('Total: ', total)


#print('Total: ', sum([produto['preco'] for produto in produtos]))