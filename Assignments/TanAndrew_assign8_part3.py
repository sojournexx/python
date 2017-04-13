#Andrew Tan, 4/12, Section 010, Part 3

import random

#Define possible cards and associated values
cards  = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts', '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts', 'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', '10 of Diamonds', '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', '5 of Diamonds', '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 'Ace of Diamonds', 'King of Diamonds', 'Queen of Diamonds', 'Jack of Diamonds', '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs', 'Ace of Clubs', 'King of Clubs', 'Queen of Clubs', 'Jack of Clubs', '10 of Spades', '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades', '4 of Spades', '3 of Spades', '2 of Spades', 'Ace of Spades', 'King of Spades', 'Queen of Spades', 'Jack of Spades']
values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10]

#First deal
player_hand = []
player_points = 0
for i in range(2):
    index = random.randint(0, len(cards))
    player_hand.append(cards[index])
    player_points += values[index]
print("Player hand: {} is worth {}".format(player_hand, player_points))

#Subsequent deals
while player_points < 21:
    option = str.lower(input("(h)it or (s)tand? "))
    if option == "h":
        index = random.randint(0, len(cards))
        player_hand.append(cards[index])
        player_points += values[index]
        print("You drew {}".format(cards[index]))
        print("Player hand: {} is worth {}".format(player_hand, player_points))
        continue
    if option == "s":
        print()
        break

if player_points == 21:
    print("Player got 21! Blackjack!")
    winner = "Player"
elif player_points > 21:
    print("Bust!")
    winner = "Computer"

#Computer deals
elif player_points < 21:
    computer_hand = []
    computer_points = 0
    for i in range(2):
        index = random.randint(0, len(cards))
        computer_hand.append(cards[index])
        computer_points += values[index]
    print("Computer hand: {} is worth {}".format(computer_hand, computer_points))
    while computer_points < 21 and computer_points < player_points:
        index = random.randint(0, len(cards))
        computer_hand.append(cards[index])
        computer_points += values[index]
        print("Computer drew {}".format(cards[index]))
        print("Computer hand: {} is worth {}".format(computer_hand, computer_points))

    if computer_points == 21:
        print("Computer got 21! Blackjack!")
        winner = "Computer"
    elif computer_points > 21:
        print("Bust!")
        winner = "Player"
    else:
        winner = "Computer"

#Display winner
print("{} wins!".format(winner))
