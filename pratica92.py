# (Parte 1) Try, except, else e finally

#a = 18
#b = 0
#c = a / b

try:
    a = 18
    b = 0
    #print(b[0])
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')

except ZeroDivisionError:
    print('Dividiu por Zero.')
    
except NameError:
    print('Variavel b não está definida.')

except (TypeError, IndexError):
    print('TypeError + IndexError.')

except Exception:
    print('ERRO DESCONHECIDO.')
print('Continuar')