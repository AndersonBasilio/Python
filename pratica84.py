# Dictionary comprehension e set comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritorio',
}
novo_dicionario = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave , valor in produto.items()
    if chave == 'categoria' #if chave != 'categoria' mostra todas as chaves menos categoria.

}

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]

#dc = { # dictionary Comprehension
#    chave: valor
#    for chave, valor in lista
#}

# print(dict(lista)) Convertendo lista para dicionario

dc = {
    chave: valor
    for chave, valor in lista
}

s1 = {2 ** i for i in range(10)} # set Comprehension só passo valores
print(s1)