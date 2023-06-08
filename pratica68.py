# Manipulando chaves e valores em dicionários
# Não podemos acessar uma chave que nao existir em dicionário.

pessoa = {}# Essas chaves precisam existir, se não existir vamos ter exeções e ira parar o programa no momento que a exeção ocorrer.

    ##Muitos codigos
    ##

chave = 'nome'# Criando uma chave dinamicamente para acessar uma varivel.
pessoa[chave] = 'Anderson'# Esta recebendo o valor, podemos inserir qualquer valor.

pessoa['sobrenome'] = 'Miranda'# Criando uma chave para sobrenome.
print(pessoa[chave])# Acessando a chave tambem pelos colchetes.

pessoa[chave] = 'Helena'# Criando uma chave no dicionário

del pessoa['sobrenome']# Para apagar usamos del pessoa e o nome da chave que queremos apagar.
print(pessoa)
print(pessoa['nome'])


# Evitando erro quando não existir "Sobrenome"
# if não faz a exerção parar.
# Por padrão o get retorna None.
# Se existir retorna o valor da chave em si.
# get tenta obter uma chave.
if pessoa.get('sobrenome') is None: # Se não exixte retornará (Nao existe)
    print('Não existe')
else:
    print(pessoa['sobrenome'])# Se existir retornará o sobrenome.