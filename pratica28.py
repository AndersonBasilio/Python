"""
Qual letra apareceu mais vezes no while? (iterando string com while)
\ -> Quebra linha
"""
import os
os.system('cls')
frase = 'O python é uma linguagem de programação'\
'multiparadigma'\
'Python foi criado por Guido Von Rossum.'

#print(frase.lower().count('python'))# count é um metodo dentro da string que ira contar quantas vezes a palavra Python apareceu.
# OBS: Letras maiusculas e minusculas são diferentes no pyhton.

i = 0 # Criando o indice
quantidade_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = '' #string vazia

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    quantidade_atual = frase.count(letra_atual)# vemos quantas a letra apareceu

    if quantidade_apareceu_mais_vezes <= quantidade_atual:
        quantidade_apareceu_mais_vezes = quantidade_atual
        letra_apareceu_mais_vezes = letra_atual
    i += 1

print(f'A letra que apareceu mais vezes foi [{letra_apareceu_mais_vezes}] que apareceu {quantidade_apareceu_mais_vezes} vezes.\n')



