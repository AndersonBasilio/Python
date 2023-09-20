# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def nao_aceito_zero(divisor):
        if divisor == 0:
            raise ZeroDivisionError('Voce esta tentando dividir por zero')
        return True

def deve_ser_int_ou_float(numero):
       tipo_numero = type(numero)
       if not isinstance(numero, (float, int)):
            raise TypeError(
                  f'"{numero}" deve ser int ou float.'
                  f'"{tipo_numero.__name__}" enviado.'
            )
       return True

def divide(numero, divisor):
    deve_ser_int_ou_float(numero)
    deve_ser_int_ou_float(divisor)
    nao_aceito_zero(divisor)
    return numero / divisor
    
print(divide(8, 'l'))