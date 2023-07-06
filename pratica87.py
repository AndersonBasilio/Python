# dir, hasattr e getattr em Pyhton

string = 'Anderson'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não tem o método', metodo)