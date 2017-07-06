import sys

if __name__ == "__main__":
    # Check if the user provided all of the 
    # arguments. The script name counts
    # as one of the elements, so we need at 
    # least three, not fewer.
    if len(sys.argv) < 2:
        print ("Usage: ")
        print (" python run.py <players> <name>")
        print (" e.g. python run.py 2 John,Luke")
        sys.exit()
        NUM_players = sys.argv[1]
        PLAYER_name1 = sys.argv[2]
        PLAYER_name2 = sys.argv[3]
        print("Players: [{0}], Names: [{1},{2}]".format(NUM_players,PLAYER_name1,PLAYER_name2))
        