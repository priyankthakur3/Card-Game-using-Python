from Classes.Deck import Deck

from Classes.Hand import Hand


class CardGame():
    def __init__(self, hands_list=None) -> None:
        self.deck = Deck()      # initialize Deck
        self.deck.shuffle()     # shuffle Cards in Deck
        self.drawed_cards_list = []     # played cards list
        self.hands_list = []    # hands list

        total_players = int(input("Enter Number of Players: "))

        if total_players not in [2, 4, 13, 26]:
            print("Please Enter Number of players in range of 2,4,13,26")
            exit()

        for i in range(0, total_players):
            # initialize hands object for every player
            self.hands_list.append(
                Hand(input("Enter Player {} Name: ".format(i+1))))

        # Deal Cards to players
        self.deck.deal(self.hands_list, 12)

    def display_hand_cards(self, index) -> str:
        '''Wrapper function to display cards in Hand of player'''
        print(self.hands_list[index])

    def winner_current_turn(self) -> int:
        '''
        Function to return index of winner hand at end of round
        '''
        index_player = 0

        # Set highest card to 0th card from stack and iterate through remaining
        # to find highest card index
        highest_card = self.drawed_cards_list[0]

        for i in range(0, len(self.drawed_cards_list)):
            if self.drawed_cards_list[i] > highest_card:
                # Compare Cards and if greater update max card
                highest_card = self.drawed_cards_list[i]
                index_player = i

        # Clear out Played Cards for next round

        self.drawed_cards_list = []

        return index_player

    def printWins_all(self):
        '''Function to displays Rounds Won by Players'''
        print("Round Win Summary:")
        print("Player\tWins")
        print("-"*30)
        for i in range(0, len(self.hands_list)):
            print(self.hands_list[i].name + "\t" +
                  str(self.hands_list[i].round_wins))

    def getGameWinner(self):

        # build list which contains wins of all hands
        wins_list = list(map(lambda hand: hand.getWins(), self.hands_list))
        # set initial index as 0 and maxWins
        index = 0
        maxWins = wins_list[index]
        tie = 0
        tie_indicator = False

        for i in range(0, len(wins_list)):
            # iterate through entire list and update index if maxWins is less
            if maxWins < wins_list[i]:
                # maxWins is less than next Wins value
                # update index maxValue, tieIndicator
                index = i
                maxWins = wins_list[i]
                tie_indicator = False

            elif maxWins == wins_list[i]:
                # if initial maxWins is equal to next Wins value
                # then set tie_indicator to Tru
                tie_indicator = True

            elif maxWins > wins_list[i]:
                # if initial maxWins is greater than next Wins value
                # then set tie_indicator to False
                # this is avoid incase intial maxValue if highest and
                # there are tie in next values
                tie_indicator = False

        # incase of tie return -1 else return index of highest wins by player
        if not tie_indicator:
            return index
        else:
            return -1

    def playCards(self):
        '''
        Function to start Game Execution
        '''
        print("Begin")
        rounds = 0
        # get maximum card present in a hand
        max_cards = max(list(map(len, self.hands_list)))

        # loop until there no cards left in hand of player
        while max_cards:
            print("\nRound {}".format(rounds+1))
            for i in range(0, len(self.hands_list)):
                print("\n"+str(self.hands_list[i].name)+"'s Turn\n")
                # Display Cards present in Hand
                print(self.hands_list[i])

                while True:
                    card_index = int(
                        input("Enter Index of Card to be played from Hand: "))
                    # Add Card to played card list
                    try:
                        self.drawed_cards_list.append(
                            self.hands_list[i].pop_card(card_index-1))
                        break
                    except IndexError:
                        print("Invalid Index Number please Enter Correct Index")

                print("\n"+self.hands_list[i].name + " Played '" +
                      str(self.drawed_cards_list[-1])+"'")

            # get index of player with highest card from current round
            winner_index = self.winner_current_turn()
            print("\n"+"#"*50)
            print("Winner of Current round is: " +
                  str(self.hands_list[winner_index].name))
            print("#"*50+"\n")
            self.hands_list[winner_index].round_wins += 1
            rounds += 1
            max_cards = max(list(map(len, self.hands_list)))

            self.printWins_all()

        winner_index = self.getGameWinner()

        if winner_index < 0:
            print("\n"+"#"*50)
            print("Game is Tied")
            print("#"*50+"\n")
        else:
            print("\n"+"#"*50)
            print("Winner of Game is: "+self.hands_list[winner_index].name)
            print("#"*50+"\n")
