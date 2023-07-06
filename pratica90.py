# Introdução as Generator functions em Pyhton
# generator = (numero for numero in range(100000))

def generator(numero=0, maximum=10):
    while True:
        yield numero
        numero += 1

        if numero > maximum:
            return 


gen = generator(numero=1, maximum=10)
for numero in gen:
    print(numero)