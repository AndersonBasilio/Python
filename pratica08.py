print('Operador Lógico "OR"')

entrada = input('[E] para Entra/ [S] para Sair: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar...')
elif entrada == '' or senha_digitada == '':
    print('Você não preencheu corretamente uma ou ambas informações. Por favor, preencha corretamente.')
else:
    print('Saindo...')

print('==='  * 32)

print('\nAvaliação de curto circuito')
senha = input('Senha: ') or 'Sem senha' # Se nao digitar nada irá aparecer sem senha
print('Sem senha')

print(True or False) # Irá parar na primeira condição verdadeira
print(True or False or True)
print(0 or False or False or 'ABC')
print(0 or False or False or 0 or 'ABC' or True)
