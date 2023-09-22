# Combinations, Permutations e itertools
# Combinação a ordem não importa - iteravel + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores unicos

# Não esqucer de inserir combinations, permutations, product
from itertools import combinations, permutations, product

def print_iter(iterador):
    print(*list(iterador), sep='\n')
    print()

pessoas = [
    'Joana', 'Joao', 'Luiz', 'Leticia',
]

camisetas = [
    ['Preta', 'Branca'],
    ['P', 'M',],
    ['Masculino', 'Feminino'],
    ['Algodão', 'Poliéster']
]

print('Combinação - Não repete as combinações') # Não repete
print_iter(combinations(pessoas, 2))

print('Permutação - Repete') # Repete
print_iter(permutations(pessoas, 2))

print('Produto')
print_iter(product(*camisetas))# Tem que desempacotar com (*)