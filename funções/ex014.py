'''
Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a
soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
8  3  4
1  5  9
6  7  2
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza
todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais
simples que usar uma matriz 3x3.
'''


def gera_quadrado():
    '''
    -> Gera todas as combinações de soma igual a 15 com números diferentes de 1 a 9, organiza na matriz
    de modo a não se repetirem os números e que a soma de todas as linhas, colunas e diagonias seja 15.
    :return: Quadrado mágico.
    '''
    combinacoes = []
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if i + j + k == 15 and i != j and i != k and j != k:
                    combinacoes.append((i, j, k))
    for i in combinacoes:
        for j in combinacoes:
            for k in combinacoes:
                if i[0] + j[1] + k[2] == i[2] + j[1] + k[0] == i[0] + j[0] + k[0] == i[1] + j[1] + k[1] == 15:
                    if i[0] not in j and i[1] not in j and i[2] not in j:
                        print(i)
                        print(j)
                        print(k)
                        print()


if __name__ == '__main__':
    gera_quadrado()
