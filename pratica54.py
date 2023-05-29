import re
import os
import sys

os.system('cls')
cpf = input('Digite seu CPF: ')
cpf_enviado_pelo_usuario = re.sub(r'[^0-9]', '', cpf)

entrada_e_sequencial = cpf == cpf[0] * len(cpf)# conferindo se o usuário digitou numero repetidos.
if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

nove_digitos = cpf_enviado_pelo_usuario[:9]
contador_regressivo_1 = 10
resultador_para_digito_1 = 0

for digito_1 in nove_digitos:
    resultador_para_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultador_para_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = cpf_enviado_pelo_usuario[:10]
contador_regressivo_2 = 11

resultador_para_digito_2 = 0

for digito_2 in dez_digitos:
    resultador_para_digito_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultador_para_digito_2 * 10) % 11
digito_2  = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_pelo_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf} é válido.')
else:
    print(f'{cpf} é inválido.')