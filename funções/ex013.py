'''
Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve
receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é
20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.
'''

def desenha_moldura(lin = 1, col = 1):
    for i in range(1, lin + 1):
        for j in range(1, col + 1):
            if i == 1 or i == lin:
                if j == 1:
                    print('+', end='')
                elif j == col:
                    print('+')
                else:
                    print('-', end='')
            elif col > j > 1:
                print(' ', end='')
            if j == 1:
                if lin > i > 1:
                    print('|', end='')
            elif j == col:
                if lin > i > 1:
                    print('|')


if __name__ == '__main__':
    while True:
        try:
            linha = int(input('Quantas linhas deseja (máx 20)? '))
            while linha < 3 or linha > 20:
                linha = int(input('Digite um valor válido (máx 20): '))
            coluna = int(input('Quantas colunas deseja (máx 20)? '))
            while coluna < 3 or coluna > 20:
                coluna = int(input('Digite um valor válido (máx 20): '))
        except:
            print('valor inválido, tente novamente!')
        else:
            desenha_moldura(linha, coluna)
            break
