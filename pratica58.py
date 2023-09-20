"""
Argumentos nomeados e não nomeados em funções Python
Argumento tem nome com sinal de igual
Argumento não é nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    print(f'{x = } {y = } {z = }', '|', f' {x} + {y} + {z} = {x + y + z}')

soma(5, 2, 3)# Quando falamos em definição falamos em valores, quando falamos em valores é argumentos.
soma(1, 7, z = 7)# Não é recomendado fazer assim, ou chame tudo da mesma forma que chamou 1.
soma(z = 7, x = 1, y = 7)# Valores serao mudados de ordem mas esta sendo atribuindo os valores

#soma -> Nome da função o que esta na memoria
#(1, 2, 3) -> Execução de função

#soma(1, 2, 3) -> Argumento não nomeado chamados na mesma ordem da definiçao
#soma(1, y2, z=5) -> Para passar fora da ordem usamos argumentos nomeados depois que nomeamos o primeiro todos os proximos precisa ser nomeados.

#print(1, 2, 3, sep=' - ')