# Métodos úteis dos dicionários em Python (Tudo em Python e um objeto, métodos geralmente estão dentro dos objetos)
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma copia rasa (shallow copy)
# get obtem uma chave
# pop - Apaga um itém com a chave especificada (del)
# popitem - Apaga o ultimo item adicionado
# update - Atualiza um dicionario com outro
# dunder method começa com dois __ e termina com __

pessoa = {
    'nome': 'Anderson',
    'sobrenome': 'Basilio',
    # Se usarmos chaves repitidos quando usamos len será dois valores porque estou repetindo.
    #'sobrenome': 'Basilio 1',
    #'sobrenome': 'Basilio 2',
    #'idade': 900 # Se tiver a idade retornará 

}

#print((pessoa.__len__())) # Método dunder __len__
#print(len(pessoa))# ira retornar a quantidade chaves
#print(pessoa.keys())# irá retornar as chaves dic
#print(list(pessoa.keys()))# Convertendo chaves para lista.
#print(list(pessoa.values()))# So terei os valores
#print(list(pessoa.items()))# irá retornar a chave e o valor, convertido para lista.
pessoa.setdefault('idade', 0)# Passamos a chave para o dicionario e o valor que quisermos.
print(pessoa['idade'])# Se não tiver no dicionario ira dar um erro.

#Enumerate ira retorna chave e valor lista tupla dentro.
#for chave, valor in pessoa.items():
#    print(chave, valor)

#for valor in pessoa.values():
#   print(valor)# So valores.