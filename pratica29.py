#Exemplo do while -> Quando não sabemos quantas repetições vai ser.

senha_salva = 123456
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input('Sua senha {repeticoes}: ')
    repeticoes += 1
    print(repeticoes)
    print('Esse codigo pode ter repetições infinitas.')