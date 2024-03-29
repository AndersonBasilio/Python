# Exercicio adiando funções
def soma(x, y):
    return f'{x} + {y} = {x + y}'

def multiplica(x, y):
    return f'{x} x {y}  = {x * y}'


def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(10))
print(multiplica_por_dez(10))
