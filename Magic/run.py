import time
from app import *

def get_file(filename):
    file = open(filename, "r")
    contents = file.read()
    contents_ls = []
    string = ""
    for i in contents:
        if i == "\n" or i == "EOF":
            contents_ls.append(string)
            string = ""
        else:
            string = string + str(i)
    return contents_ls

def introduction():
    libraries = []
    names = []
    I1 = input("How many players?")
    for i in range(int(I1)):
        I2 = input("What is your name, player " + str(i+1) + "?")
        names.append(I2)
        I3 = input("Would you like to import a library file? (Y/N)")
        if I3.lower() == "y":
            I4 = input("What is the name of the file?")
            libraries.append(get_file(I4))
        else:
            introduction()
    player_data = [names,libraries]
    return player_data

def main():
    Game = 0
    while True:
        game_one = MTG()
        game_one.store()
        game_one.file.write("Starting New Game: " + str(time.time()) + ", " + str(time.clock()) + "\n")
        names,libraries = introduction()
        game_one.file.write("Players: " + str(names) + "\n")
        game_one.setup(names,libraries)
        game_one.file.write("Setup: " + str(time.time()) + ", " + str(time.clock()) + "\n")
        game_one.ordering()
        game_one.first_turn(game_one.players[game_one.order[0]])
        game_one.file.write("Turn " + str(game_one.turn) + ": " + str(time.time()) + ", " + str(time.clock()) + "\n")
    
        IEND = raw_input("Would you like to play again?(Y/N)")
        if IEND.lower() == "n":
            game_one.file.write("Games: " + str(Game) + "\n")
            game_one.file.write("Ended: " + str(time.time()) + ", " + str(time.clock()) + "\n")
            game_one.file.close()
            break
        Game += 1
    
main()    