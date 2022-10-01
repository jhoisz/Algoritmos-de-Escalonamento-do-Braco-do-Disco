# FCFS
def fcfsFunction(posInicial, posicoes):
    fcfs = 0
    pos = posicoes.copy()
    # para cada posição, é feito o calculo da distancia
    for x in pos:
        fcfs += abs((posInicial - x))
        posInicial = x  
    return 'FCFS ' + str(fcfs)
