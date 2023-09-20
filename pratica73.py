# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}

#s1 = set() # Vazio
#s1 = {'Luiz', 1, 2, 3} # Com dados
#print(s1)

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

#s1 = {1, 2, 3, 3, 3, 3, 3, 1}
#l1 = [1, 2, 3, 3, 3, 3, 3, 1]
#s1 = set(l1)
#l2 = list(s1)
#s1 = {1, 2, 3}
#for numero in s1:
#   print(numero)

# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Anderson')
s1.add(1)
s1.update(('Olá Mundo', 1, 2, 3, 4))# Tupla
#s1.clear() Limpa o set
s1.discard('Olá Mundo')
s1.discard('Anderson')
#print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s4 = s1 & s2
s5 = s1 - s2 # Se inverte s5 = s2 - s1 a diferença será {4}
s6 = s1 ^ s2

print('União ', s3)
print('Intersecção ', s4)
print('Diferença ', s5)
print('Diferença Simétrica ', s6, '\n')