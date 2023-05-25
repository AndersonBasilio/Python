"""
while + while(Laços internos)
"""

quantidade_de_linhas = 5
quantidade_de_colunas = 4
linha = 0
while linha <= quantidade_de_linhas:
    coluna = 1
    while coluna <= quantidade_de_colunas:
        print(f'{linha}, {coluna}')
        coluna += 1
    print('-----------')
    linha += 1

print('Termina aqui.')
