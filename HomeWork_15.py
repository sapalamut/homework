import random

class Card:
    def __init__(self, value, name, suit):
        self.suit = suit
        self.value = value
        self.name = name

    def card_face(self):
        print(f"{self.name} {self.suit}")

class Player:
    def __init__(self, name, wallet):
        self.name = name
        self.card_deck = []
        self.wallet = wallet
        self.current_stake = 0

    #take card
    def take_card(self, card):
        self.card_deck.append(card)
    # current stake
    def stake_value(self):
        sum = 0
        for c in self.card_deck:
            sum += c.value
        return sum
    # drop cards to start a new round
    def drop_cards(self):
        self.card_deck = []
        self.current_stake = 0

    def set_player_won(self, won, amount):
        if won:
            self.wallet += amount
        else:
            self.wallet -= self.current_stake
        self.drop_cards()

    def make_bet(self, stake):
        if stake > 0 and stake <= self.wallet:
            self.current_stake = stake
            print(f"Your stake is: {self.current_stake}")
            print(f'Your wallet balance is: {self.wallet - self.current_stake}')
            return True
        else:
            print("You don't have enough balance!")
            return False

    def show_cards(self):
        for c in self.card_deck:
            c.card_face()

class Dealer:
    def __init__(self):
        self.player_1 = Player("Jacky", 100)
        self.player_2 = Player("Chan", 100)
        self.cards = []
        self.generate_cards()

    def generate_cards(self):
        card_suits = ["Diamonds", "Hearts", "Spades", "Clubs"]

        for v in range(2, 15):
            for suit in card_suits:
                name = ""

                if v < 11:
                    name = str(v) +" " + "of"
                elif v == 11:
                    name = "Jack " + "of"
                elif v == 12:
                    name = "Queen " + "of"
                elif v == 13:
                    name = "King " + "of"
                elif v == 14:
                    name = "Ace " + "of"

                value = v
                if v > 10:
                    value = 10

                self.cards.append(Card(value, name, suit))

    def check_bust(self):
        if self.player_1.stake_value() > 21:
            print("Player 1 lost")
            return True
        elif self.player_2.stake_value() > 21:
            print("Player 2 lost")
            return True
        else:
            return False

    def draw_card(self):
        try:
            card = random.choice(self.cards)
            self.cards.remove(card)
            return card
        except IndexError:
            print("Cards are over")
            exit()

    def draw_extra_card(self, player):
        while True:
            player_move = input("Do you want to take a card: (Yes/No) ")

            if player_move == "Yes":
                player.take_card(self.draw_card())
                player.show_cards()

                if self.check_bust():
                    print("Bust!")
                    return False

            elif player_move == "No":
                return True

    def get_stake(self):
        stake = -1
        while (stake == -1):
            try:
                stake = int(input(f"What is your stake ? "))
                break
            except ValueError:
                stake = -1
                print("It's not a number")

        return stake

    def play(self, player):
        print(f"{player.name} cards")
        player.show_cards()

        if not player.make_bet(self.get_stake()):
            return

        return not self.draw_extra_card(player)

    def check_who_win(self):
        bank = self.player_1.current_stake + self.player_2.current_stake
        player_1_won = True

        if  self.player_1.stake_value() > 21:
            # player_2 wins
            player_1_won = False
        elif self.player_2.stake_value() > 21:
            # player_1 wins
            pass
        else:
            if self.player_1.stake_value() > self.player_2.stake_value():
                # player_1 wins
                pass
            else:
                # player_2 wins
                player_1_won = False

        self.player_1.set_player_won(player_1_won, bank)
        self.player_2.set_player_won(not player_1_won, bank)

    def play_round(self):
        print("Round Started!\n\n")

        self.player_1.take_card(self.draw_card())
        self.player_1.take_card(self.draw_card())

        player_1_bust = self.play(self.player_1)

        if not player_1_bust:
            self.player_2.take_card(self.draw_card())
            self.player_2.take_card(self.draw_card())

            self.play(self.player_2)

        self.check_who_win()

dealer = Dealer()

while True:
    dealer.play_round()
