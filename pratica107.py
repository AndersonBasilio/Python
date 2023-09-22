# Considerando duas listas de inteiro ou float(lista_a e lista_b)
# Some os valores nas listas retornando uma nova lista com os valores somados
# Se uma lista for maior que a outra, a soma so vai considerar o tamanho da menor
# Exemplo:
# lista_a = [1, 2, 3, 4, 5, 6, 7]
# lista_b = [1, 2, 3, 4]
# ============ Resultado
# lista_soma = [2, 4, 6, 8]

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

#Minha Solução
#def zipper(lista_a, lista_b):
#    intervalo = min(len(lista_a), len(lista_b))
#    return [
#        (lista_a[indice] + lista_b[indice]) for indice in range(intervalo)
#    ]

#lista_soma = zipper(lista_a, lista_b)
#print('lista_a   ', lista_a)
#print('lista_b   ', lista_b)
#print('lista_soma', lista_soma)

# Funciona para qualquer linguagem
#lista_soma  = []
#if lista_a < lista_b:
#    for indice in range(len(lista_a)):       
#        lista_soma.append(lista_a[indice] + lista_b[indice])
#else:
#    for indice in range(len(lista_b)):
#        lista_soma.append(lista_a[indice] + lista_b[indice])

#print('lista_soma', lista_soma)

# Solução Pythonica
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print('lista_soma', lista_soma)