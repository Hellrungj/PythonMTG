#MTG CARD GAME IN PYTHON BY JOHN HELLRUNG
import sys
import random

class MTG():
    def __init__(self):
        self.players = {}
        self.phases = {0:"Beginning",1:"Main",2:"Combat",3:"End"}
        self.order = []
        self.file = None
        self.turns = 0
    
    def store(self, filename="data/Log.txt"):
        self.file = open(filename, "a+")
        print("Created " + str(filename))
        
    def setup(self, names, libraries):
        # Setups the players with the names and libraries
        for i in range(len(names)):
            #self.players.append({"P" + str(i):names[i]})
            random.shuffle(libraries[i])
            # my_dict['address'] = 'Downtown'
            self.players[names[i]] = Player(names[i], libraries[i])
            
    def shuffle(self,player):
        # Shuffle the players library 
        random.shuffle(player.library)
            
    def ordering(self):
        # Choices who goes first
        players = list(self.players.keys())
        #print(players)
        order = [i for i in players]
        #print(order)
        random.shuffle(order)
        #print(order)
        self.order = order
    
    def turn(self, player):
        if player.turn == 0:
            print("First Phase")
            self.first_phase(player)
        else:
            print("Beginning Phase")
            self.beginning_phase(player)
        print("Main Phase 1")
        self.main_phase(player)
        print("Combat Phase")
        combat_phase = self.combat_phase(player)
        if combat_phase == False:
            sys.exit()
        else:
            print("Main Phase 2")
            self.main_phase(player)
            print("End Turn")
            self.end_phase(player)
            player.turn += 1
            print("{0}, Turn {1} Over".format(player.name,player.turn))
    
    def first_phase(self, player):
        # The player draws seven card from their library
        for i in range(7):
            self.draw(player)
        print(player.name + " Hand: " + str(player.hand))
        print(player.name + " Lib: " + str(player.library))
        print(player.name + " Num Library: " + str(len(player.library)))
        
    def draw(self, player):
        # Draws from the deck and adds to hand
        # print("Hand: " + str(player.hand))
        # print("Lib: " +  str(player.library))
        player.hand.append(player.library[0])
        player.library.pop(0)
        
    def discard(self, player):
        # Discard a card from the hand to discard pile
        # print("Discard: " + str(player.hand))
        # print("Hand: " +  str(player.library))
        player.graveyard.append(player.hand[0])
        player.hand.pop(0)
        
    def untap(self, player):
        pass
        
    def beginning_phase(self, player):
        try:
            self.draw(player)
        except:
            print("You lose! Out of cards")
            sys.exit() #Quits the game
        if len(player.hand) >= 7:
            for i in range(len(player.hand) - 7):
                self.discard(player)
        self.untap(player)

    def status(self, player):
        print("-STATUS-")
        print("-Life: {0}".format(player.life))
        print("-Hand: {0}".format(player.hand))
        print("-Num Library: {0}".format(len(player.library)))        
        print("-Num Graveyard: {0}".format(len(player.graveyard)))

    def main_phase(self, player):
        self.status(player)
    
    def combat_phase(self, player):
        self.status(player)
        #player.life = player.life - 1 #Testing reasons
        return(self.lose_win(player)) 
    
    def end_phase(self, player):
        pass
        
    def lose_win(self, player):
        if len(list(self.players.keys())) == 1:
            print("Win, {}".format(player.name))
            return(False)
        else:
            if player.life == 0:
                print("Game Over, {0}".format(player.name))
                self.players.pop(str(player.name))
                return(False)
        return(True)
 
class Player():
    def __init__(self, name, library):
        self.name = name
        self.life = 20
        self.hand = []
        self.field = []
        self.mana = []
        self.library = library
        self.graveyard = []
        self.turn = 0
    