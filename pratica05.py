print('Introdução aos blocos de codigos + if/ elif/ else (Condicionais)')

entrada = input('Você deseja "entrar" ou "sair" do sistema? ')
    
if entrada == 'Entrar':
    print('Você entrou no sistema.')
elif entrada == 'Sair':
    print('Você saiu do sistema.')
else:
    print('Você nao digitou nem "Entrar" nem "Sair".')

print('====' * 17)
numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))

if numero1 > numero2:
    print(f'{numero1} + {numero2} = {numero1 + numero2}')
else:
        print(f'{numero2} - {numero1} = {numero2 - numero1}\n')