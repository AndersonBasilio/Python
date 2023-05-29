"""
Operador Ternario (Condicional de um linha)
<valor> if  <condicional> else <outro calor>
"""


#numero_1 = int(input('Digite um numero: '))
#numero_2 = int(input('Digite outro numero: '))
#condicao = numero_1 == numero_2
#variavel = f'{numero_1} é igual a {numero_2}.' if condicao else f'{numero_1} não é igual a {numero_2}.'
#verificando_condicao = f'A condiçao era {numero_1} = {numero_2}.' if condicao == True else f'\nA condicão era {numero_1} = {numero_1}.'

#print(variavel, verificando_condicao)

digito = 11 # > 9 = 0 -> Digito maior que 9 e Zero.
novo_digito = digito if digito <= 9 else digito# Se digito for maior que 9 o digito sera igual 0 senao igual ao digito mesmo.
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

print('Valor' if False else 'Outro valor'  if True else 'Fim')# Não é uma boa pratica.
