import os
os.system('cls')

while True:
    numero_1 = input('Digite um número: ')
    numero_2 =  input('Digite outro número: ')
    operador = input('Digite o operador(+ - * /): ')

    # Flags
    numero_validos = None
    numero_1_float = 0
    numero_2_float = 0
 
    try: #Convertendo os numeros que o usuário digitou para float
        numero_1_float =  float(numero_1)
        numero_2_float = float(numero_2)
        numero_validos = True

    except:
        numero_validos = None

    if numero_validos is None:
        print('Um ou ambos os números digitados são invalidos. ')
        continue

    operadores_permitidos = '+-/*'

    if  operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    if len(operador) > 1:
        print('Por favor informe apenas um operador.')
        continue

    os.system('cls')

    print('Realizando sua conta confira o resultado abaixo.')

    if operador == '+':
        print(f'{numero_1_float} + {numero_2_float} = {numero_1_float + numero_2_float}')
    
    elif operador == '-':
        print(f'{numero_1_float} - {numero_2_float} = {numero_1_float - numero_2_float}')
    
    elif operador == '/':
        print(f'{numero_1_float} / {numero_2_float} = {numero_1_float / numero_2_float}')
    
    elif operador == '*':
        print(f'{numero_1_float} x {numero_2_float} = {numero_1_float * numero_2_float}')
        
    else:
        print('Nunca deveria ter chegado até aqui.')
    
    print('===' * 15)

    sair = input('Deseja sair ou continuar? [Sim]/ [Nao]: ').lower(). startswith('s')

    os.system('cls')
    print('Saindo...')
    print('Obrigado por participar!!!\n')
    
    if sair is True:
        break

     
