import sys
from fcfs import *
from sstf import *
from elevador import *

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


print(fcfsFunction(posicaoInicial, posicoes))
print(sstfFunction(posicaoInicial, posicoes))
print(elevador(posicaoInicial, limite, posicoes))