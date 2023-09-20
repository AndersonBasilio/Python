# (Parte 2) try, except, else e finally

#a = 18
#b = 0
#c = a / b

try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')

except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    
except NameError:
    print('Variavel b não está definida.')

except (TypeError, IndexError) as error:
    print('TypeError + IndexError.')
    print('Mensagem:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO.')

print('Continuar')