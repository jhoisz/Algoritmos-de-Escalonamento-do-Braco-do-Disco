import sys

# limite do braço do disco
limite = None
# posição inicial do disco
posicaoInicial = None
# lista das demais posições
posicoes = []

# tratamento de entrada
for linha in sys.stdin:
    linhaFormatada = int(linha.replace('\n', ''))
    if (limite == None):
        limite = linhaFormatada
    elif (posicaoInicial == None):
        posicaoInicial = linhaFormatada
    else:
        posicoes.append(linhaFormatada)

# FCFS
def fcfsFunction(posInicial):
    fcfs = 0
    pos = posicoes.copy()
    # para cada posição, é feito o calculo da distancia
    for x in pos:
        fcfs += abs((posInicial - x))
        posInicial = x  
    return 'FCFS ' + str(fcfs)

# SSTF
def sstfFunction(posInicial):
    tmp = posInicial
    pos = posicoes.copy()    
    sstf = 0

    def distanceTo(atual):
        return abs(atual - tmp)

    for y in range(len(pos)):
        # varre a lista de posicoes e retorna as distancias
        newAbsList = list(map(distanceTo, pos))
        # retorna o menor valor da lista, ou seja, a posição mais próxima
        minValue = min(newAbsList)
        # retorna o índice desse valor mínimo
        index = newAbsList.index(minValue)
        # remove esse valor mínimo
        tmp = pos[index]
        pos.remove(tmp)
        # incrementa nas movimentações do braço do disco
        sstf += minValue
    return 'SSTF ' + str(sstf)


# tmp = posicaoInicial    
# tmpPosicoes = posicoes


def elevador(posInicial, lim):
    # cria cópia das posicoes no disco de forma ordenada
    pos = posicoes.copy()
    pos.sort()
    # variavel para guardar movimentacoes no algoritmo do elevador
    elevador = 0
    # variavel temporaria que inicia com a posicao onde a cabeça do disco está posicionada
    tmp = posInicial

    # lista para percorrer outro direcao de requisicoes
    posDir2 = []

    # Para cada posicao na lista de posicoes
    for p in pos:
        # verifica se esta dentro do limite da lista, e se é maior que a posicao anterior
        if p < lim and p > tmp:
            # incrementa ena variavel elevador a quantidade de movimentacoes
            elevador+= abs(p-tmp)
            # a variavel temporaria passa a ser a variavel da posicao atual
            tmp = p
        else:
            # caso contrario, incrementa na lista de posicoes que estao na outra direcao do braco do disco
            posDir2.append(p)

    # ordena a lista de posicoes na outra direcao do braco do disco de forma reversa, decrescente
    posDir2.sort(reverse=True)
    # realiza as mesma operacoes para contar os movimentos
    for p in posDir2:
        elevador+= abs(p-tmp)
        tmp = p

    return "ELEVADOR "+str(elevador)