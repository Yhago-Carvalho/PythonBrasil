'''
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
'''

def imprime_numeros(num):
    for i in range(1, num+1):
        for j in range(1, i+1):
            print(f'{j:<3}', end='')
        print()


if __name__ == '__main__':
    while True:
        try:
             n = int(input('Digite um número inteiro: '))
        except:
             print('Número inválido, tente novamente!')
        else:
             break
    imprime_numeros(n)
