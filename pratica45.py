"""
Imprecisão dos números de ponto flutuante + round e decimal (Decimal)
Imprecisão de ponto flutuante
"""
import decimal # Importando uma biblioteca

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2

print(numero_3)
print(f'{numero_3:.2f}')# Formatando com string.
print(round(numero_3,2)) # Formatando usando o round dentro do print.