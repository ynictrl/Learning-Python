"""
CONSTANTE = 'Variaveis' que não vão mudar
Muitas condições no  mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distancia onde o radar pega

vel_passou_radar_1 = velocidade > RADAR_1
pos_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) # \ pula linha
multado_radar_1 = pos_passou_radar_1 and vel_passou_radar_1

if vel_passou_radar_1:
    print('Velocidade do carro passou do radar 1!')

if pos_passou_radar_1:
    print('Posição do carro passou do radar 1!')

if multado_radar_1:
    print('O carro foi multado!')