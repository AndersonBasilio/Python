import os

os.system('cls')

print('==================')
print('Calculando IMC')
print('==================')

nome = input('Qual é seu nome: ')
peso = input('Digite seu peso: ')
altura = input('Digite sua altura: ')

try:

    nome = str(nome)
    peso = float(peso)
    altura = float(altura)

    IMC = peso / (altura * altura)

    os.system('cls')

    print(f'Olá {nome} seu IMC e {IMC:.2f}.')

    if IMC <= 17:
        print('Muito abaixo do peso.')

    elif IMC >= 17 and IMC < 18.5: 
        print('Abaixo do peso.')
    
    elif IMC >= 18.5 and IMC < 25:
        print('Peso ideal.')
    
    elif IMC >= 25 and IMC < 30:
        print('Sobrepeso.')
    
    elif IMC >= 30 and IMC < 35:
        print('Obesidade')
    
    elif IMC >= 35 and IMC < 40:
        print('Obesidade Severa.')
    
    else:
        print('Obesidade Mórbida')

except:
    print('Você não digitou os dados pedidos corretamente.')


