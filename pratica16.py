"""
Introdução ao try/ except
try -> tentar executar o codigo
except -> Ocorreu algum erro ao tentar executar
"""

numero_str = input('Dobrando o número que você digitar: ')

try:
    print('str: ', numero_str)
    numero_float = float(numero_str)
    print('Float: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2}.')

except:
    print('Isso não é um número.')