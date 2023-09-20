"""
split, join e strip sao metodos muito uteis da str
split e join com lista str
split divide uma string
join une uma string
"""
frase = '   Olha só que coisa interessante.'
lista_frase = frase.split(', ')# Se quiser quebrar na virgula e no espaço.

for i, frase in enumerate(lista_frase):
    print(lista_frase[i].strip())# strip corta os espaços dos dois lados
    print(lista_frase[i].rstrip())# rstrip corta os espaços somente da direita
    print(lista_frase[i].lstrip())# lstrip corta os espaços somente da esquerda
print(lista_frase)