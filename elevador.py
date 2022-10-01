def elevador(posInicial, lim, posicoes):
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