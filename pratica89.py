# Generator expression, Iterables e Iterators em Python
import sys


iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__() # Tem __iter__ e __next__
lista = [numero for numero in range(1000000)]
generator = (numero for numero in range(1000000))# So sabe qual sera o proximo valor.

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

#for numero in generator:
#   print(numero)