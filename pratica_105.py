# Ordem dos decoradores

def parametros_decorador(nome):
    def decorador(funcao):
        print('Decorador: ', nome)
    
        def sua_nova_funcao(*args, **kwargs):
            resposta = funcao(*args, **kwargs)
            final = f'{resposta}, {nome}'
            return final
        return sua_nova_funcao
    return decorador

@parametros_decorador(nome= 'terceiro')
@parametros_decorador(nome = 'segundo')
@parametros_decorador(nome='primeiro')

def soma(x, y):
    return f'{x} + {y} = {x + y}'

dez_mais_cinco = soma(5, 6)
print(dez_mais_cinco)
