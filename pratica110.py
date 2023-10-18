# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iteravel + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

def print_iter(iterador):
    print(*list(iterador), sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Leticia',
]

camisetas = [
    ['Preta', 'Branca'],
    ['p', 'm'],
    ['Masculino', 'Feminino'],
    ['Algodão', 'Poliester']
]

# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))