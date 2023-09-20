# Empacotamento e Desempacotamento de Dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)

# pessoas = {
#    'Nome:': 'Anderson',
#    'Sobrenome:': 'Basilio',
# }

# (a1, a2), (b1, b2) = pessoas.items()
# print(a1, a2)
# print(b1, b2)

pessoas = {
    'Nome:': 'Anderson',
    'Sobrenome:': 'Basilio',
}

dados_pessoas = {
    'Idade:': 32,
    'Altura:': 1.89,
}

dados_completos = {**pessoas, **dados_pessoas}
# print('\n', dados_completos, '\n')

# args e Kwargs
# args(já vimos)
# kwargs - keword aeguments(argumentos nomeados)

def mostra_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS ', args)
    for chave, valor in kwargs.items():
        print(chave, valor)

# mostra_argumentos_nomeados('Anderson', nome='Joana', sobrenome='Souza')
# mostra_argumentos_nomeados(**dados_completos)

configuracoes = {
    'arg1' : 1,
    'arg2' : 2,
    'arg3' : 3,
    'arg4' : 4,
}

mostra_argumentos_nomeados(**configuracoes)
