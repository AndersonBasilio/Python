"""
(Parte1 e Parte2)
args - Argumentos não nomeados
* - * args (empacotamento e desempacotamento)
# Lembre-te de desempacotamento
"""

#     empacotamento
#x, y, *resto = 1, 2, 3, 4
#print(x, y, resto)

#def soma(x, y):
 #   return x + y

def soma(*args):
    total = 0
    for numeros in args:
        total += numeros
    return total
 

soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)


soma_4_5_6 = soma(4, 5, 6)
print(soma_4_5_6)


outra_soma = soma(1, 2, 3, 4, 5, 6, 7, 78, 10)
print(outra_soma)

print(sum((1, 2, 3, 4, 5, 6, 7, 78, 10)))# sum é uma função pronta no Python temos que passar como uma tupla.