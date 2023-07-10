# try, except, else e finally

try:
    print('ABRIR O ARQUIVO')
    # 8 / 0 

except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('Dividiu por zero.')
    
except IndexError as error:
    print('IndexError.')
except (NameError, ImportError):
    print('NameError, ImportError.')
else:
    print('Não deu erro') 

finally:# Sempre será executado, mesmo que ocorra um erro.
    print('FECHAR ARQUIVO') 
 