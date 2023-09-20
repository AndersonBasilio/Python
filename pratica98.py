# arquivo main
#from sys import path

#import aula102_package.modulo
#from aula102_package.modulo import soma_do_modulo
#from aula102_package import modulo
#from aula102_package.modulo import *

#print(*path, sep="\n")

#print(soma_do_modulo(1, 2))
#print(aula102_package.modulo.soma_do_modulo(1, 2))
#print(modulo.soma_do_modulo(1, 2))
#print(variavel)

# from aula102_package.modulo import soma_do_modulo, fala_oi

# fala_oi()
# print(__name__)

from aula98_package import falar_oi, soma_do_modulo

print(soma_do_modulo(2, 5))
falar_oi()