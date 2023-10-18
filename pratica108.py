# count é um iterador sem fim (itertools)
from itertools import count

contador = count(start=10, step=2)
range1 = range(10, 21, 2)

print('Contador tem o método iter: ', hasattr(contador, '__iter__'))
print('Contador tem o método next: ', hasattr(contador, '__next__'))
print('range tem o método iter: ', hasattr(range1, '__iter__'))
print('range tem o método iter: ', hasattr(range1, '__next__'))

print('\ncount')
for i in contador:
    if i > 20:
        break
    print(i)

print('\nrange')
for i in range1:
    print(i)
