"""
Interpolação basica de string
S -> string
d e i -> int
f -> float
x e X -> Hexadecimal(ABCDEF0123456789)
"""
print('Interpolação de string com "%" em python')
nome = 'Anderson'# -> string
preco = 1000.95897643
variavel = '%s, o preço e R$ %.2f \n'%(nome,preco)
print(variavel)
