"""
while + continue - pulando alguma repetição
"""

contador = 0
while contador <= 100:
    contador += 1
    if contador == 6:
        print(f'Não vou mostrar o número {contador}.')
        continue
    
    if contador >= 10 and contador  <= 27:
        print(f'Não vou mostrar o {contador}')
        continue

    print(contador)

    if contador ==  40:# Forçando a parar no quarenta.
        break # Vai terminar o laço não importando a condição.
print('Fim da Contagem!')

# break e continue -> Serão usados para o while mais proximos deles, as vezes podemos ter um while
# continue -> Se colocar continue dentro do laço antes do contador gera um laço infinito.