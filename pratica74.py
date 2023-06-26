# Exemplo de uso dos sets

letras = set()
while True:
    letra = input('Digite uma letra: ')
    letras.add(letra)

    if 'l' in letras:
        print('PARABÉNS')
        print(f'A letra era {letra}')
        break

    print(letras)