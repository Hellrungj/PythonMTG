######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your names
# Username: heggens             TODO: Change this to your usernames
#
# Assignment: T1: Choose Your Own Adventure
# Purpose: To create a choose-your-own-adventure style game.
# Each "twist" in the story is from a different group. The resulting story
# will either be incoherently random, or entertainingly "Mad Lib" like.
# Either way, it should be fun!
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#   Inspired by https://www.cs.hmc.edu/twiki/bin/view/CS5/Week0ChoiceProblem

######################################################################
import time

delay = 1.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False

# TODO Ask the user to input their name. Make it adventurous, such as:
# TODO "What do they call you, worthy adventurer? "

username = "Scott"          # Replace this line with user input
#################################################################
# The following is the first part of the story. Don't change this.
print()
print("Welcome,", username, ", to the labyrinth")
time.sleep(delay)
print("Before you lies two paths.")
print("One path leads to treasures of unimaginable worth.")
print("The other, certain death. Choose wisely.")
print()
time.sleep(delay * 2)
print("You are in a dark cave. You can see nothing.")
print("Staying here is certainly not wise. You must find your way out.")
print()
time.sleep(delay)
direction = input("Which direction would you like to go? [North/South/East/West]")

########################################################

# An example chapter, to start your user off on your adventure
# Author: Scott Heggen
if direction == "North":
   print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
   time.sleep(delay)
elif direction == "South":
   print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
   time.sleep(delay)
   print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
   print("Running seems like a good idea now. But... it's really, really dark.")
   print()

   speed = int(input("How many steps would you like to take?"))
   if speed < 5:
       print("It appears you are more scared of the dark than a bear.")
       time.sleep(delay*2)
       print("Your fears were well-placed. The bear was hibernating, and your quiet exit pays off.")
   else:
       print("You run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
       time.sleep(delay)
       print("He eats you. You are delicious.")
       dead = True
else:
   print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
   time.sleep(delay)


# It is unusual to quit a program early like I do below. However, it serves us very well for this assignment,
# because it ends our story upon death. So we will use it. The alternative is a LOT of nested if/else statements,
# which would get messy by the last group. You will need this statement after your chapter is added.
if dead == True:
    quit()

#########################################################################################################
# TODO Add your part of the story here. Keep in mind you may not be coming right after the example above.
# TODO don't forget the two lines of code above!

# Author: Scott Heggen          TODO Change this! right after the example above.
# TODO don't forget the two lines of code above!

# Author: Scott Heggen          TODO Jacob Beckman and Noah Dehart
import time
delay = 1.0
dead = False
print("The man is acutally Xbox Live Customer Support!")
username = input("What is your gamertag?")
##############################################################################################################
print()

print("hello,", username, ", welcome to my spaceship!!!!!!!!!!!!!! ;)")
time.sleep(delay)
print("Infront of you lies an advanced spacecraft that looks like a giant Doritos Bag TM.(Cool Ranch, cause a blue spaceship is cooler)")
print("behind you is a stinky rotten cave that no one liked anyways(must've been designed by a rookie author.)")
time.sleep(delay)
print("You have two choices, Go on the awesome space adventure! or go back to the dirty boring cave that even to this day nobody likes(nerd cave).")
time.sleep(delay*2)
print("What do you do?")
direction = input("[Awesome Space Adventure/Nerd Cave]")
##################################################################################################################
time.sleep(delay)
if direction == "Nerd Cave":
   time.sleep(delay)
   print('Do you mean "Awesome Space Adventure"?')
   direction = input("[Awesome Space Adventure/Nerd Cave]")
   if direction == "Nerd Cave":
       print('I think you mean "Awesome Space Adventure".')
   if direction == "Nerd Cave":
       print("Fine, you can go back to the dirty stinky Nerd Cave.")
       time.sleep(delay)
       wait = int(input("How many hours do you wait in the Nerd Cave?"))
       if wait >= 2:
           print("You die of boredom because you are stuck in a cave and chose a lame adventure. You should feel bad, the writer had a great adventure planned for you.(Nerd)")
           time.sleep(delay*3)
           dead= True

       else:
           print("Do you change your mind and go on the Awesome Space Adventure? [Yes/Yes]")
           if input== "Yes":
               time.sleep(delay)
               print("As you approach the spaceship and the man who claims to be Xbox Live Customer Support, you are ecstatic to go on this adventure. You've been dreaming about this for years.")
               print("You realize that your entire existence is actually fictitious and entirely made up of pixels on a screen of a laptop that belongs to a stressed out college student trying to live.")
               print("You push this thought to the back of your head and jump onto the Cool Ranch TM spaceship. It smells terrible yet still delicious. Feels like you need some Mountain Dew TM. ")
               print('''As you journey through the cosmos, your days consist of playing "Cod of Duty: Fishing Warfare."You've become an amazing quickbater and pwn all the noobs. ''')
               print("It isn't until late in your journey you realize you might not ever make it to your destination because of how vast the cosmos are and how small your human lifespan is.")
               print("Depressed you ask the pilot to take you back to the dirty rotten nerd cave. The pilot sadly obliges and returns you to Earth 15 years later.")
               print("You Continue your Journey.(Nerd Cave.)")

if direction == "Awesome Space Adventure":
   time.sleep(delay)
   print("As you approach the spaceship and the man who claims to be Xbox Live Customer Support, you are ecstatic to go on this adventure. You've been dreaming about this for years.")
   print("You realize that your entire existence is actually fictitious and entirely made up of pixels on a screen of a laptop that belongs to a stressed out college student trying to live.")
   print("You push this thought to the back of your head and jump onto the Cool Ranch TM spaceship. It smells terrible yet still delicious. Feels like you need some Mountain Dew TM. ")
   print('''As you journey through the cosmos, your days consist of playing "Cod of Duty: Fishing Warfare."You've become an amazing quickbater and pwn all the noobs. ''')
   print("It isn't until late in your journey you realize you might not ever make it to your destination because of how vast the cosmos are and how small your human lifespan is.")
   print("Depressed you ask the pilot to take you back to the dirty rotten nerd cave. The pilot sadly obliges and returns you to Earth 15 years later.")
   print("You Continue your Journey.(Nerd Cave.)")
else:
   print("You make some choice that wasn't listed and honestly sounds pretty dumb, you reconsider your choices and choose between the Awesome Space Adventure or the Nerd Cave.")






if dead == True:
   quit()

#########################################################################################################

print()
time.sleep(delay *5)
print("You wake up.......It was actually a DREAM!!")
print("You start doing normal things that you usually do...!!")
print("...However, that dream starts hunting you")
print()
time.sleep(delay*2)
myinput = input("Do you want to keep living with that dream [Y/N]")
print("You chose: " + myinput)
if myinput == "Y":
   print("You walk down to the neighboring street and suddenly think that one of your late friend is following you...")
   print("That scares you terribly to an extent that you couldn't pay attention to the road signs. ")
   print("Car is coming right behind you in an running speed of average human being")
   speed = int(input("How many minute does it take you to run 5K?"))
   if speed < 60:
       print("It looks like you can't make it")
       print()
       time.sleep(delay * 2)
       print("You're DEAD!!!! :( ")
       dead = True
   else:
       print("You are a clone of Usain Bolt,,, thank god you can run that fast")
       print("You're safe now!")
else:
   print("Go to church and talk to the priest about your nightmare")
   print(" And the priest says, my child, the Devil is trying to test your faith. ")
   print("*you get even more scared*")
   print("And the priest prays for you")
   print("You then feel relived after the prayer")
   print("You return home and the dream stops hunting you")
   print()
   time.sleep(delay *3)
   print("You're safe")
if dead == True:
   quit()
# TODO don't forget the two lines of code above!

# Author: Scott Heggen          TODO Jacob Beckman and Noah Dehart
import time
delay = 1.0
dead = False
print("The man is acutally Xbox Live Customer Support!")
username = input("What is your gamertag?")
##############################################################################################################
print()

print("hello,", username, ", welcome to my spaceship!!!!!!!!!!!!!! ;)")
time.sleep(delay)
print("Infront of you lies an advanced spacecraft that looks like a giant Doritos Bag TM.(Cool Ranch, cause a blue spaceship is cooler)")
print("behind you is a stinky rotten cave that no one liked anyways(must've been designed by a rookie author.)")
time.sleep(delay)
print("You have two choices, Go on the awesome space adventure! or go back to the dirty boring cave that even to this day nobody likes(nerd cave).")
time.sleep(delay*2)
print("What do you do?")
direction = input("[Awesome Space Adventure/Nerd Cave]")
##################################################################################################################
time.sleep(delay)
if direction == "Nerd Cave":
   time.sleep(delay)
   print('Do you mean "Awesome Space Adventure"?')
   direction = input("[Awesome Space Adventure/Nerd Cave]")
   if direction == "Nerd Cave":
       print('I think you mean "Awesome Space Adventure".')
   if direction == "Nerd Cave":
       print("Fine, you can go back to the dirty stinky Nerd Cave.")
       time.sleep(delay)
       wait = int(input("How many hours do you wait in the Nerd Cave?"))
       if wait >= 2:
           print("You die of boredom because you are stuck in a cave and chose a lame adventure. You should feel bad, the writer had a great adventure planned for you.(Nerd)")
           time.sleep(delay*3)
           dead= True

       else:
           print("Do you change your mind and go on the Awesome Space Adventure? [Yes/Yes]")
           if input== "Yes":
               time.sleep(delay)
               print("As you approach the spaceship and the man who claims to be Xbox Live Customer Support, you are ecstatic to go on this adventure. You've been dreaming about this for years.")
               print("You realize that your entire existence is actually fictitious and entirely made up of pixels on a screen of a laptop that belongs to a stressed out college student trying to live.")
               print("You push this thought to the back of your head and jump onto the Cool Ranch TM spaceship. It smells terrible yet still delicious. Feels like you need some Mountain Dew TM. ")
               print('''As you journey through the cosmos, your days consist of playing "Cod of Duty: Fishing Warfare."You've become an amazing quickbater and pwn all the noobs. ''')
               print("It isn't until late in your journey you realize you might not ever make it to your destination because of how vast the cosmos are and how small your human lifespan is.")
               print("Depressed you ask the pilot to take you back to the dirty rotten nerd cave. The pilot sadly obliges and returns you to Earth 15 years later.")
               print("You Continue your Journey.(Nerd Cave.)")

if direction == "Awesome Space Adventure":
   time.sleep(delay)
   print("As you approach the spaceship and the man who claims to be Xbox Live Customer Support, you are ecstatic to go on this adventure. You've been dreaming about this for years.")
   print("You realize that your entire existence is actually fictitious and entirely made up of pixels on a screen of a laptop that belongs to a stressed out college student trying to live.")
   print("You push this thought to the back of your head and jump onto the Cool Ranch TM spaceship. It smells terrible yet still delicious. Feels like you need some Mountain Dew TM. ")
   print('''As you journey through the cosmos, your days consist of playing "Cod of Duty: Fishing Warfare."You've become an amazing quickbater and pwn all the noobs. ''')
   print("It isn't until late in your journey you realize you might not ever make it to your destination because of how vast the cosmos are and how small your human lifespan is.")
   print("Depressed you ask the pilot to take you back to the dirty rotten nerd cave. The pilot sadly obliges and returns you to Earth 15 years later.")
   print("You Continue your Journey.(Nerd Cave.)")
else:
   print("You make some choice that wasn't listed and honestly sounds pretty dumb, you reconsider your choices and choose between the Awesome Space Adventure or the Nerd Cave.")






if dead == True:
   quit()

#########################################################################################################

print()
time.sleep(delay *5)
print("You wake up.......It was actually a DREAM!!")
print("You start doing normal things that you usually do...!!")
print("...However, that dream starts hunting you")
print()
time.sleep(delay*2)
myinput = input("Do you want to keep living with that dream [Y/N]")
print("You chose: " + myinput)
if myinput == "Y":
   print("You walk down to the neighboring street and suddenly think that one of your late friend is following you...")
   print("That scares you terribly to an extent that you couldn't pay attention to the road signs. ")
   print("Car is coming right behind you in an running speed of average human being")
   speed = int(input("How many minute does it take you to run 5K?"))
   if speed < 60:
       print("It looks like you can't make it")
       print()
       time.sleep(delay * 2)
       print("You're DEAD!!!! :( ")
       dead = True
   else:
       print("You are a clone of Usain Bolt,,, thank god you can run that fast")
       print("You're safe now!")
else:
   print("Go to church and talk to the priest about your nightmare")
   print(" And the priest says, my child, the Devil is trying to test your faith. ")
   print("*you get even more scared*")
   print("And the priest prays for you")
   print("You then feel relived after the prayer")
   print("You return home and the dream stops hunting you")
   print()
   time.sleep(delay *3)
   print("You're safe")
if dead == True:
   quit()
#######################################################################################
# Authors: Logan Owens & Brandon Wimsatt

print()
print("You wake up on the banks of a river.")
analyze = (input("Do you take a look around? [y or n]"))
print()
if analyze == "y":
   print("To the North you see a path leading into a forest.")
   time.sleep(1)
   print("To the West you see a house.")
   time.sleep(1)
   print("To the East is the River.")
   time.sleep(1)
   print("To the South is the River.")
   time.sleep(1)
   direction = input("Which direction would you like to go? [North, South, East, West]")
elif analyze == "n":
   direction = input("Which direction would you like to go? [North, South, East, West]")
else:
   print("You stand there wasting time like a college student.")
   direction = input("Which direction would you like to go? [North, South, East, West]")
if direction == "North":
   print("You walk along for 2 hours, suddenly you hear howling in the distance.")
   direction = input("Would like to keep moving? [y or n] ")
   print()
   if direction == "y":
       print("You continue along the path till you reach an opening.")
   else:
       print("A few moments pass and a wolf lashes out from your blind spot.")
       direction = input("Do you decide to fight the wolf, or do you try and run? [Fight or Run]")
       if direction == "Fight":
           force = int(input("How much force do you use in fighting the wolf?"))
           if force > 10:
               print("With the wolf cradled in your thighs you jump at least 1 foot off the ground.")
               print("With the force of a thousand warriors, you obliterate the wolf's skull.")
               time.sleep(1)
               print()
               print("Your visions blurs, you died from exerting yourself too much.")
               dead = True
           else:
               print("You pile drive the wolf breaking its neck, you continue along the path till you end at an opening")
       else:
           print("You run for a quarter mile or so until the wolf pounces once more critically wounding you.")
           time.sleep(2)
           print("You die.")
           dead = True
elif direction == "West":
       print("You enter the house, you see a living room and a flight of stairs.")
       print("You hear what sounds like a fart...?")
       print()
       direction = input("Do you go up the stairs or east into the living room? [Up or Run]")
       if direction == "Up":
           print("As you walk up the stairs a bandit jumps out tackling you causing you both to fall down the stairs.")
           direction = input("Do you choose to stay and fight or run from the house? [Fight or Run]")
           print()
           if direction == "Run":
               print("You run out of the house and hurry North.")
               print("You walk along for 2 hours, suddenly you hear howling in the distance.")
               direction = input("Would like to keep moving? [y or n] ")
               print()
               if direction == "y":
                   print("You continue along the path till you reach an opening.")
               else:
                   print("A few moments pass and a wolf lashes out from your blind spot.")
                   direction = input("Do you decide to fight the wolf, or do you try and run? [Fight or Run]")
                   if direction == "Fight":
                       force = int(input("How much force do you use in fighting the wolf?"))
                       if force > 10:
                           print("With the wolf cradled in your thighs you jump at least 1 foot off the ground.")
                           print("With the force of a thousand warriors, you obliterate the wolf's skull.")
                           time.sleep(1)
                           print("Your visions blurs, you died from exerting yourself too much.")
                           dead = True
                       else:
                           print("You pile drive the wolf breaking its neck, you continue along the path till you end at an opening")
                   else:
                       print("You run for a quarter mile or so until the wolf pounces once more critically wounding you.")
                       time.sleep(2)
                       print()
                       print("You die.")
                       dead = True
           else:
               print("More bandits come down the stairs in response to the noise.")
               print("The bandits surround you and begin stabbing and kicking you.")
               print("Several hours later after the bandits have had their fun with you, you die.")
               dead = True
       else:
           print("You run out of the house and hurry North.")
           print("You walk along for 2 hours, suddenly you hear howling in the distance.")
           direction = input("Would like to keep moving? [y or n] ")
           print()
           if direction == "y":
               print("You continue along the path till you reach an opening.")
           else:
               print("A few moments pass and a wolf lashes out from your blind spot.")
               direction = input("Do you decide to fight the wolf, or do you try and run? [Fight or Run]")
               print()
               if direction == "Fight":
                   force = int(input("How much force do you use in fighting the wolf?"))
                   if force > 10:
                       print("With the wolf cradled in your thighs you jump at least 1 foot off the ground.")
                       print("With the force of a thousand warriors, you obliterate the wolf's skull.")
                       time.sleep(1)
                       print()
                       print("Your visions blurs, you died from exerting yourself too much.")
                       dead = True
                   else:
                       print("You pile drive the wolf breaking its neck, you continue along the path till you end at an opening")
               else:
                   print("You run for a quarter mile or so until the wolf pounces once more critically wounding you.")
                   time.sleep(2)
                   print("You die.")
                   dead = True
else:
   print("You trip and hit your head falling into the river.")
   time.sleep(3)
   print("You wake up several hours later no better off than you were before.")
   print("")
if dead == True:
   quit()
#######################################################################################

######################################################################
# Author: Nathan Jose and Malachi Holden    TODO: Change this to your names
# Username: josen and holdenm           TODO: Change this to your usernames
#
# Assignment: T1: Choose Your Own Adventure
# Purpose: To create a choose-your-own-adventure style game.
# Each "twist" in the story is from a different group. The resulting story
# will either be incoherently random, or entertainingly "Mad Lib" like.
# Either way, it should be fun!
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#   Inspired by https://www.cs.hmc.edu/twiki/bin/view/CS5/Week0ChoiceProblem

######################################################################
import time

delay = 1.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False

# TODO Ask the user to input their name. Make it adventurous, such as:
# TODO "What do they call you, worthy adventurer? "

username = input("What's your name?")
#################################################################
# The following is the first part of the story. Don't change this.
print()
print("Welcome,", username, ", to the labyrinth")
time.sleep(delay)
print("Before you lies two paths.")
print("One path leads to treasures of unimaginable worth.")
print("The other, certain death. Choose wisely.")
print()
time.sleep(delay * 2)
print("You are in a dark cave. You can see nothing.")
print("Staying here is certainly not wise. You must find your way out.")
print()
time.sleep(delay)
direction = input("Which direction would you like to go? [North/South/East/West]")

########################################################

# An example chapter, to start your user off on your adventure
# Author: Scott Heggen
if direction == "North":
  print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
  time.sleep(delay)
elif direction == "South":
  print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
  time.sleep(delay)
  print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
  print("Running seems like a good idea now. But... it's really, really dark.")
  print()

  speed = int(input("How many steps would you like to take?"))
  if speed < 5:
      print("It appears you are more scared of the dark than a bear.")
      time.sleep(delay*2)
      print("Your fears were well-placed. The bear was hibernating, and your quiet exit pays off.")
  else:
      print("You run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
      time.sleep(delay)
      print("He eats you. You are delicious.")
      dead = True
else:
  print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
  time.sleep(delay)

print()
print("********************* CHAPTER 2 ***********************")
print("You enter a mineshaft.....You take a few steps and trip on a chunk of metal... ")
print("The metal seems like a rail and you can feel the track. You can see a light approaching...")
direction1=input("What do you do?\n1. Do you move towards the light in hope of escaping the dark? Press 1\n2. Do you want to run away from the light on the track? Press 2\n3. Do you want to get off the track? Press 3")
if direction1=="1":
  speed=float(input("How many miles/hour are you going to run? (Enter a number)"))
  if speed<10:
      lastwords=input("Do you have any last words?")
      if lastwords=="JUMP" or lastwords=="jump" or lastwords=="Jump":
          print("You have jumped onto the minecart which is full of gold. Now you're rich enough to get married.")
          exit()
      else:
          print("You have a terrible choice of words. You get hit by the minecart and guess what your last thought was - 'Man, that's the dumbest thing I've said.'")
          exit()


  if speed>=10:
          print("You ran too fast and the minecart mowed you down")
          exit()
if direction1=="2":
  print("It's getting darker as you run away")
  time.sleep(2)
  print("DARKER..")
  time.sleep(1)
  print("You hear a crash behind you! The mineshaft seems to be caving in...")
  time.sleep(2)
  print("You run Faster")
  time.sleep(2)
  print("And FASTER")
  time.sleep(1)
  print("Seconds later you're falling into the sea...As soon as you surface, you look up and see a minecart crashing towards you.")
  exit()
else:
  print("Trying to play it safe huh? Well, turns out that there's a chasm beneath the track.\nYou fall to your death and regret hurts you more than your body smacking the ground.")
  exit()





# Author: Malachi Holden and Nathan Jose          TODO Change this!


if dead == True:
   quit()

#########################################################################################################
# TODO Once you've tested your code and it works, copy your code between the blocks of ###'s,
# TODO plus the death code above, into your Google Doc.
# TODO The instructor will be combining it all into the master program.

# Authors: Evan Johnson, Nick Hitchcock          TODO Change this!
if dead == False:
   print("(Your new friend has just asked for your name)")
   username2 = input("(What will you tell him?)")
   print('''"Fantastic, nice to meet you ''' + str(username2) + '''."''' )
   friendusername = input('''"I'm..."''' + "  (What would you like your friend's name to be?)")
   origins = input('''"So where have you come from, ''' + username2 + '''?"''' "[above/below]")
if origins == "below":
   print("(Why would you admit to this?)")
   time.sleep(delay)
   print("...")
   print("(Are you aware of what this implies?)")
   print('''"A Demon... Why have you come to stain this land?...''')
   reaction = int(input('''(How loudly will you deny the accusation?) (On a scale from 0 - 10)'''))
   if reaction < 5:
       print("(Exactly what you would expect is about to happen)")
       print("(Your friend immediatley pulls out a dagger and kills you)")
       print("(Nice job)")
       dead = True
   else:
       print ('''"A poor choice of words, I presume"''')
       print ('''"but I don't believe we should travel together, as the very suggestion of trusting a demonic presence is a joke."''')
       alone = True
elif origins == "above":
   print('''"As one would assume"''')
   hometown = input('''"What town do you originate from?"''')
   print ('''"Ah, I've only heard of the riches of ''' + str(hometown) + '''"''')
   motivations = input ('''"Why have you come to this labyrinth?"''')
   print('''"Well''' + str(username2) + "from" + str(hometown) + '''which way would you like to go?"''')
   direction2 = input('''"East or West?"''')
   print ("(You then wander into the darkness, hopeful, but fearing for your life.)")
if dead == True:
   quit()
# Author: Ty Feng, Aaron Christson      
print()
number = float(input("Pick any number as your lucky number"))

if number > 500:
   print("Congratulations! Welcome to the next chapter. You are rewarded 500 points.")
elif number <- 0:
   print("Sorry, anything negative is not lucky enough. You're dead. End of the story.")
   dead == True
else:
   print("Okay, it's an okay number. Welcome to the next chapter.")
if dead == True:
   quit()
# Author: Dr. Scott Heggen      TODO: Change this to your names
# Username: heggens             TODO: Change this to your usernames
#
# Assignment: T1: Choose Your Own Adventure
# Purpose: To create a choose-your-own-adventure style game.
# Each "twist" in the story is from a different group. The resulting story
# will either be incoherently random, or entertainingly "Mad Lib" like.
# Either way, it should be fun!
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#   Inspired by https://www.cs.hmc.edu/twiki/bin/view/CS5/Week0ChoiceProblem

######################################################################
import time

delay = 1.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False

# TODO Ask the user to input their name. Make it adventurous, such as:
# TODO "What do they call you, worthy adventurer? "

username = input("What's your name?")
#################################################################
# The following is the first part of the story. Don't change this.
print()
print("Welcome,", username, ", to the labyrinth")
time.sleep(delay)
print("Before you lies two paths.")
print("One path leads to treasures of unimaginable worth.")
print("The other, certain death. Choose wisely.")
print()
time.sleep(delay * 2)
print("You are in a dark cave. You can see nothing.")
print("Staying here is certainly not wise. You must find your way out.")
print()
time.sleep(delay)
direction = input("Which direction would you like to go? [North/South/East/West]")

########################################################

# An example chapter, to start your user off on your adventure
# Author: Scott Heggen
if direction == "North":
  print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
  time.sleep(delay)
elif direction == "South":
  print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
  time.sleep(delay)
  print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
  print("Running seems like a good idea now. But... it's really, really dark.")
  print()

  speed = int(input("How many steps would you like to take?"))
  if speed < 5:
      print("It appears you are more scared of the dark than a bear.")
      time.sleep(delay*2)
      print("Your fears were well-placed. The bear was hibernating, and your quiet exit pays off.")
  else:
      print("You run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
      time.sleep(delay)
      print("He eats you. You are delicious.")
      dead = True
else:
  print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
  time.sleep(delay)


# It is unusual to quit a program early like I do below. However, it serves us very well for this assignment,
# because it ends our story upon death. So we will use it. The alternative is a LOT of nested if/else statements,
# which would get messy by the last group. You will need this statement after your chapter is added.
if dead == True:
   quit()

#########################################################################################################
# TODO Add your part of the story here. Keep in mind you may not be coming right after the example above.
# TODO don't forget the two lines of code above!

# Author: Tobi Adejumo and Abdirahman Mohamed         TODO Change this!


if dead == True:
   quit()

print("\nas you continue walking in the dark you see a dim light flickering to your your right and to your left you a "
     "hear whispers.")
newDirection = input("which way will you go now [your left, right, or continue forward]")

if newDirection== "left" or newDirection == "Left":
   print("you found a flash light on the floor")
elif newDirection == "right" or newDirection=="Right":
   print("as you get closer to the whispers you realize that the figure that stands before you isn't a human but rather"
         "a creature that stands at least 20 feet tall")
   print("\nthe creature tells that behind him lies your freedom but in order to get there you must answer a riddle ")
   answer = input("\nthe riddle is what is the least common number 1-1000")
   if answer.isnumeric():
       if answer == '0' or int(answer) > 1000:
           print("onward wise adventurer")
       else:
           print("die")
   else:
       print("die")
elif newDirection == "forward" or newDirection=="Forward":
   print("nothing lies ahead of you for another 1000 miles")
#########################################################################################################
# TODO Once you've tested your code and it works, copy your code between the blocks of ###'s,
# TODO plus the death code above, into your Google Doc.
# TODO The instructor will be combining it all into the master program.
######################################################################
# Author: Jonathan Kemp Yungpeng Xia     TODO: Change this to your names
# Username: kempj xiay       TODO: Change this to your usernames
#
# Assignment: T1: Choose Your Own Adventure
# Purpose: To create a choose-your-own-adventure style game.
# Each "twist" in the story is from a different group. The resulting story
# will either be incoherently random, or entertainingly "Mad Lib" like.
# Either way, it should be fun!
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#   Inspired by https://www.cs.hmc.edu/twiki/bin/view/CS5/Week0ChoiceProblem

######################################################################
import time

delay = 1.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False

# TODO Ask the user to input their name. Make it adventurous, such as:
# TODO "What do they call you, worthy adventurer? "


#################################################################
# The following is the first part of the story. Don't change this.

# It is unusual to quit a program early like I do below. However, it serves us very well for this assignment,
# because it ends our story upon death. So we will use it. The alternative is a LOT of nested if/else statements,
# which would get messy by the last group. You will need this statement after your chapter is added.
if dead == True:
   quit()

#########################################################################################################
# TODO Add your part of the story here. Keep in mind you may not be coming right after the example above.
# TODO don't forget the two lines of code above!

# Author: Jon Kemp Yungpeng Xia        TODO Change this!

import time
delay =2.0
print("On a dark night lightning splits the clouds with a large boom of thunder as you walk ")
print("up the path to a dilapidated old house. You get to the door and see a large")
print("ornate golden lion door if knocker.")
print("Before you can let the knocker go you hear a voice.")
username = input("Who goes there?")
########################################################################################################
print("Welcome,", username,", to Narnia")
time.sleep(delay)
print("beyond this door there are 3 different hallways.")
print("One path will lead to unimaginable bliss.")
print("Three will lead to shall we say less than desirable circumstances.")
print("choose carefully.")
print()
time.sleep(delay)
direction = input("Which hallway will you take? [Left/Forward/Right]")
if direction == "Left":
   print("Ah what a choice! You will be greeted with 600 pounds of choclate and a glowing red EXIT sign.")
   time.sleep(delay)
elif direction == "Forward":
   print("As you gaze deeply into the darkness that lies before you looking straight ahead and ignoring the floor")
   print("you fall into an endless pit and are mauled by ravenous wolves. Sucks to be you.")
   dead = True
elif direction == "Right":
   print("You ascend an endless staircase and collapse from exhaustion and fall down all the steps and break both legs.")
   print("You eventually die from starvation.")
   dead = True
   speed = int(input("How many steps would you like to take?"))
   if speed > 10:
       print("You eventually die from starvation.")

   print("You get bored and walk back down the steps but trip and fall and die.")
   dead = True

if dead == True:
   quit()

#########################################################################################################
# TODO Once you've tested your code and it works, copy your code between the blocks of ###'s,
# TODO plus the death code above, into your Google Doc.
# TODO The instructor will be combining it all into the master program.
# Author: Bhawesh Mishra & Josh W. Pollock        TODO Change this!

fruit = input("Enter the one do you like the most? [Apples / Oranges / Banana / Peach]")

if fruit == "Apples":
  print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
  time.sleep(delay)

elif fruit == "Oranges":
  print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
  time.sleep(delay)
  print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
  print("Running seems like a good idea now. But... it's really, really dark.")
  print()

  amt = int(input("How many Oranges would you like to eat?"))
  if amt < 5:
      print("Oops!! you didn't eat enough to make through the trip. Sorry!!")
      time.sleep(delay*2)
      print("You are lacking energy and died of exhaustion. Should have eaten more..")
      dead = True
  else:
      print("You have eaten too much oranges. The Citric Acid melted your empty stomach. You died!! Oops!! ")
      time.sleep(delay)
      dead = True

elif fruit == "Banana":
   print ("You got your banana but you are clumsy. You slipped on the peel, fell and landed head first on the stone.")
   print()
   print("Sorry, you are dying a horrible and painful death")
   time.sleep(delay)
   dead = True

elif fruit == "Peach":
   print ("Why Peach?? ")
   time.sleep(delay)
   print()
   print()
   way = input ("There are peaches everywhere. Which direction would you like to go? [ Left / Right] ")
   if way == "Left":
       print ("Sorry, You walked right into a Monster -- He is hungry and bites your head off.")
       print()
       dead = True
   elif way == "Right":
       time.sleep(delay)
       print("Hurray!! You can eat your peach now. However, it is not safe. Please find a way out.")
       print()
else:
  print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
  time.sleep(delay)
if dead == True:
   quit()
if dead == True:
   quit()

#########################################################################################################
# TODO Add your part of the story here. Keep in mind you may not be coming right after the example above.
# TODO don't forget the two lines of code above!

# Author: Natasha Mupfunya and Ivy Webb          TODO Change this!
choice = input("Do you wish to approach? [yes/no]")

print()
if choice == "yes":
   print("The stranger is also lost and has an extinguished torch. Luckily you have a match!")
   print()

else: cont = input("Do you wish to pass without greeting? [yes/no]")

print()

if cont == "yes":
   print("You go crazy from the darkness and die.")
   dead = True
else: print("Congratulations, the stranger has an extinguished torch and you have a match!"
           " You are able to see your surroundings and can continue to explore the cave.")

explore = int(input( "How long would you like to spend exploring?"))  #integer question
if explore  < 30:
   print("You have found a new part of the cave! It is full of gold and skeletons!") # success
elif explore > 30:
   print ("You got very lost and confused, and die of thirst.") # death
   dead = True

if dead == True:
  quit()
print()
if dead == False:
   print('You are on a private plane flying to the other side of the kingdom.')
   time.sleep(delay)
   print('The pilot gets sick and is unable to fly the plane.')
   time.sleep(delay)
   print()
   decision = input("You have the decision to fly the plane or jump out. [fly/jump]")
   print()
   if decision == "fly":
       print("Even though you have never flown a plane before you land safely in an open field.")
   elif decision == "jump":
       time = int(input("In how many minutes, you want to leave the plane? "))
       if time <= 3:
           print ("Ouf! That was close!")
           parachute = input("You have to chose between two parachutes. [blue/red].")
           print()
           if parachute == "blue":
                   print("You have chosen a faulty parachute where the cord does not release the pilot chute "
                         "causing you to hit the ground at a very fast speed ending in your death. RIP")
                   dead = True
           elif parachute == "red":
                   print("When you jumped out of the plane your parachute took a very long time to deploy, "
                         "but it deployed just in time given you a rough yet surviving landing.")
       elif time >= 3:
           print ("Sorry! It took you too long!")
           dead = True
       else:
           print("something went wrong in line 110")

if dead == True:
   quit()
#########################################################################################################
# TODO Once you've tested your code and it works, copy your code between the blocks of ###'s,
# TODO plus the death code above, into your Google Doc.
# TODO The instructor will be combining it all into the master program.
