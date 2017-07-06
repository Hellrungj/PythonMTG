import time
from app import *

def get_file(filename):
    file = open(filename, "r") #Opens file
    contents = file.read() #Reads the file
    contents_ls = [] #Grabs the content in the file
    string = " "
    for i in contents: #Loops through each line
        if i == "\n" or i == "EOF": #Loops through each character
            contents_ls.append(string) #Adds line to list
            string = " "
        else:
            string = string + str(i) #Adds character to list creating a line 
    return contents_ls 

def introduction():
    libraries = []
    names = []
    I1 = input("How many players?")
    #I1 = 1
    for i in range(int(I1)):
        #I2 = input("What is your name, player " + str(i+1) + "?")
        I2 = "John{0}".format(i)
        names.append(I2)
        #I3 = input("Would you like to import a library file? (Y/N)")
        I3 = "y"
        if I3.lower() == "y":
            #I4 = input("What is the name of the file?")
            I4 = "data/ListOfCards.txt"
            libraries.append(get_file(I4))
        else:
            introduction()
    #print("Names: {0}".format(names))
    player_data = [names,libraries]
    return player_data

def main():
    game_one = MTG() #Create Class Intaince
    game_one.store() #Creates a Log File
    game_one.file.write("Starting New Game: {0}, {1}\n".format(time.time(),
                                                               time.clock())) 
    #Writes to the Log file
    names,libraries = introduction() # Adds the players names and decks to the game
    #print(names)
    print("_____________________________________") #For testing reasons
    game_one.file.write("Players: {0}\n".format(names))
    #Writes to the Log file
    game_one.setup(names,libraries) #Setup up both players hands
    game_one.file.write("Setup: {0}, {1}\n".format(time.time(), time.clock()))
    #Writes to the Log file
    game_one.ordering() #Reorders the both players cards
    while True: #Play the main game
        for player in game_one.order: #Set order for the players
            print(" TURN: ({0}) ".format(game_one.players[player].name)) #Display player name
            game_one.turn(game_one.players[player]) #Player takes their turn
            game_one.turns += 1 #Adds one to the turn counter
            game_one.file.write("Turn {0}:{1},{2}\n".format(game_one.turn, time.time(),
                                                            time.clock()))
            #Writes to the Log file
            print("_____________________________________") #For testing reasons
            time.sleep(1) #For testing reasons
    
if __name__ == "__main__":
    Game = 0 # Game counter
    while True: # Runs main game
        main() #Runs "main' fuction
        IEND = input("Would you like to play again?(Y/N)") #Ask use if they want to play again
        IEND = "N" #For testing reasons 
        if IEND.lower() == "n": #Quit the game if no
            game_one.file.write("Games: {0}\n".format(Game))
            #Writes to the Log file
            game_one.file.write("Ended: {0},{1}".format(time.time(), time.clock()))
            #Writes to the Log file
            game_one.file.close() # Close opened log file
            break
        Game += 1 # Adds one to game counter
    print("Total Games {}".format(Game)) #Print total of games
  
  