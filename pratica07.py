"""
Operadores lógicos
and(e), or(ou), not(não)
and -> Todas as condições precisam ser verdadeiras
se qualquer valor for considerado falso,
a expressão inteira será avaliada naquele valor
Sao considerados falsy 
O O.O " " False String vazia
Também existe o tipo none que é usada
para representar um valor que não existe.

if condicao = True
"""
print('Operadore Lógico "and"')

entrada = input('[E] para Entrar / [S] para Sair: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print("Entrada Permitida")
else:
    print("Saindo...")

print("===" * 15)

print(True and True and True)
print(True and False and True)
print(bool(0.0))
print('')# string vazia
print(' ')# string com espaço
print(True and 0 and True)
