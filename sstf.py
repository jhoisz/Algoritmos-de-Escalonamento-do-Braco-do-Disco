# SSTF
def sstfFunction(posInicial, posicoes):
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