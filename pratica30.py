"""
Introduçao ao for/ in - estrutura de repetição para coisas finitas
Iteravel podemos iterar uma vez por cada string ou variavel.
"""
nome = input('Qual é seu nome: ')

novo_nome = ''
for letra in nome:
    novo_nome += f'*{letra}'
    print(letra)

print(novo_nome)
