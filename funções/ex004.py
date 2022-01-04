'''
Faça um programa, com uma função que necessite de um argumento.
A função retorna o valor de caractere ‘P’, se seu argumento for
positivo, e ‘N’, se seu argumento for zero ou negativo.
'''

def positivo_ou_negativo(num):
    return 'P' if num>0 else 'N'


if __name__ == '__main__':
    while True:
        try:
             n1 = input('Digite um número: ').replace(',', '.').strip()
             n1 = float(n1)
        except:
             print('Você digitou algum número inválido, tente novamente!')
        else:
             break
    print(positivo_ou_negativo(n1))
