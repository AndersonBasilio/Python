print('Operadores "in" e "not in" ')
"""
Operadores in e not in
strings sao interaveis -> consegue navegar na string
0  1  2  3  4  5  6  7
A  n  d  e  r  s  o  n
-8 -7 -6 -5 -4 -3 -2 -1 -> itens negativo
"""

nome = 'Anderson'
print(nome[3])
print(nome[4])

print('d' in nome)
print('z' in nome)
print('And' in nome)
print('Zero' in nome)
print('-------------------')
print('And' not in nome) # False porque está entre o nome
print('Zero' not in nome)# True porque não está entre o nome

print('=================================')
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar em nome: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}.')
else:
    print(f'{encontrar} não esta em {nome}.')

