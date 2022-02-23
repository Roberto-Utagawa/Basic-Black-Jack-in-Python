import itertools, random

class CARD(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class DECK(object):
    def __init__(self):
        self.cards = []
        self.amount = 0
        self.deckShuffle()

    # INSERT A CARD INTO THE DECK #
    def push(self, card):
        self.cards.append(card)

    # REMOVE A CARD FROM THE DECK #
    def pop(self):
        return self.cards.pop()

    # SHUFFLE DE DECK #
    def deckShuffle(self):
        temp = list(itertools.product(range(1, 14), ['Ouros', 'Copas', 'Espadas', 'Paus']))
        random.shuffle(temp)
        for i in temp:
            carta = CARD(i[0], i[1])
            self.push(carta)

class PLAYER(object):
    def __init__(self):
        self.cardsQuantity = 0
        self.hand = []
        self.balance = 1000

    def push(self, card):
        self.hand.append(card)
        self.cardsQuantity += 1

    def pop(self):
        self.cardsQuantity -= 1
        return self.hand.pop()

class GAME(object):
        def __init__(self):
            self.players = 0
            self.player = []
            self.bet = 0
            self.playerBet = []
            self.deck = DECK()
        # BLACK JACK RULES #
        def rules(self):
            print('\n\n')
            print('============ BLACK JACK ===========')
            print('\nRules:\n')
            print('- The game consistis in reach the value 21')
            print('- The player who has the sum of the cards closer than 21 will win the round')
            print('- If the sum of the cards exceed 21, the player will lose the round')
            print('- Each player starts with 1000 balance, if the balance reach 0, the player will be disqualifiqued')
            print('- In case of drawn, the bets will be returned for each player\n')
            print('===================================\n')
        # PUSH PLAYERS #
        def playerPush(self, amount):
            for i in range(amount):
                self.players += 1
                self.player.append(PLAYER())
        # DEFINE THE BET #
        def betInsert(self, player, bet):
            if bet == 0 or bet > self.player[player].balance:
                bet = self.player[player].balance
            self.bet += bet
            self.playerBet[player] = bet
            self.player[player].balance -= bet
        # PAY THE BET TO THE WINNER #
        def betPay(self, player):
            self.player[player].balance += self.bet
            self.bet = 0
        # RESET THE BET #
        def betClear(self):
            self.bet = 0
            for i in range(self.players):
                self.playerBet[i] = 0
        # TAKE CARDS IF POSSIBLE#
        def playerTakeCard(self, index):
            if self.playerBet[index] > 0:
                take = 1
                while take == 1:
                    take = int(input('Player {}, you have {} cards, type 1 to take more cards, or 0 to stop: ').format(index, self.player[index].cardsQuantity))
                    if take == 1:
                        self.players[index].push(self.deck.pop)

def blackJack():
    game = GAME()
    game.rules()
    game.playerPush(int(input('Select the number of players: ')))
    continue_ = True

    while #possivel jogar? and continue_ == True:
        for i in range(game.players):
            if game.player[i].balance > 0:
                bet = int(input('Player {}, choose your bet: ').format(i))
                game.betInsert(i, bet)
        bigger = -1
        for i in range(game.players):
            game.playerTakeCard(i)
            #VERIFICAR MAO
            #COLOCAR O MAIOR, SE HOUVER EMPATE DEVOVLER BETS
            # RESETAR BARALHO
            # RESETAR BETS
            # RESETAR CARTAS PLAYERS
        continue_ = int(input('Press 1 to continue playing, 0 to stop: '))

blackJack() 




'''''
# INSERT THE CARDS INTO THE DECK #

# CREATE THE PLAYERS #
def players():
    qnt = int(input('\nDigite a quantidade de jogadores: '))
    jogadores = []
    for i in range(0, qnt):
        jogador = JOGADOR()
        jogadores.append(jogador)
    print('\n===================================')
    return jogadores

# TAKE CARDS TO EACH PLAYER #
def take_cards(jogadores, deck):
    for i in range(len(jogadores)):
        print('\nJOGADOR {}:'.format(i))
        continue_ = True
        while continue_ == True:
            print('\nJogador {}, voce tem um total de {} cartas'.format(i, jogadores[i].quantidade))
            continue_ = int(input('Digite 1 para pegar uma carta ou 0 para sair: '))

            if continue_ == True:
                jogadores[i].quantidade += 1
                jogadores[i].push(deck.pop())
        print('\n===================================')

# CHECK IF IS POSSIBLE PLAY #
def check_balance(jogadores):
    for i in range(len(jogadores)):
        if jogadores[i].saldo  <= 0:
            return False
    return True

def bet(jogadores):
    bet_ = 0
    for i in range(len(jogadores)):
        bet1 = input(int('Player: {}, select the bet: '))
        if bet1 > jogadores[i].saldo or bet <= 0:
            bet1 = jogadores[i].saldo
        jogadores[i].saldo -= bet1
        bet_ += bet1
    return bet_

def check_game(jogadores):
    card = -1
    bigger = -1
    index_b = -1

    for i in range(len(jogadores)):
        total = 0
        while jogadores[i].quantidade != 0:
            card = jogadores[i].pop()
            total += card.valor
            jogadores[i].quantidade -= 1
        if total <= 21 and total > bigger:
            index_b = i
            bigger = total

    return index_b

def main():
    print('\n\n============ BLACK JACK ===========')
    jogadores = players()

    while check_balance(jogadores):
        index = -1
        deck = BARALHO()
        deck_push(deck)
        bet_ = bet(jogadores)
        take_cards(jogadores, deck)
        index = check_game(jogadores)
        jogadores[index].saldo += bet
    # anunciar quem venceu

main()
'''''