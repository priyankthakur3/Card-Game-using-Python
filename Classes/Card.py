class Card:
    suit_list = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_list = ["None", "Ace", "2", "3", "4", "5", "6",
                 "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2) -> None:
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        return (self.rank_list[self.rank] + " off " + self.suit_list[self.suit])

    def __eq__(self, __o: object) -> bool:
        return (self.rank == __o.rank and self.suit == __o.suit)

    def __gt__(self, __o: object) -> bool:
        if self.suit > __o.suit:
            return True
        elif self.suit == __o.suit:
            if self.rank > __o.rank:
                return True

        return False
