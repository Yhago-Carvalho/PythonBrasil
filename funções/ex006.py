'''
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa
deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções:
uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M.
e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M.
ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as
vezes que desejar.
'''

def converte_hora(hora, min):
    if hora > 11:
        hora -= 12
        return f'A hora {hora + 12}:{min}, transformada em notação 12h, fica {hora}:{min} P.M.'
    else:
        if hora == 0:
            return f'A hora {hora}:{min}, transformada em notação 12h, fica {hora + 12}:{min} A.M.'
        return f'A hora {hora}:{min}, transformada em notação 12h, fica {hora}:{min} A.M.'


if __name__ == '__main__':
    while True:
        while True:
            try:
                h = int(input('Que horas? '))
                while h < 0 or h > 23:
                    print('Digite um horário válido!')
                    h = int(input('Que horas? '))
                m = int(input('Quantos minutos? '))
                while m < 0 or m > 60:
                    print('Digite um horário válido!')
                    m = int(input('Quantos minutos? '))
            except:
                print('Você digitou um horário inválido, tente novamente!')
            else:
                break
        print(converte_hora(h, m))
        resp = input('Deseja continuar? [S/N] ').strip()[0]
        if resp in 'Nn':
            break
