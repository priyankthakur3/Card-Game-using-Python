import random

from Classes.Card import Card


class Deck:
    def __init__(self) -> None:
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def __str__(self) -> str:
        s = ""
        for i in range(len(self.cards)):
            s += i * " " + str(self.cards[i]) + "\n"
        return s

    def shuffle(self):
        n_cards = len(self.cards)
        for i in range(n_cards):
            j = random.randrange(0, n_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def isEmpty(self):
        return not len(self.cards)

    def pop_card(self):
        if self.isEmpty():
            return None
        else:
            return self.cards.pop()

    def deal(self, hands, n_cards=52):
        n_players = len(hands)
        for i in range(n_cards):
            if self.isEmpty():
                break

            card = self.pop_card()
            current_player = i % n_players
            hands[current_player].add_card(card)
