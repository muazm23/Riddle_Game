import random
#Random number generator from 1 to 6
dice = random.randint(1,6)
#Game instructions
print ("Welcome to Guess or Dare!\n")
print ("There is only 1 rule to this game, no cheating!")
print ("You either guess the right answer or you do the dare!\n")
print ("Welcome to Round 1!\n")
#If you want to roll pres 'y'
throw = input("To roll the dice type y: ")
if throw == 'y':
#If you roll a 1
    if dice == 1:
        print ("You have rolled a 1\n")
        print ("Your riddle is: ")
        answer = 'egg'
        riddle = input("What has to be broken before you can use it ? ")
        if riddle.lower() == answer:
            print ("\nThat is correct")
        else:
            print ("\nThat is incorrect")
            print ("The correct answer is: " + answer)
            print ("\nYour dare is: ")
            print ("Take an embarrassing selfie and post it")
#If you roll a 2
    elif dice == 2:
        print ("You have rolled a 2\n")
        print ("Your riddle is: ")
        answer = 'all of them'
        riddle = input("What month of the year has 28 days ? ")
        if riddle.lower() == answer:
            print ("\nThat is correct")
        else:
            print ("\nThat is incorrect")
            print ("The correct answer is: " + answer)
            print ("\nYour dare is: ")
            print ("Write your name on the floor with your tongue")
#If you roll a 3
    elif dice == 3:
        print ("You have rolled a 3\n")
        print ("Your riddle is: ")
        answer = 'sponge'
        riddle = input("What is full of holes but still holds water ? ")
        if riddle.lower() == answer:
            print ("\nThat is correct")
        else:
            print ("\nThat is incorrect")
            print ("The correct answer is: " + answer)
            print ("\nYour dare is : ")
            print ("You have to take a shot of pickle juice")
#If you roll a 4
    elif dice == 4:
        print ("You have rolled a 4\n")
        print ("Your riddle is: ")
        answer = 'towel'
        riddle = input("What gets wet while drying ? ")
        if riddle.lower() == answer:
            print ("\nThat is correct")
        else:
            print ("\nThat is incorrect")
            print ("The correct answer is: " + answer)
            print ("\nYour dare is: ")
            print ("Get into a heated debate with a wall")
#If you roll a 5
    elif dice == 5:
        print ("You have rolled a 5\n")
        print ("Your riddle is: ")
        answer = 'darkness'
        riddle = input("The more of this there is, the less you see. What is it ? ")
        if riddle.lower() == answer:
            print ("\nThat is correct")
        else:
            print ("\nThat is incorrect")
            print ("The correct answer is: " + answer)
            print ("\nYour dare is: ")
            print ("You have to eat a raw egg")
#If you roll a 6
    elif dice == 6:
        print ("You have rolled a 6\n")
        print ("Your riddle is: ")
        answer = 'piano'
        riddle = input("What has many keys but can't open a single lock ? ")
        if riddle.lower() == answer:
            print ("\nThat is correct")
        else:
            print ("\nThat is incorrect")
            print ("The correct answer is: " + answer)
            print ("\nYour dare is: ")
            print ("Let someone draw on your face")

#Start of round 2
print ("\nWelcome to Round 2!")
#Random number generator from 7 to 12
digit = random.randint(10,12)
#If you want to roll press 'y'
roll = input("\nTo roll the dice type y: ")
if roll == 'y':
#If you roll a 7
    if digit == 7:
        print ("\nYou have rolled a 7\n")
        print ("Your riddle is: ")
        answer = 'secret'
        riddle = input("If you’ve got me, you want to share me; if you share me, you haven’t kept me. \nWhat am I ? ")
        if riddle.lower() == answer:
            print ("\nThat is correct")
        else:
            print ("\nThat is incorrect")
            print ("The correct answer is: " + answer)
            print ("\nYour dare is: ")
            print ("Let someone else style your hair and keep it that way for the rest of the day")
#If you roll an 8
    elif digit == 8:
        print ("\nYou rolled an 8\n")
        print ("Your riddle is: ")
        answer = 'stairs'
        riddle = input("What goes up and down but doesn't move ? ")
        if riddle.lower() == answer:
            print ("\nThat is correct")
        else:
            print ("\nThat is incorrect")
            print ("The correct answer is: " + answer)
            print ("\nYour dare is: ")
            print ("For the next 5 minutes you have to sing whenever you talk")
#If you roll a 9
    elif digit == 9:
        print ("\nYou rolled a 9\n")
        print ("Your riddle is: ")
        answer = 'second place'
        riddle = input("If you’re running in a race and you pass the person in second place, \nwhat place are you in ? ")
        if riddle.lower() == answer:
            print ("\nThat is correct")
        else:
            print ("\nThat is incorrect")
            print ("The correct answer is: " + answer)
            print ("\nYour dare is: ")
            print ("Call the last person you talked to and sing 'Happy Birthday' for them")
#If you roll a 10
    elif digit == 10:
        print ("\nYou rolled a 10\n")
        print ("Your riddle is: ")
        answer = 'your name'
        riddle = input("It belongs to you, but other people use it more than you do. What is it ? ")
        if riddle.lower() == answer:
            print ("\nThat is correct")
        else:
            print ("\nThat is incorrect")
            print ("The correct answer is: " + answer)
            print ("\nYour dare is: ")
            print ("You have to wax a part of your body")
#If you roll an 11
    elif digit == 11:
        print ("\nYou rolled an 11\n")
        print ("Your riddle is: ")
        answer = 'short'
        riddle = input("What five-letter word becomes shorter when you add two letters to it ? ")
        if riddle.lower() == answer:
            print ("\nThat is correct")
        else:
            print ("\nThat is incorrect")
            print ("The correct answer is: " + answer)
            print ("\nYour dare is: ")
            print ("You have to crack an egg over your head")
#If you roll a 12
    elif digit == 12:
        print ("\nYou rolled a 12\n")
        print ("Your riddle is: ")
        answer = 'envelope'
        riddle = input("What begins with an 'e' and only contains one letter ? ")
        if riddle.lower() == answer:
            print ("\nThat is correct")
        else:
            print ("\nThat is incorrect")
            print ("The correct answer is: " + answer)
            print ("\nYour dare is: ")
            print ("Give your phone to another player to send a text message to their contact \nof choice")

#Start of round 3 (final round)
print ("\nWelcome to the final Round!")
#Random number generator from 13 to 18
number = random.randint(13,18)
#if you want to roll press 'y'
shake = input("\nTo roll the dice type y: ")
if shake == 'y':
#If you roll a 13
    if number == 13:
        print ("\nYou rolled a 13\n")
        print ("Your riddle is: ")
        answer = 'stone'
        riddle = input("What word of five letters has one left when two are removed ? ")
        if riddle.lower() == answer:
            print ("\nThat is correct")
        else:
            print ("\nThat is incorrect")
            print ("The correct answer is: " + answer)
            print ("\nYour dare is: ")
            print ("Let one person slap you as hard as they want")
#If you roll a 14
    elif number == 14:
        print ("\nYou rolled a 14\n")
        print ("Your riddle is: ")
        answer = 'few'
        riddle = input(" I am a word of letters three; add two and fewer there will be. What word am I ? ")
        if riddle.lower() == answer:
            print ("\nThat is correct")
        else:
            print ("\nThat is incorrect")
            print ("The correct answer is: " + answer)
            print ("\nYour dare is: ")
            print ("You have to show everyone your last message")
#If you roll a 15
    elif number == 15:
        print ("\nYou rolled a 15\n")
        print ("Your riddle is: ")
        answer = 'light'
        riddle = input("What can fill a room but takes up no space ? ") 
        if riddle.lower() == answer:
            print ("\nThat is correct")
        else:
            print ("\nThat is incorrect")
            print ("The correct answer is: " + answer)
            print ("\nYour dare is: ")
            print ("You have to drink whatever the group makes for you")
#If you roll a 16
    elif number == 16:
        print ("\nYou rolled a 16\n")
        print ("Your riddle is: ")
        answer = 'mirror'
        riddle = input("If you drop me I’m sure to crack, but give me a smile and I’ll always smile back. What am I ? ")
        if riddle.lower() == answer:
            print ("\nThat is correct")
        else:
            print ("\nThat is incorrect")
            print ("The correct answer is: " + answer)
            print ("\nYour dare is: ")
            print ("You have to do 30 pushups")
#If you roll a 17
    elif number == 17:
        print ("\nYou rolled a 17\n")
        print ("Your riddle is: ")
        answer = 'day and night'
        riddle = input("What breaks yet never falls, and what falls yet never breaks ? ")
        if riddle.lower() == answer:
            print ("\nThat is correct")
        else:
            print ("\nThat is incorrect")
            print ("The correct answer is: " + answer)
            print ("\nYour dare is: ")
            print ("You have to give everyone the silent treatment for 30 minutes")
#If you roll an 18
    elif number == 18:
        print ("\nYou rolled an 18\n")
        print ("Your riddle is: ")
        answer = 'coffin'
        riddle = input("The person who makes it has no need of it; the person who buys it has no use for it. The person who uses it can neither see nor feel it. What is it ? ")
        if riddle.lower() == answer:
            print ("\nThat is correct")
        else:
            print ("\nThat is incorrect")
            print ("The correct answer is: " + answer)
            print ("\nYour dare is: ")
            print ("You have to eat a spoonful of hot sauce without anything to drink after")
#End of the game
print ("\nThe game has now come to an end. Thank you for playing.")
print ("If you got all the answers right, Congratulations!")
print ("If you got any of the answers wrong, Good luck with your dare!")  
