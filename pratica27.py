# while/ else

string = 'Qualquer valor'

i = 0
while i < len(string):
    letra = string[i]
    
    # Se encontrar espaço o break será executado
    # Se não encontrar espaço o break não será executado
    if letra == ' ':
        break

    print(letra)
    i += 1
else:
        print('Não encontrei espaço na string.')