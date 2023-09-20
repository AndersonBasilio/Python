print('Operadores Relacionais (de Comparação)')
"""
OP           Significado         Exemplo(True)
>            maior                  2 > 1
<            maior igual            2 >= 2
>=           menor                  1 < 2
<=           menor igual            2 <= 2
==           igual                 'a' == 'a'
!=           Diferente             'a' != 'b'

"""
numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))


if numero1 > numero2:
    print(f'{numero1} e maior que {numero2}.')
elif numero1 < numero2:
    print(f'{numero1} e menor que {numero2}.')
else:
    print(f'{numero1} é igual ao {numero2}')

letra1 = input('Digite uma letra: ')
letra2 = input('Digite outra letra ')

if letra1 and letra2:
    if letra1 == letra2:
         print(f'A letra ({letra1}) e igual a letra ({letra2}).')
    elif letra1 != letra2:
         print(f'A letra ({letra1}) é diferente da letra ({letra2}).')
