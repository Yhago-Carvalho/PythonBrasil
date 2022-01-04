'''
Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o
custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto
sobre vendas.
'''
def somaImposto(taxaImposto, custo):
    return f'O custo do produto com impostos é R$ {custo * (1 + taxaImposto / 100):.2f}'


if __name__ == '__main__':
    while True:
        try:
             c = input('Digite o custo do produto: R$ ').replace(',', '.').strip()
             c = float(c)
             taxa = input('Qual a taxa de imposto em %? ').replace(',', '.').strip()
             taxa = float(taxa)
        except:
             print('Você digitou algum número inválido, tente novamente!')
        else:
             break
    print(somaImposto(taxa, c))
