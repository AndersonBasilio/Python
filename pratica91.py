# yield from

def generator_1():
    print('COMEÇOU GENERATOR 1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GENERATOR 1')

def generator_3():
    print('COMEÇOU GENERATOR 3')
    yield 10
    yield 20
    yield 30

def generator_2(generator=None):
    print('COMEÇOU GENERATOR 2')
    if generator is not None:
        yield from generator
    yield 4
    yield 5
    yield 6
    print('ACABOU GENERATOR 2')

gen1 = generator_2(generator_1())
gen2 = generator_2(generator_3())
gen3 = generator_2()
for numero in gen1:
    print(numero)
print()

for numero in gen2:
    print(numero)
print()

for numero in gen3:
    print(numero)
print()
