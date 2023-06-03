

print('+','=' * 15,'+')
print('|    Exercicio    |')
print('+','=' * 15, '+')

nome = input('Qual é seu nome? ')
idade = input('Qual é sua idade? ')
if nome and idade:
    print(f'Seu nome é {nome}.')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome tem espaço.')
    else:
        print('Seu nome não tem espaços.')
    if ' ' in nome:
        nome = nome.replace(' ', '')
        print(f'Seu nome tem {len(nome)} letras.')
    else:
        print(f'Seu nome tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é {nome[:1]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
    print(f'Sua idade é {idade}')
else:
    print(f'Desculpe, você deixou campos vazios tente novamente')
