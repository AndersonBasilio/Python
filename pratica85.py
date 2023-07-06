# isinstance - Para saber se o objeto é de determinado tipo
lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Anderson'}]

for item in lista:
    if isinstance(item, set):
        print('\nSET')
        item.add(5)
        item.add(200)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('\nSTR')
        item.upper()
        print(item.upper())

    elif isinstance(item, (int, float)):
        print('\nNUM')
        print(item * 2)

    else:
        print('\nOUTRO')
        print(item)