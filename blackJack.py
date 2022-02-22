import itertools, random

class CARTA(object):
    def __init__(self, valor, nipe):
        self.valor = valor
        self.nipe = nipe

class BARALHO(object):
    def __init__(self):
        self.cartas = []

    def push(self, carta):
        self.cartas.append(carta)

    def pop(self):
        return self.cartas.pop()

    def empity(self):
        return self.cartas == []

class JOGADOR(object):
    def __init__(self):
        self.quantidade = 0
        self.mao = []
        self.saldo = 1000

    def push(self, carta):
        return self.mao.append(carta)

    def pop(self):
        return self.mao.pop()

# INSERT THE CARDS INTO THE DECK #
def deck_push(deck):
    temp = list(itertools.product(range(1, 14), ['Ouros', 'Copas', 'Espadas', 'Paus']))
    random.shuffle(temp)
    for i in temp:
        carta = CARTA(i[0], i[1])
        deck.push(carta)

def players():
    qnt = input('\nDigite a quantidade de jogadores: ')
    jogadores = []
    for i in range(0, qnt):
        jogador = JOGADOR()
        jogadores.append(jogador)
    return jogadores

def main():
    print('============ BLACK JACK ===========')

    deck = BARALHO()
    deck_push(deck)
    jogadores = players()

    for i in range(len(jogadores)):
        continue_ = True
        while continue_ == True:
            print('\nJogador {}, voce tem um total de {} cartas'.format(i, jogadores[i].quantidade))
            continue_ = input('Digite 1 para pegar uma carta: ')

            if continue_ == True:
                jogadores[i].quantidade += 1
                jogadores[i].push(deck.pop())
        print('\n===================================')

    for i in range(len(jogadores)):
        print('a')

print("A")
main()