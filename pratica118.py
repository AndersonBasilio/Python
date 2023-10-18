import json

pessoa = {
    'nome': 'Anderson',
    'sobrenome': 'Basilio 1',
    'endereço': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero':55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
    # 'set': {1, 2, 3}
}

with open('aula121.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa, 
        arquivo, 
        ensure_ascii=False,
        indent=2,
    )

# with open('aula121.json', 'r', encoding='utf8') as arquivo:
#     pessoa = json.load(arquivo)
#     print(pessoa['nome'])
#