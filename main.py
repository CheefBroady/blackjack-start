############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import random
from art import logo
from replit import clear

user_cards = []
computer_cards = []
repeats = 2
play_again = True

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(logo)

def deal_card():
  rand_idx = random.randint(0, len(cards)-1)
  print(rand_idx)
  return cards[rand_idx]

def add_card(player_list, card):
  player_list.append(card)
  # print(f"{card} was added")

def sum_cards(player_list):
  cards_sum = 0
  for value in player_list:
    cards_sum += value
  return cards_sum

def replace_as(players_list):
  temp_user_cards = []
  for value in players_list:
    if value != 11:
      temp_user_cards.append(value)
    else:
      temp_user_cards.append(1)
  return temp_user_cards

def return_str_value(players_list):
  new_value = ""
  for value in players_list:
    new_value += str(value)
    new_value += ", "
  return new_value[:-2]




play_game = input("Do you want play a game of Blackjack? Type 'y' or 'n': ")

if play_game == 'Y' or play_game == 'y':
  for nr in range(repeats):
    add_card(user_cards, deal_card())
  users_actual_value = sum_cards(user_cards)
  print(f"Your cards: [{user_cards[0]}, {user_cards[1]}], current score: {users_actual_value}")
  add_card(computer_cards, deal_card())
  print(f"Computer's first card: {computer_cards[0]}")
  if users_actual_value == 21:
    print("You won!!!!")
  else:
    while play_again:
      play_again = input("Type 'y' to get another card, type 'n' to pass: ")
      if play_again == 'y' or play_again == 'Y':
        add_card(user_cards, deal_card())
        users_actual_value = sum_cards(user_cards)
        print(f"Your cards: [{return_str_value(user_cards)}], current score: {users_actual_value}")
        add_card(computer_cards, deal_card())
        computers_actual_value = sum_cards(computer_cards)
        print(f"Computer's cards: [{return_str_value(computer_cards)}], current score: {computers_actual_value}")
        if computers_actual_value == 21:
          print("You lose!!!")
          play_again = False
        elif users_actual_value > 21:
          if sum_cards(replace_as(user_cards)) > 21:
            print("You lose!!!")
            play_again = False
      else:
        play_again = False


print("Good Bye")

print(return_str_value(user_cards))




