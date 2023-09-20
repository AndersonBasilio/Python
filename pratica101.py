# Variáveis livres + nonlocal(locals, globals)
# print(global)
#def fora(x):
 #   a = x

#    def dentro():
        #print(locals())
#        print(dentro.__code__.co_freevars)
#        return a
#    return dentro

#dentro1 = fora(10)
#dentro2 = fora(20)

#print(dentro1())
#print(dentro2())

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna

concatena = concatenar('a')
print(concatena('b'))
print(concatena('c'))
print(concatena('d'))