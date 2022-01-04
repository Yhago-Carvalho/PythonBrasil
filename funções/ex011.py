'''
Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva
uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso
a data seja inválida.
'''

def conversao_datas(data):
    mes = {'01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril', '05': 'Maio', '06': 'Junho',
          '07': 'Julho', '08': 'Agosto', '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'}
    data = data.split('/')
    print(f'{data[0]} de {mes[data[1]]} de {data[2]}')


def validacao_datas():
    while True:
        try:
            dd = int(input('Dia: '))
            while dd<1 or dd>31:
                dd = int(input('Digite um dia entre 01 e 31: '))
            mm = int(input('Mês: '))
            while mm<1 or mm>12:
                mm = int(input('Digite um mês entre 01 e 12: '))
            aaaa = int(input('Ano: '))
            while aaaa<1:
                aaaa = int(input('Digite um ano válido: '))
        except:
            print('Dados inválidos inserido, tente novamente!')
        else:
            return f'{dd:0>2}/{mm:0>2}/{aaaa:0>4}'


if __name__ == '__main__':
    data = validacao_datas()
    conversao_datas(data)
