'''
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada
no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
'''
GASOLINA = 'Gasolina'
ÁLCOOL = 'Álcool'
DIESEL = 'Diesel'

class bombaCombustível():
    GASOLINA = 'Gasolina'
    ÁLCOOL = 'Álcool'
    DIESEL = 'Diesel'
    combustíveis = [{GASOLINA: 6.49}, {ÁLCOOL: 4.99}, {DIESEL: 5.42}]
    def __init__(self, tipoCombustível=GASOLINA, valorLitro=combustíveis[0][GASOLINA], quantCombustivel=20):
        self.tipoCombustível = tipoCombustível
        self.valorLitro = valorLitro
        self.quantCombustivel = quantCombustivel

    def abastecerPorValor(self, quantV):
        quantLitros = quantV / self.valorLitro
        self.quantCombustivel += quantLitros
        return f'{quantLitros:.2f} litros'

    def abastecerPorLitro(self, quantL):
        quantValor = quantL * self.valorLitro
        self.quantCombustivel += quantL
        return f'R${quantValor:.2f}'

    def alteraValor(self, novoValor):
        self.valorLitro = novoValor
        return self.valorLitro

    def alteraCombustível(self, novoComb):
        self.tipoCombustível = novoComb
        return self.tipoCombustível

    def alterarQuantidadeCombustivel(self, novaQuant):
        self.quantCombustivel = novaQuant
        return self.quantCombustivel

if __name__ == '__main__':
    bomba = bombaCombustível()
    print(bomba.valorLitro)
    print(bomba.tipoCombustível)
    print(bomba.alteraCombustível(ÁLCOOL))
    print(bomba.quantCombustivel)
    print(bomba.abastecerPorLitro(20))
    print(bomba.quantCombustivel)
    print(bomba.abastecerPorValor(100))
    print(bomba.quantCombustivel)


