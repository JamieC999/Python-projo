import random

playAgain = True

endingMessages = [
    "Thank you for playing my game",
    "Look out for more",
    "Bye!!!"
]

# This function displays a start combat message
def startCombat():
    print( "Let's fight, when i win comming for your army and for the country and taking it back" )



startingStory = "\n6 enimies arrive to your country to take over, you arrived and the people need your help while you are the last samurai of your clan"

civilianQuestion = "\nWho are you?...."
Storyanswers = 'Im a samurai from the Hinokami clan, and im the last one.'


enemieName = 'Lord Muzan'

print( startingStory )
userName = input( f"{civilianQuestion}: " )

# While the user wants to play again, start again from here.
while playAgain:
    print(f"\nLord Muzan: Hahahahahah {userName}, you think you're going to win? No you will never win.")

    startCombat()


    userAttack = input( "\nPress enter to attack [HIT ENTER]: " )
    number1 = random.randint(0,1)

    print( "\nLord Muzan: Ouch!!!\n" )

    userAttack = input( "Press enter to attack again to get a potential crit: " )
    number2 = random.randint(0,1)

    print( "\nLord Muzan: So you've chosen death. Hit me again if you dare!!!!\n" )

    userAttack = input( "Press enter to attack one more time and hope Muzan will go down: " )
    number3 = random.randint(0,1)

    print( "\nLord Muzan: Oh, no you want trouble huh\n" )

    result = number1 + number2 + number3

    if result > 1:
        print( f"{userName}: Lord Muzan, I beat you, and im taking my country back!" )
    else:
        print( f"Lord Muzan, {userName} I have defeted you and your country is mine hahah" )
    
    userResponse = input( "Do you want to fight again: y/n: " )

    # if the response is not equal to a yes
    if userResponse != "y":
        playAgain = False

# print out an empty line. Print out nothing and end with a new line
print()

for message in endingMessages:
    print( message )





