# groupby agrupando valores  (itertools)

from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota':'A'},
    {'nome': 'Anderson', 'nota':'B'},
    {'nome': 'Leticia', 'nota':'A'},
    {'nome': 'Fabricio', 'nota':'C'},
    {'nome': 'Rosemary', 'nota': 'A'},
    {'nome': 'Amanda', 'nota':'B'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota':'C'},
    {'nome': 'Eduarda', 'nota': 'D'},
    {'nome': 'André', 'nota':'A'},
    {'nome': 'Freddie Mercury', 'nota': 'A'},
    {'nome': 'James Hetfield', 'nota':'D'},
]

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print()
    print('==' * 20)
    print(f'Notas {chave}')
    print('==' * 20)
    for aluno in grupo:
        print(aluno)
print('==' * 20)