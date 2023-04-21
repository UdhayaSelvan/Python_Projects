
"""Python program using class objects and functions to play black jack with the computer.
Card values are given below in a variable called "values".
The game rules are simple:
    If your card value reach above 21 when you hit, you lose (bust).
    If your card value is less than the computer's card value when you stay, you lose.
This game involves an element of financial risk and may be addictive. Please play responsibly and at your own risk"""

#importing random lib
import random
#importing "clear_output" from IPython.display lib
from IPython.display import clear_output

#assigning values to the global variables
#card deck values 
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, "Nine":9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':1}


#creating a class for cards
class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit
        


#Creating a class for the deck to deal and shuffle
class Deck():
    
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
                
    def shuffle(self):
        return random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()    


#creating a class player who can hit/stay and the value is displayed
class Player():
    
    def __init__(self):
        self.all_cards = []
        
    def hit(self,new_card):
        return self.all_cards.append(new_card)
    
    def sum_value(self):
        sums = 0
        for item in self.all_cards:
            sums += item.value
        return sums
            
    def display(self):
        print("player's cards:\n")
        for card in self.all_cards:
            print(card)
    
    def __str__(self):
        return f"{self.name} has {len(self.all_cards)} in hand "


#creating a class to keep track of the player's money
class Account():
    
    def __init__(self):
        self.balance = 100
        
    def deposit(self, add):
        self.balance += add
        return str(add)+ f"has been credited to your account. Total amount is {self.balance}"
    
    def withdraw(self, sub):
        self.balance -= sub
        return str(sub)+ f"has been deducted from your account. Total amount is {self.balance}"
    
    def __str__(self):
        return f"Total amount in the player's account is {self.balance}"


#Creating a class for the computer
class Comp():
    def __init__(self):
        self.all_cards = []
        
    def hit(self,new_card):
        return self.all_cards.append(new_card)
    
    def sum_value(self):
        sums = 0
        for item in self.all_cards:
            sums += item.value
        return sums
    
    def display(self,show):
        print("\ncomputer's cards:\n")
        for card in self.all_cards:
            if card == self.all_cards[0]:
                if show == 'OFF':
                    print("##################")
                elif show == 'ON':
                    print(card)
            else:
                print(card)
            
    
    def __str__(self):
        return f"Computer has {len(self.all_cards)} in hand "


#initializing variables outside the loop
rounds = 0
game_on = True
player_account = Account()

#outer loop with conditions to start the game
while game_on:
    
    #calling functions 
    player = Player()
    computer = Comp()
    new_deck = Deck()
    new_deck.shuffle()
    
    #Deal two cards
    for x in [1,2]:
        player.hit(new_deck.deal_one())
        computer.hit(new_deck.deal_one())
    
    #if player's balance is less than zero, discontinue the game and startover.
    if player_account.balance <= 0:
        print("Insufficient balance to continue. Please start over!")
        game_on = False
        break
    
    #main game loop
    while True:

        #get bet amount input from the player
        print("Player please choose a bet: ")
        player_bet = int(input(f"Your balance: {player_account.balance}. Please enter your bet: "))


        if type(player_bet) != int:
            print("Wrong choice. Please enter an integer!")
            continue
            
        elif player_account.balance < player_bet:
            print("Limit exceeded. Please choose a lesser amount.")
            continue
        
        else:
            print(f"You placed a bet for {player_bet}")
            break
    #game play starts    
    rounds += 1 #count of the rounds
    print(f"This is round{rounds}\n")
    
    player.display() #display players cards
    print("\n"*2)
    computer.display('OFF') #hide one of the computer cards
    
    #for loop to check if the delt card is an ace. If ace then player can choose its value (either 1 or 11) 
    for card in player.all_cards:
        if card.rank == 'Ace':
            while True:
                choice_value = input("Press 'x' for value 1 and 'y' for value 11")
                if choice_value not in ['x','y']:
                    print("Wrong choice! Please try again.")
                    continue
                elif choice_value == 'x':
                    card.value = 1
                    break
                elif choice_value == 'y':
                    card.value = 11
                    break
            
    
    bust = False  #Did player bust
    plr = True #Player's turn
    
    #player's turn loop
    while plr:
        
        if player.sum_value() > 21: #player busted
            print("Computer won the game! (Bust)") 
            player_account.withdraw(player_bet)
            bust = True
            plr = False
            break
    
        else:
            print("\nPlayer's turn!")
            player_choice = input("Please choose (h)Hit or (s)Stay.")

            #if wrong choice
             if player_choice not in ['s','h']:
                print("Wrong choice try again")
                continue

            #When player choose hit or stay
            elif player_choice == 'h':
                player.hit(new_deck.deal_one())
                clear_output()
                player.display()
                computer.display('ON')

                #if the player gets an Ace while hitting
                if player.all_cards[-1].rank == 'Ace':
                    while True:
                        choice_value = input("Press 'x' for value 1 and 'y' for value 11")
                        if choice_value not in ['x','y']:
                            print("Wrong choice! Please try again.")
                            continue
                        elif choice_value == 'x':
                            player.all_cards[-1].value = 1
                            break
                        elif choice_value == 'y':
                            player.all_cards[-1].value = 11
                            break
                    continue

            else:
                plr = False
                break
    
    #if player's turn is done and the player did not get busted, now its computer's turn           
    if not plr and not bust:
        cmp = True #Computer's turn
    else:
        cmp = False

    #computer turn's loop
    while cmp:
        
        if computer.sum_value() > 21:
            print("player won the game! (Bust)")
            player_account.deposit(player_bet)
            bust = True
            cmp = False
            break
        
        else:
            #computer keeps hitting as long as the value is less than 18
            if computer.sum_value() < 18:
                print("\nComputer's turn!")
                computer.hit(new_deck.deal_one())
                clear_output()
                player.display()
                computer.display('ON')
                continue
                
            else:
                cmp = False
                break
    #if both not bust then check their value and see who won            
    if not bust:
        
        if player.sum_value() >= computer.sum_value():
            clear_output()
            player.display()
            computer.display('ON')
            print("Player won the game! :)")
            player_account.deposit(player_bet)

        
        else:
            clear_output()
            player.display()
            computer.display('ON')
            print("Computer won the game!")
            player_account.withdraw(player_bet)
            
    
    #a loop to continue the game (you can continue only if you have enough funds!)        
    while True:
    
        to_continue = input("Do you want to continue. Press 'Y' or 'N': ")

        if to_continue not in ['Y', 'N']:
            print("Wrong choice! Please try again.")
            continue

        elif to_continue == 'Y':
            game_on = True
            break

        else:
            game_on = False
            break
    continue

print("Game Over!!!")
