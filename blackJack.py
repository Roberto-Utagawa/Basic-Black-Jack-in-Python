from ast import While
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
        self.amount += 1
        self.cards.append(card)

    # REMOVE A CARD FROM THE DECK #
    def pop(self):
        self.amount -= 1
        return self.cards.pop()

    # SHUFFLE DE DECK #
    def deckShuffle(self):
        while self.amount > 0:
            self.pop()

        temp = list(itertools.product(range(1, 14), ['Ouros', 'Copas', 'Espadas', 'Paus']))
        random.shuffle(temp)

        for i in temp:
            carta = CARD(i[0], i[1])
            self.push(carta)

        self.amount = 52

class PLAYER(object):
    def __init__(self):
        self.cardsQuantity = 0
        self.hand = []
        self.balance = 1000

    def push(self, deck):
        self.hand.append(deck.pop())
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
                self.playerBet.append(0)

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
                    take = int(input('Player {}, you have {} cards, type 1 to take more cards, or 0 to stop: '.format(index, self.player[index].cardsQuantity)))
                    if take == 1:
                        self.player[index].push(self.deck)

        # GIVE BACK THE BET TO EACH PLAYER #
        def betBack(self):
            for i in range(self.players):
                self.player[i].balance += self.playerBet[i]
            self.bet = 0

        def betsReset(self):
            for i in range(self.players):
                self.playerBet[i] = 0

        def IsPossible(self):
            players = 0
            for i in range(self.players):
                if self.player[i].balance > 0:
                    players += 1
            if players > 1:
                return True
            return False
        
        def winner(self):
            bigger = -1
            index = -1
            draw = False
            for i in range(self.players):
                if self.player[i].balance > bigger:
                    bigger = self.player[i].balance
                    index = i
                    draw = False
                elif self.player[i].balance == bigger:
                    draw = True
            if draw:
                print('ITS A DRAW !!!!')
            else:
                print('CONGRATULATIONS PLAYER {}, YOU WIN!!!'.format(index))

def blackJack():
    game = GAME()
    game.rules()
    game.playerPush(int(input('Select the number of players: ')))
    continue_ = True

    while continue_ == True and game.IsPossible():
        for i in range(game.players):
            if game.player[i].balance > 0:
                print('Player {}, you balance is {}'.format(i, game.player[i].balance))
                bet = int(input('Player {}, choose your bet: '.format(i)))
                game.betInsert(i, bet)
        bigger = -1
        index = -1
        draw = 0
        for i in range(game.players):
            sum = 0
            game.playerTakeCard(i)
            while game.player[i].cardsQuantity > 0:
                card = game.player[i].pop()
                sum += card.value
            if sum <= 21 and sum > bigger:
                bigger = sum
                index = i
                draw = 0
            elif sum == bigger:
                draw = 1
            print('Player {}, the sum is: {}'.format(i, sum))
        if draw == 1 or index == -1:
            print('Its a draw')
            game.betBack()
        else:
            print('Player {} win this round'.format(index))
            game.betPay(index)

        game.deck.deckShuffle()
        game.betsReset()
        continue_ = int(input('Press 1 to continue playing, 0 to stop: '))

    game.winner()

blackJack() 