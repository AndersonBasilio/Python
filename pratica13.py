"""
Fatiamento de string
0123456 -> indices positivo
Ola mundo -> string são interavel assim podemos pegar letra por letra
-9-8-7-6-5-4-3-2-1 -> indeces negativos vai depender da quantidade -1-2-3
fatiamento[i:f:p][::] -> inicio, fim, passo(indice final, e omitido pelo Python)
OBS: A função len retorna a quantidade de caractere da str
OBS: A contagem começa do indice 0.
"""
variavel = 'Ola Mundo'
print(variavel[4:])# Ira começar a contar MUNDO.
print(variavel[-8:2])# ira pegar a letra l
print(variavel[1:9:3])# Ira pegar o lMd
print(len(variavel))# Numero de Letras
print(variavel[-1:-10:-1])# Inverte a palavra