"""
range + for para usando intervalos de números
for + range
range -> range(start, stop, step)
               começo, parar, pular -> range(0, 100, 5)
OBS: O for nao depende do range e nem o range depende do for/
CUIDADO! Não usar palavras reservadas 
o ulimo valor não e impresso
"""

numeros = range(0, 110, 10)# -> step negativo(-8) tem que colocar menos em todos valores(-0, -100, -8)
for contador in numeros:# -> Pegando o valor(contador)
    print(contador)