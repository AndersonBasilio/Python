"""
Exercicio
1 - Faça um programa que peça para o usuário digitar um número inteiro, informe se este número é
par ou impar. Caso o usuário não digitar o número inteiro, informe que não é um número inteiro.

"""

try:
    numero = input('Digite um número: ')
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'impar'
    
    if par_impar:
        par_impar_texto = 'Par'
        print(f'O número {numero_int} é {par_impar_texto}')
    else:
        par_impar_texto = 'Impar'
        print(f'O número {numero_int} é {par_impar_texto}')

except:
    print('Você não digitou um número inteiro.')

print('===' * 10)
"""
2 - Faça um programa que pergunte a hora que ao usuário e baseando - no horario descrito, exiba a saudação
apropriada. Ex Bom dia 0 - 11, Boa Tarde 12 - 17, Boa Noite 18 - 23.

"""
try:
    
    hora = input('Digite a hora por favor: ')
    hora = int(hora)

    if hora >= 0 and hora <= 11:
        print('Bom Dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa Tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa Noite!')    
except:
    print('Você nao digitou um número inteiro.')

print('===' * 10)
"""
3 - Faça um programa que peça o primeiro nome do usuário. se o nome tiver 4 letras ou menos "Seu nome é curto", se tiver entre 5 e 6 letras, escreva
"Seu nome é normal", maior que 6 letras "Seu nome é muito grande".
"""

nome = input('Digite seu nome: ')
tamanho_do_nome = len(nome)

if tamanho_do_nome > 1:    
    if tamanho_do_nome <=  4:
        print('Seu nome é curto.')
    elif tamanho_do_nome >= 5 and tamanho_do_nome <= 6:
        print('Seu nome é normal.')
    else:
     print('Seu nome é grande.')
else:
    print('Você não digitou o que foi pedido ou digitou uma letra. Por favor digite corretamente o que foi pedido.')

print('===' * 10)