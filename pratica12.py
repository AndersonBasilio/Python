"""
Formatação básica de strings
s -> string
d -> int
f -> float
. <número digitado>f
x ou X -> Hexadecimal
(caractere)(<>^)(quantidade)
> Esquerda
< Direita
Sinal -> + ou -
Ex. 0 > 100,.1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(variavel)
print(f'.{variavel:>10}')# Preenche com espaço esquerda.
print(f'{variavel:<10}.')# Preenche com espaço a direita.
print(f'{variavel:^10}')# Deixa a letra no centro.
print(f'{variavel:0^10}')# Completa com 0 e deixa as letras no centro.