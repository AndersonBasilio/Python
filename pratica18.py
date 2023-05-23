"""
flags(Bandeira) - Marca o local
none = não nulo
is e is not = é ou nao é(tipo, valor, identidade)
id = identidade 
"""
v1 = 'a'
v2 = 'b'# Se a variavel 2 for a mesma da variavel 1 o id e o mesmo.
print(id(v1))
print(id(v2))

print('----------------------------')

condicao = True
passou_no_if = None
if condicao:
    passou_no_if = True #Isso nao e bom tem que declarar a variavel fora do bloco
    print('Faça algo')

else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if.')


