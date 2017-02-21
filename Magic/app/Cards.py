class Card():
    def __init__(self):
        self.name = " "
        self.cost = []
        self.types = {0:"land",1:"creature",2:"artifact",3:"enchantment",
                    4:"planeswalker",5:"instant",6:"sorcery"} 
        self.colors = {0:"Colorless",1:"White",2:"Blue",3:"Red",4:"Green",
                    5:"Black"}
        
class Creature():
    def __init__(self):
        self.typing = ["Vampire"]
        self.current_type = None
        self.power = 0
        self.toughness = 0 
        self.tapped = 0
        self.effect = []
        
    def attack(self):
        pass
    
    def defend(self):
        pass
        
class Land():
    def __init__(self):
        self.tapped = 0
        self.effect = []
        
    def spend(self):
        self.tapped = 1
        
    def renew(self):
        self.tapped = 0
        
class Artifact():
    def __init__(self):
        self.tapped = 0
        self.effect = []
        
class Enchantment():
    def __init__(self):
        self.equipment_type = ["creature"]
        self.equiped = 0
        self.effect = []
    
class Planeswalker():
    def __init__(self):
        self.loyalty = 0 
        self.tapped = 0
        self.abilities = []
    
class Instant():
    def __init__(self):
        self.effects = []

class Sorcery(): 
    def __init__(self):
        self.effects = []