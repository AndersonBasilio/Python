"""
Higher Order Functions
Funções de primeira classe
"""

def saudacao(msg, nome): #
    return f'{msg}, {nome}'

def executa(funcao, *args):# Empacotando as coisa que passo na v = executa...
    return funcao(*args)# Estou chamando a função e desempacotei.


v = executa(saudacao, 'Bom dia', 'Anderson!')
print(v)