"""
Retorno das funções (return)
return -> Sempre que executamos determinada função sempre retornará uma determiado valor.
None -> Significa um não valor.
return só tem em somente métodos e função tem return também indica que irá parar a funçao.
"""

#def soma(x, y):
    #print(x + y)# Essa função nao retorna nada(None)
    #return(x + y)# Essa função retorna algum valor.
    #print(123) depois do retunr nao aparecerá nada.

def soma(x, y):
    if x > 10:
        return [10, 20] # Só podemos ter um valor por função.
    return x + y

#variavel = soma(1, 2)
#variavel = int('1')
soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11,55))
