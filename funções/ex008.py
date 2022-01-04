'''
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
'''

def conta_digitos(num):
    return len(str(num))


if __name__ == '__main__':
    while True:
        try:
            n = int(input('Informe um número: '))
        except:
            print('Inform eum inteiro válido!')
        else:
            break
    print(f'A quantidade de dígitos no número informado é: {conta_digitos(n)}')