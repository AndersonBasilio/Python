"""
Exercícios
Crie funções que duplicam, triplicam e quadriplicam
o numero recebido como parâmetro.
"""

#def duplicar(numero):
    #return numero * 2

#def triplicar(numero):
    #return numero * 3

#def quadriplica(numero):
    #return numero * 4

def criar_multiplicador(multiplicador):# Criando uma função que ira receber um multiplicador.
    def multiplicar(numero):# Criando uma função que ira receber um número que irá multiplicar o número.
        return numero * multiplicador
    return multiplicar


 

duplicar = criar_multiplicador(2)# Criando uma variavel para duplicar.
triplicar = criar_multiplicador(3)# Criando uma variavel para triplicar.
quadriplicar = criar_multiplicador(4)# Criando uma variavel para quadruplicar.

print(f'Duplicando = {duplicar(2)}')
print(f'Triplicando = {triplicar(2)}')
print(f'Quadruplicando = {quadriplicar(2)}')
