'''
Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string
com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo,
ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos
os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
'''

def embaralha_palavras(palavra):
    from random import randint

    n = []
    p = []
    for i in range(len(palavra)):
        x = randint(0, len(palavra) - 1)
        while x in n:
            x = randint(0, len(palavra) - 1)
        n.append(x)
        p.append(palavra[x])
    return ''.join(p)


if __name__ == '__main__':
    print(embaralha_palavras(input('Digite uma palavra: ').upper()))
