import random
outdated_cards=[]
total_cards=10
num_cards_to_be_dealt = 5

def deal_cards():
    global characters
    characters=[{'character_name': 'Neymar', 'power_0': 91, 'power_1': 90, 'power_2':100,'power_3': 115},
                {'character_name': 'Luka Modric', 'power_0': 75, 'power_1': 52,  'power_2': 82,'power_3': 76},
                {'character_name': 'James Rodriguez', 'power_0': 55, 'power_1': 69,  'power_2': 70,'power_3': 70},
                {'character_name': 'Kylian Mbappe', 'power_0': 82, 'power_1': 102, 'power_2': 95,'power_3': 85},
                {'character_name': 'Oliver Giroud', 'power_0': 65,'power_1': 61, 'power_2': 55,'power_3': 78},
                {'character_name': 'Cristiano Ronaldo', 'power_0': 98, 'power_1': 91, 'power_2': 102,'power_3': 100},
                {'character_name': 'Shkodran Mustafi', 'power_0': 25, 'power_1': 35, 'power_2': 42,'power_3': 68 },
                {'character_name': 'Alexis Sanchez', 'power_0': 57, 'power_1': 65, 'power_2': 79,'power_3': 69},
                {'character_name': 'Mohammed Salah', 'power_0': 93, 'power_1': 99,  'power_2': 90,'power_3': 95},
                {'character_name': 'Lionel Messi', 'power_0': 100, 'power_1': 102, 'power_2': 119,'power_3': 99 }]
    # Shuffling characters now
    random.shuffle(characters)
    # Shuffled cards dealed among players
    player_one.cards=characters[0:5]
    
    player_two.cards=characters[5:]

def create_player():
    global player_one, player_two, p1, p2
    p1=input("Name of Player 1: ")
    p2=input("Name of Player 2: ")
    player_one=Player(p1)
    player_two=Player(p2)

def roll_dice():    
    player_one_roll = random.randint(1,6)
    player_two_roll = random.randint(1,6)
    print(p1 + " : ",player_one_roll)
    print(p2 + " : ",player_two_roll)
    if (player_one_roll == player_two_roll):
        print("Dice value same..Roll the Dice Again!")
        roll_dice()
    elif (player_one_roll > player_two_roll):
        print(p1 + " goes first")
        player_one.has_next_move = True      
    else:
        print(p2 + " goes first")
        player_two.has_next_move = True

def display_cards():
    print(p1 + " cards: ", player_one.cards[0])
    print(p2 + " cards: ", player_two.cards[0])

def god_spell():
    
    if player_one.has_next_move:
        num_cards_playertwo=len(player_two.cards)
        card_position=input("There are "+str(num_cards_playertwo)+" cards in total..Please choose position")
        popped_card=player_two.cards.pop(int(card_position)-1)
        player_two.cards=[popped_card] + player_two.cards
        # return player_two.cards
    elif player_two.has_next_move:
        num_cards_playerone = len(player_one.cards)
        card_position=input("There are "+str(num_cards_playerone)+" cards in total..Please choose position")
        popped_card=player_one.cards.pop(int(card_position)-1)
        player_one.cards=[popped_card] + player_one.cards
        # return player_one.cards
    else:
        return None

def resurrect_spell(player_res_turn):
    if player_res_turn == 1:
        res_card = random.choice(outdated_cards)
        player_one.cards = [res_card] + player_one.cards
        # return player_one.cards
    elif player_res_turn == 2:
        res_card = random.choice(outdated_cards)
        player_two.cards = [res_card] + player_two.cards
        # return player_two.cards
    else:
        return None

def battle_cards():

    if player_one.has_next_move:
        print(p1 + " cards :", player_one.cards[0])
    else:
        print(p2 + " cards :", player_two.cards[0])
 
    if player_one.cards[0]["power_"+str(my_choice)] > player_two.cards[0]["power_"+str(my_choice)]:
        display_cards()
        print(p1 + " won this round")
        player_one.has_next_move = True
        player_two.has_next_move = False
    else:        
        display_cards()
        print(p2 + " won this round")
        player_two.has_next_move = True
        player_one.has_next_move = False


def display_points():
    print(p1 + " points ", player_one.points)
    print(p2 + " points ", player_two.points)

def calculate_points():
            
    if player_one.cards[0]["power_"+str(my_choice)] > player_two.cards[0]["power_"+str(my_choice)]:
        player_one.add_point()
    else: 
        player_two.add_point()
    
def outdated_deck():
    global outdated_cards
    outdated_top_cards=[player_one.cards[0],player_two.cards[0]]
    outdated_cards=outdated_cards+outdated_top_cards
    print("Outdated Deck")
    print(outdated_cards)

class Player():
    def __init__(self, player_name):
        self.name = player_name
        self.cards = []
        self.is_god_spell_available = True
        self.is_resurrect_spell_available = True
        self.player_number = 1
        self.points = 0
        self.has_next_move = False

    def add_point(self):
        self.points += 1


print(" WELCOME TO THE CARD GAME ")
print( "Player Names: ")
create_player()
print("Cards being equally distributed")
deal_cards()
print("Roll the dice")
roll_dice()

while len(player_one.cards) > 0 or len(player_two.cards) > 0:

    if player_one.has_next_move:
        spell_selection_r = input(p1 + " use spells? (press r for RESURRECT or n for NO)")
        if spell_selection_r == "r":
            if len(outdated_cards) > 0:

                if player_one.is_resurrect_spell_available:
                    resurrect_spell(1)
                    print(p1 + " RESURRECT spell used!")
                    # display_cards()
                    player_one.is_resurrect_spell_available = False
                    spell_selection_r = input(p2 + " use spells? (press r for RESURRECT or n for NO)")
                    if spell_selection_r =='r':
                        if player_two.is_resurrect_spell_available:
                            resurrect_spell(2)
                            print(p2 + " RESURRECT spell used!")
                            # display_cards()
                            player_two.is_resurrect_spell_available = False
                            print(p1 + " cards: ", player_one.cards[0])
                            my_choice = input(p1 +" Enter the power number for battle?")
                            battle_cards()
                        else:
                            print(p2 + " No RESURRECTS left!")
                            # display_cards()
                            print(p1 + " cards: ", player_one.cards[0])
                            my_choice = input(p1 +" Enter the power number for battle?")
                            battle_cards()
                    elif spell_selection_r == 'n':
                        print(p1 + " cards: ", player_one.cards[0])
                        my_choice = input(p1 +" Enter the power number for battle?")
                        battle_cards()  
                else:
                    print("No RESURRECTS left!")
                    continue
            else:
                print("Outdated Deck is empty!")
                continue
        elif spell_selection_r == "n":
            print(p1 + " cards: ", player_one.cards[0])
            spell_selection_g = input(p1 + " use GODSPELL? (press g for GODSPELL or n for NO)")
            if spell_selection_g == "g":

                if player_one.is_god_spell_available:
                    print(p1 + " cards: ", player_one.cards[0])
                    god_spell()
                    print(p1 + " GODSPELL spell used!")
                    player_one.is_god_spell_available = False
                                   
                    choice = input(p2 + " press r to use resurrect OR b to continue with battle ")
                    if choice == 'r':
                        if player_two.is_resurrect_spell_available:
                            if len(outdated_cards) > 0:

                                print(p2 + " RESURRECT spell used!")
                                resurrect_spell(2)
                                player_two.is_resurrect_spell_available = False
                                # print(player_two.cards)
                                choice = input(p1 + " do you want to battle with the resurrected card or with the previously selected card? Press r for res, p for prev ")

                                if choice == 'p':
                                    popped_card=player_two.cards.pop(1)
                                    player_two.cards=[popped_card] + player_two.cards
                                    print(p1 + " cards: ", player_one.cards[0])
                                    my_choice = input(p1 + " Enter the power number for battle?")
                                    battle_cards()
                                elif choice == 'r':
                                    print(p1 + " cards: ", player_one.cards[0])
                                    my_choice = input(p1 + " Enter the power number for battle?")
                                    battle_cards()
                            else:
                                print("Outdated deck is empty!")
                                continue
                        else:
                            print(p2 + " You have no RESURRECTS left")
                            print(p1 + " cards: ", player_one.cards[0])
                            my_choice = input(p1 + " Enter the power number for battle?")
                            battle_cards()
                    elif choice == 'b':
                        print(p1 + " cards: ", player_one.cards[0])
                        my_choice = input(p1 + " Enter the power number for battle?")
                        battle_cards()                     
                else:
                    print("No GODSPELLS left!")
                    continue
                    
            elif spell_selection_g == "n":

                spell_selection_r = input(p2 + " use spells? (press r for RESURRECT or n for NO)")
                if spell_selection_r == 'r':
                    if player_two.is_resurrect_spell_available:

                        if len(outdated_cards) > 0:
                            
                            resurrect_spell(2)
                            player_two.is_resurrect_spell_available = False
                            print(p2 + " RESURRECT spell used!")
                            # display_cards()
                            # print(p2 + " cards: ", player_one.cards[0])
                            my_choice = input(p1 + " Enter the power number for battle?")
                            battle_cards()

                        else:
                            print("Outdatd deck is empty!")
                            continue
                    else:
                        print(p2 + " You have no RESURRECTS left")
                        print(p1 + " cards: ", player_two.cards[0])
                        my_choice = input(p1 + " Enter the power number for battle?")
                        battle_cards()

                elif spell_selection_r =='n':

                    print(p1 + " cards: ", player_one.cards[0])
                    my_choice = input(p1 + " Enter the power number for battle?")
                    battle_cards()

                else:
                    print("Invalid Input")
                    continue
                
            else:
                print("Invalid Input")
                continue
        else:
            print("Invalid Input")
            continue
        

    elif player_two.has_next_move:
        spell_selection_r = input(p2 + " use spells? (press r for RESURRECT or n for NO)")
        if spell_selection_r == "r":
            if len(outdated_cards) > 0:
            
                if player_two.is_resurrect_spell_available:
                    resurrect_spell(2)
                    print(p2 + " RESURRECT spell used!")
                    player_two.is_resurrect_spell_available = False
                    # display_cards()
                    spell_selection_r = input(p1 + " use spells? (press r for RESURRECT or n for NO)")
                    if spell_selection_r =='r':
                        if player_one.is_resurrect_spell_available:
                            resurrect_spell(1)
                            print(p1 + " RESURRECT spell used!")
                            # display_cards()
                            player_one.is_resurrect_spell_available = False
                            print(p2 + " cards: ", player_two.cards[0])
                            my_choice = input(p2 +" Enter the power number for battle?")
                            battle_cards()
                        else:
                            print(p1 + " No RESURRECTS left!")
                            print(p2 + " cards: ", player_two.cards[0])
                            my_choice = input(p2 +" Enter the power number for battle?")
                            battle_cards()
                    elif spell_selection_r == 'n':
                        print(p2 + " cards: ", player_two.cards[0])
                        my_choice = input(p2 +" Enter the power number for battle?")
                        battle_cards()
                else:
                    print("No RESURRECTS left!")
                    continue
            else:
                print("Outdated deck is empty!")
                continue
        elif spell_selection_r == "n":
            print(p2 + " cards: ", player_two.cards[0])
            spell_selection_g = input(p2 + " use GODSPELL? (press g for GODSPELL or n for NO)")
            if spell_selection_g == "g":

                if player_two.is_god_spell_available:
                    god_spell()
                    print(p2 + " GODSPELL spell used!")
                    player_two.is_god_spell_available = False
              
                    choice = input(p1 + " press r to use resurrect OR b to continue with battle ")
                    if choice == 'r':
                        if player_one.is_resurrect_spell_available:

                            resurrect_spell(1)
                            print(p1 + " RESURRECT spell used!")
                            player_one.is_resurrect_spell_available = False
                            # display_cards()
                            choice = input(p2 + " do you want to battle with the resurrected card or with the previously selected card? Press r for res, p for prev")

                            if choice == 'p':
                                popped_card=player_one.cards.pop(1)
                                player_one.cards=[popped_card] + player_one.cards
                                print(p2 + " cards: ", player_two.cards[0])
                                my_choice = input(p2 + " Enter the power number for battle?")
                                battle_cards()
                            elif choice == 'r':
                                print(p2 + " cards: ", player_two.cards[0])
                                my_choice = input(p2 + " Enter the power number for battle?")
                                battle_cards()
                        else:
                            print(p1 + " No RESURRECTS left")
                            print(p2 + " cards: ", player_two.cards[0])
                            my_choice = input(p2 + " Enter the power number for battle?")
                            battle_cards()
                    elif choice == 'b':
                        print(p2 + " cards: ", player_two.cards[0])
                        my_choice = input(p2 + " Enter the power number for battle?")
                        battle_cards()
                    else:
                        print("Invalid Input!")
                        continue                                    
                else:                  
                    print("No GODSPELLS left!")
                    continue
            elif spell_selection_g == "n":
                
                spell_selection_r = input(p1 + " use spells? (press r for RESURRECT or n for NO)")
                if spell_selection_r == 'r':
                    if player_one.is_resurrect_spell_available:

                        if len(outdated_cards) > 0:
                            
                            resurrect_spell(1)
                            player_one.is_resurrect_spell_available = False
                            print(p1 + " RESURRECT spell used!")
                            print(p2 + " cards: ", player_two.cards[0])
                            my_choice = input(p2 + " Enter the power number for battle?")
                            battle_cards()

                        else:
                            print("Outdated deck is empty!")
                            continue
                    else:
                        print(p1 + "No RESURRECTS left!")
                        print(p2 + " cards: ", player_two.cards[0])
                        my_choice = input(p2 + " Enter the power number for battle?")
                        battle_cards()

                elif spell_selection_r =='n':

                    print(p2 + " cards: ", player_two.cards[0])
                    my_choice = input(p2 + " Enter the power number for battle?")
                    battle_cards()

                else:
                    print("Invalid Input!")
                    continue
                
            else:
                print("Invalid Input!")
                continue
        else:
            print("Invalid Input!")
            continue                  

    print("Calculating the points ")
    calculate_points()
    display_points()
    outdated_deck()
    player_one.cards=player_one.cards[1:]
    player_two.cards=player_two.cards[1:]

    if (len(player_one.cards) > 0 or len(player_two.cards) > 0):
        print("NEXT ROUND")
        if player_one.has_next_move==True:
            print("As "+ p1 +" won the last round "+ p1 +" starts this round")
            player_one.has_next_move=True
        else:
            print("As "+ p2 +" won the last round "+ p2 +" starts this round")
            player_two.has_next_move=True

if (len(player_one.cards) == 0 or len(player_two.cards) == 0):
    print("GAME OVER")
    print(p1 + " points: ", player_one.points)
    print(p2 + " points: ", player_two.points)
    if player_one.points > player_two.points:
        print(p1 + " won the game.")
    elif player_one.points == player_two.points:
        print("It's a draw.")
    else:
        print(p2 + " won the game.")