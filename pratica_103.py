# Funções decoradoras e decoradores
# Decorar Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são que funções que decoram outras funções
# Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções.
# Decoradores sao "Sintax sugar" (Açucar Sintatica)

def criar_funcao(funcao):
    def interna(*args, **kwargs):
        print('Vou te decorar.')
        for arg in args:
            e_string(arg)
        resultado = funcao(*args, **kwargs)
        print(f'O resultado foi {resultado}.')
        print(f'Ok, agora foi decorado.')
        return resultado
    return interna

@criar_funcao
def inverte_string(string):
    return string[::-1]

def e_string(parametro):
    if not isinstance(parametro, str):
        raise TypeError('Parâmtro deve ser uma string.')
    

invertida = inverte_string(input('Digite o que deseja inverter: '))
print(invertida)
