"""
Introdução às funções (def) em Pyhton
Funções são trechos de códigos usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros(argumentos)
e retorna um valor específico.
Por padrão, funções Python retorna None(nada)
"""

#def Print():
    #print('Anderson')

#Print()

#def imprimir(a, b, c):
    #print(a, b, c)# Valores da função imprimir(a, b, c)

#imprimir(5, 3, 9)# Atribuindo os valores para função imprimir.
#imprimir(9, 8, 7)# Posso mudar os valores da função toda vez chamo uma função posso mudar os valores.

def saudacao(nome = 'Sem Nome'):# Atribuindo o valor "Sem Nome" para nome
    print(f'Ola {nome} tudo bem? Bem Vindo ao estudo de Python.')

saudacao('Anderson')# Tem que passar um valor se não dará um erro.
saudacao()# Passando o valor 'Sem Nome'