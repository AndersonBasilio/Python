# Tipos built-in, documentação, tipo imútaveis, metodos de string

string = 'Anderson' # O valor que é atribuido a variavel é imutaveis
outra_variavel = string # Estamos copiando o valor da variavel string para outra_variavel
# Imutaveis que vimos: STR, INT, FLOAT, BOOL -> São todos imutaveis 

print(string) # String sem alteração. 
#print(outra_variavel) # String com alteração.

#string = 'ABC' # Não conseguimos mudar o valor da variavel.

print('Podemos fazer a mudança criando outra variavel.')
outra_variavel = (f'{string[:3]}ABC{string[4:]}')
print(outra_variavel)
print(string.capitalize())
print(string.upper())
print(string.zfill(20))# Completara com 0 até o número 20 for atingido contando com a letra.
