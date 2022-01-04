'''
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
'''

def soma(n1, n2, n3):
    return f'{n1 + n2 + n3:.2f}'


if __name__ == '__main__':
    while True:
        try:
             n1 = input('Digite um número: ').replace(',', '.')
             n1 = float(n1)
             n2 = input('Digite um número: ').replace(',', '.')
             n2 = float(n2)
             n3 = input('Digite um número: ').replace(',', '.')
             n3 = float(n3)

        except:
             print('Você digitou algum número inválido, tente novamente!')
        else:
             break
    print(soma(n1, n2, n3))
