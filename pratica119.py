# Problema dos parâmetros mutáveis em funções Python

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('Anderson')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Mercês', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('Maria')
adiciona_clientes('Hetfield', cliente2)
adiciona_clientes('Helena', cliente2)
print(cliente2)