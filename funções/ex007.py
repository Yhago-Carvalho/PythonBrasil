'''
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação
de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso
e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este
valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução
o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um
valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório
do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago
é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso,
cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
'''

def valorPagamento(prestacao, atraso=0):
    if atraso != 0:
        prestacao *= (1.03 + 0.001 * atraso)
    return prestacao


def relatorio(prestacoes: list):
    print('_' * 35)
    print(f'{"RELATÓRIO DO DIA":^30}')
    print('_' * 35)
    print(f'{"PRESTAÇÕES":<13}{"VALOR TOTAL"}')
    print('-'*26)
    print(f'{len(prestacoes):^13}R${sum(prestacoes):.2f}')

if __name__ == '__main__':
    p = []
    while True:
        try:
            v = input('Valor da prestação: R$').strip().replace(',', '.')
            if float(v) == 0:
                break
            p.append(float(v))
            a = int(input('Quantos dias em atraso? '))
        except:
            print('Valor inválido, tente novamente!')
        else:
            print(f'Valor da prestação: {valorPagamento(p[-1], a):.2f}')
            print('-' * 30)
        if float(v) == 0:
            break
    relatorio(p)
