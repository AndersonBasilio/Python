# filter é um filtro funcional

def print_iter(iterador):
    print(*list(iterador), sep='\n')
    print()

def filtrar_preco(produto):
    return produto['preco'] > 100

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 2', 'preco': 22.32},
    {'nome': 'Produto 1', 'preco': 10.11},
    {'nome': 'Produto 3', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

#novos_produtos = [
#    produto for produto in produtos if produto['preco'] > 20
#]

novos_produtos = filter(#lambda produto: produto['preco'] >= 10, produtos
    filtrar_preco, produtos)

print_iter(produtos)
print_iter(novos_produtos)