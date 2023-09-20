# Desempacotamento em chamadas de metodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'Legal.'
salas = [
    #   0        1
    ['Maria', 'Helena', ],# 0
    #    1
    ['Elaine', ],# 1
    #  0        1        2              3
    ['Luiz', 'João', 'Edudarda', (0, 10, 20, 30, 40)] ,# 2
]

#p, b, *_, ap, u = lista
#print(p, u, ap)

#for nome in lista:
   # print(nome, end=' ', sep=' ') # Esse print esta com end= estava como quebra de linha e o sep= como espaço

#print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
#print(*lista)# -> Esse print e a mesma coisa do print acima.
#print(*string)
#print(*tupla)

print(*salas, sep= '\n')# -> Passando a lista