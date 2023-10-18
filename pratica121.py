# Controlando a quantidade de argmentos posicionais e nomeados em funções
# args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# Positional-only Parameters (/) - Tudo antes de barra deve
# ser APENAS posicional.
# PEP 570 - Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# Keyword-Only Arguments (*) - * sozinho NÂO SUGA valores.
# PEP 3120 - Keyword-Only Arguments
# https://peps.python.org/pep-3102/

# def soma(a, b, /, x, y):
#     print(f'{a} + {b} + {x} + {y} = {a+ b + x + y}')


# #soma(1, 2)
# #soma(1, 2, 3, y=3)

def soma(a, b, /, *, c, **kwargs):
    print(kwargs)
    print(f'{a} + {b} + {c} = {a + b + c}')


#soma(1, 2)
soma(1, 2, c=3, nome='teste')