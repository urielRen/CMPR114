# Uriel Renteria
# 3/ 28/23

# Project 1
import random

def main():
    deck = create_deck()
    player1 = hand(deck, 0)   
    player1Next = 'y'
    print()

    player2 = hand(deck, 0)
    player2Next = 'y'
    print()

    game = False

    while game == False:
        player1Next = input('Player 1 do you want a card? (Y/ N): ')

        if player1Next == 'y' or player1Next == 'Y':
            player1 += hand(deck, player1)

        player2Next = input('Player 2 do you want a card? (Y/ N): ')

        if player2Next == 'y' or player2Next == 'Y':
            player2 += hand(deck, player2)

        print()

        if player1 == 21 and player2 > 21 or player1 == 21 and player2 < 21 or player2 > 21:
            print(f'Player 1 won with a {player1}!')
            game = True
        elif player2 == 21 and player1 > 21 or player2 == 21 and player1 < 21 or player1 > 21:
            print(f'Player 2 won with a {player2}!')
            game = True
        elif player1 == 21 and player2 == 21:
            print('The game is tie!')
            game = True

def create_deck():
    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,

            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,
            
            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,
    
            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}

    return deck

def hand(deck, hand):
    hand_value = 0

    card = random.choice(list(deck))
    print(card)
    
    if hand < 17 and deck[card] == 1 or deck[card] == 1 and hand + 11 < 21:
        hand_value = deck[card] + 10
    else:
        hand_value = deck[card]

    del deck[card]
    hand += hand_value
    print(f'Value of this hand: {hand}')

    return hand_value

if __name__ == '__main__':
    main()