print('Melhor pratica de programação')

frase = ' Olha so que coisa interessante.   '
lista_frases_cruas = frase.split(', ')

lista_frase = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frase.append(lista_frases_cruas[i].strip())
print(lista_frases_cruas)# Lista antiga
print(lista_frase)# lista atualizada
