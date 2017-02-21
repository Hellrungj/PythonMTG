#MTG CARD GAME IN PYTHON BY JOHN HELLRUNG

import random

class MTG():
    def __init__(self):
        self.players = {}
        self.phases = {0:"Beginning",1:"Main",2:"Combat",3:"End"}
        self.order = []
        self.file = None
        self.turn = 0
    
    def store(self, filename="Log.txt"):
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
        self.order = self.players.keys()
        random.shuffle(self.order)
    
    def first_turn(self, player):
        # The player draws seven card from their library
        for i in range(7):
            #print("Hand: " + str(player.hand))
            #print("Lib: " +  str(player.library))
            player.hand.append(player.library[0])
            player.library.pop(0)
        print(player.name + " hand: " + str(player.hand))
        print(player.name + " lib: " + str(player.library))
        
    def beginning_phase(self):
        pass

    def main_phase(self):
        pass
    
    def combat_phase(self):
        pass
    
    def end_phase(self):
        pass
 
class Player():
    def __init__(self, name, library):
        self.name = name
        self.life = 20
        self.hand = []
        self.field = []
        self.mana = []
        self.library = library
        self.graveyard = []
        self.turns = 0
    