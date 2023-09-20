"""
lista e seus indices
"""
salas = [
    #   0        1
    ['Maria', 'Helena', ],# 0
    #    1
    ['Elaine', ],# 1
    #  0        1        2              3
    ['Luiz', 'João', 'Edudarda', (0, 10, 20, 30, 40)] ,# 2
]

print(salas[1][0])
#print(salas[0][1])
#print(salas[2][2])
#print(salas[1][0])
#print(salas[2][3][2])

for sala in salas:
    print(f'Sala é {sala}.')
    for aluno in sala:
            print(f'O aluno(a) da sala é {aluno}')
