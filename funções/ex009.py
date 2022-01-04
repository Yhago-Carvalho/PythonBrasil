'''
Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado.
Por exemplo: 127 -> 721.
'''

def reverso_numero(num):
    return str(num)[::-1]


if __name__ == '__main__':
    while True:
        try:
            n = int(input('Digite um número: '))
        except:
            print('Digite um inteiro válido!')
        else:
            break
    print(f'O reverso de {n} é {reverso_numero(n)}')
