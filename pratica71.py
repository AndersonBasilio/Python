# get obtem uma chave
# pop - Apaga um itém com a chave especificada (del)
# popitem - Apaga o ultimo item adicionado
# update - Atualiza um dicionario com outro

p1 = {
    'nome': 'Anderson',
    'sobrenome': 'Basilio'
}

#print(p1['nome'])
#print(p1.get('nome', 'Nome não existe'))

#nome = p1.pop('nome')
#print(nome)
#print(p1)

#ultima_chave = p1.popitem()
#print(ultima_chave)
#print(p1)

#p1.update({
#    'nome': 'novo valor',
#    'idade': 30
#})
#print(p1)

#p1.update(nome='novo valor', idade= 30)
#print(p1)

#tupla = (('nome', 'novo valor'),('idade', 30))
#p1.update(tupla)
#print(p1)

lista = [['nome', 'novo valor',], ['idade', 30]]
p1.update(lista)
print(p1)