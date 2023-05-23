"""
Variaveis Constantes e Complexidade do Codigo
CONSTANTE = Variaveis que nunca vai mudar
muitas condições no mesmo if(ruim) -> and, or, not irá ficar dificil de entender
Contagem complexidade(ruim) -> Blocos de codigos dentro de blocos tem que ser simples.
"""

velocidade = 60 # Velociade atual do carro
local_carro = 100 # Local em que o carro esta na estrada

# Variaveis com letras maiusculas não ira mudar
RADAR_1 = 60
LOCAL_1 = 100 #Carro precisa passar no local que esta o radar - o range 99Km
RADAR_RANGE = 1 # 101 o range

if velocidade > RADAR_1:
    print('Velocidade carro passou do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and\
    local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1:
    print('Carro multado em radar 1.')
# Varias coisas ruins nesse codigo acima.

print('==' * 18)
# Boas Praticas


velocidade = 60
local_carro = 100
RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
local_carro  <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and \
velocidade_carro_passou_radar_1

if velocidade_carro_passou_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1.')

if carro_multado_radar_1:
    print('Carro multado em radar 1.')
