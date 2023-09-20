"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parametro, o valor padrão será usado.
Refatorar: Editar o seu código. -> Nunca seu código esta pronto sempre pode melhorar
"""

def soma_teste(x, z = None, y = '' ):# Todos parâmetros que vierem após os nomeados devem ser nomeados.
    print(f'{x} + {y} + {z} | {x} + {y} + {z} = {x + y + z}')

def soma(x, y, z = None):# 0, 0.0, '' -> É considerado um valor Falsy
    #def soma(x, z = None, y = None) -> Dessa forma vai dar um erro NoneType
    if z is not None:# Para saber se o z não é None
        print(f'{x = } {y = } {z = } | {x} + {y} + {z} = {x + y + z}')
    else:
        print(f'{x = } {y = } | {x} + {y} = {x + y}')

#Obs: Não posso executar meu codigo se passar o valor z em todos locais que estava utilizando essa função.

soma(1, 2, 5)#Se eu envio o valor para z o valor e o que foi enviado
soma(3, 5)# Se eu não envio o valor para z é None
soma(100, 200)# Se eu não envio o valor para z é None
soma(7, 9, 0)#Se eu envio o valor para z o valor e o que foi enviado
soma(z = 5, y = 1, x = 2)# Enviando os valores nomeados.

soma_teste(x=2, y=7, z=9)