"""
enumerate - enumera iteraveis (índices)
"""
#[(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'Joao')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

#lista_enumerada = enumerate(lista)

#for indice, nome in enumerate(lista):
  #  print(indice, nome)

#for tupla_enumerada in enumerate(lista):
 #   print('For da tupla: ')
  #  for valor in tupla_enumerada:
  #      print(f'\t{valor}')