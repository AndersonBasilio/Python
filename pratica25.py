# Iterando strings com while

nome = input('Digite seu nome: ')
indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += letra
    indice += 1
    novo_nome += '*'
print(f'*{novo_nome}\n')
