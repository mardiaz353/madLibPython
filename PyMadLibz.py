#This space is where you import libraries
#Needs to be seeded
#Need to try for loop instead of new variables way
import random

randNumOne = random.randrange(0, 5)
randNumTwo = random.randrange(0, 5)
randNumThree = random.randrange(0, 5)
randNumFour = random.randrange(0, 5)
randNumFive = random.randrange(0, 5)

random.seed(0, 5)

#My name is ___ ____. You _____ my _____. Prepare to _____.
#first name, last name, verb in past tense, family member and another verb

firstName = ["Squeezy", "Dopey", "Tanonbum", "Robo", "Professor"]
lastName = ["Pickity", "Snickerz", "Gump", "Poultry", "Creaker"]
verbPastTense = ["dropped", "caught", "pinched", "snatched", "tossed"]
familyMember = ["mom", "dad", "brother", "grandma", "great - aunt"]
verb = ["jump", "climb", "sleep", "fish", "breathe"]

print("To play mad libz, press 1, to quit the program, press 0")
userNum = int(input())
message = "My name is %s %s. You %s my %s. Prepare to %s."
while userNum >= 0:
    if userNum == 1:
        print(message % (firstName[randNumOne], lastName[randNumTwo], verbPastTense[randNumThree], familyMember[randNumFour], verb[randNumFive]))
        print("Would you like to play again? Press 1 for yes and 0 for no")
        userNum = int(input())
        random.seed(0, 5)
    elif userNum == 0:
        print("I can't make you play with me")
        break
    else:
        print("You have to enter a valid number")
        print("Press 1 to play mad libz and 0 for no")
        userNum = int(input())
