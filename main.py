
'''
CPE 551B: Engineering Python 

Name: Priyank Thakur
CWID: 20009546

Fall 2022 Project: Implement Card Game

Rules of Game:
Each Game consists of either 2,4,13,26 Players
Dealer method is going to divide and deal cards
to all Hands.
Player who plays highest card wins current round
Until all cards in players hand are played, round
continues
And Player with highest wins, wins the game

Working:
When program starts executing, its going to ask 
for number of players followed by name of each 
Hand, once game starts, program is going to ask each
player to input index of card from Cards in Hand
and at each round display winner of current round
At end of game it will display winner players name

Rank for Deck:
Spade > Hearts > Diamonds > Clubs
'''

import sys
from Classes.CardGame import CardGame

print("Starting Card Game")
c1 = CardGame()
c1.playCards()

print("\nBye!!")
