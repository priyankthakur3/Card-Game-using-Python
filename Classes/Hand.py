from Classes.Deck import Deck


class Hand(Deck):
    def __init__(self, name="") -> None:
        self.cards = []
        self.index = 0
        self.name = name
        self.round_wins = 0

    def check_is_empty(self) -> bool:
        '''Check if there are no cards in Hand'''
        return len(self.cards) == 0

    def __len__(self) -> int:
        return len(self.cards)

    def isEmpty(self) -> bool:
        return not len(self.cards)

    def add_card(self, card) -> None:
        '''Add Card to Hand List'''
        self.cards.append(card)

    def pop_card(self, index):
        '''Function to return Card from passed index'''
        if index >= len(self.cards):
            raise IndexError("Invalid Card Number! Please check input")
        else:
            return self.cards.pop(index)

    def getWins(self) -> int:
        '''Function to return wins of Players'''
        return self.round_wins

    def __str__(self) -> str:
        s = "Hand of " + self.name
        if self.isEmpty():
            return s + " is empty"
        s += " contains \n-----------------------------------------\n" + \
            Deck.__str__(self)
        return s
