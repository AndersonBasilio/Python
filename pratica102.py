# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usadas para fazer o Python usar outras funções.

def criar_funcao(funcao):
    def interna(*args, **kwargs):
        print('Vou te decorar.')
        for arg in args:
            e_string(arg)
        resultado = funcao(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, você foi decorada!')
        return resultado
    return interna

def inverte_string(string):
    return string[::-1]

def e_string(parametro):
    if not isinstance(parametro, str):
        raise TypeError('Parâmetro deve ser uma string.')


inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro(input('Digite algo que deseja inverter: '))
print(invertida)
