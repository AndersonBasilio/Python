# Decoradore com parâmetro

def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(funcoes):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            resposta = funcoes(*args, **kwargs)
            return resposta
        return aninhada
    return fabrica_de_funcoes

@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
        return f'{x} + {y} = {x + y}'

    
decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: f'{x} x {y} = {x * y}')

dez_mais_cinco = soma(2, 8)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)
