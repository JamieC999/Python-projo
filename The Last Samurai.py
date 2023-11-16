import random

playAgain = True

# This function displays a start combat message
def startCombat():
    print( "Let's start with combat" )


startingStory = "\n6 enimies arrive to your country to take over, you arrived and the people need your help while you are the last samurai of your clan"

civilianQuestion = "Who are you?...."
Storyanswers = 'Im a samurai from the Hinokami clan, and im the last one.'


enemieName = 'Lord Muzan'

print( startingStory )
userName = input( f"{civilianQuestion}: " )

print(f"Lord Muzan: Hahahahahah {userName}, you think you're going to win? No.")

startCombat()


userAttack = input( "Press enter to attack" )
number1 = random.randint(0,1)

userAttack = input( "Press enter to attack again " )
number2 = random.randint(0,1)

userAttack = input( "Press enter to attack one more time" )
number3 = random.randint(0,1)

result = number1 + number2 + number3

if result > 1:
    print( f"{userName}: Lord Muzan, I beat you, hahahahahahaha" )
else:
    print( f"Lord Muzan, {userName} I beat you bad hahahahahaha" )





