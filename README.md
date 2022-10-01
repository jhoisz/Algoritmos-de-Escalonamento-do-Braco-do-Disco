# 💿 Escalonamento do braço do disco

## Sobre
Programas que simulam os seguintes algoritmos de escalonamento do braço de disco:

- FCFS (First Come, First Serve)
- SSTF
- Elevador: O braço se movimenta inicialmente em direção ao cilindro mais
externo do disco.

## Como executar:

Baixe o projeto, entre no terminal e execute o comando:
```shell
python3 main.py < entrada.txt
```

**Descrição da entrada:** A entrada é composta por uma série de números inteiros, um
por linha, indicando primeiro o número do último cilindro no disco (os cilindros variam
de 0 até este número), o cilindro sobre o qual a cabeça de leitura está inicialmente
posicionada e a sequência de requisições de acesso.

**Exemplo de entrada:**

```
199
53
98
183
37
122
14
124
65
67
```
**Descrição da saída:** A saída é composta por linhas contendo a sigla de cada um dos
três algoritmos e a quantidade total de cilindros percorridos pela cabeça de leitura para
atender todas as requisições de acesso ao disco.

```
FCFS 640
SSTF 236
ELEVADOR 299
```
