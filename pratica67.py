# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Anderson',
#     'sobrenome': 'Basilio',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Anderson', sobrenome='Basilio') Não é tão usada.

pessoa = {
    'nome': 'Anderson',
    'sobrenome': 'Basilio',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
 
#print(pessoa, type(pessoa))

print(pessoa['nome'])# Acessando uma coisa em especifico.

# Dicionario nao é um método interavel mas o Python converte.
for chave in pessoa:
    print(f'{chave}: {pessoa[chave]}')# Pegando o valor da chave e o valor de pessoa.