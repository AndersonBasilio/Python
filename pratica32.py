"""
Como for funciona debaixo dos panos
Iteravél -> str, range, etc -> método chamado(__iter__).
Iterador -> Quem sabe entregar um valor por vez.
next -> Me entrega o proximo valor.
iter -> Me entrega o proximo iterador.
"""
#numeros = range(0, 100, 8)
#for numero in numeros:
   # print(numero)

#for letra in texto
texto = iter('Anderson')# iteravél
iterador = iter(texto)# iterador

while True:
    try:
        letra = (next(iterador))
        print(letra)
    except StopIteration:
        break
print(letra)