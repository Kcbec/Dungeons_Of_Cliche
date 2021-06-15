# Created by Kevin Becchio

# generates random number for attacks -- 0 - 5
import random
## creates a delay in action prints by the entered second -- use integers only...real numbers fucks shit up
import time


# call for any attack
attack_Function = random.randint(0, 5)

# var for player and any enemy appears below. Keep it neat...ish
trollHealth = 12
attack_Function = random.randint(0, 5)
trollHealth = 12
trollhealth = int(trollHealth)
userDamage = int(attack_Function)
newTrollHealth = trollHealth - userDamage
playerStartingHealth = 20
newPlayerHealth = playerStartingHealth - userDamage



def attacking():
    if attack_Function == "0":
        print("SWWWWINGGG and a miss. The odds of that happening weren't great...you should be upset")   
    else:
        print("your attack damage is " + str(attack_Function))   
        time.sleep(2)
        print("!!!!")
        time.sleep(2)
        print("fuck man, I wasn't serious.")
        time.sleep(2)
        print("That actually hurts...")

def attack_error():
    print("...either you cannot spell or you're being a dick. Either way, try again " + userName)
    time.sleep(1)
    print("Let's try this again...write attack. Otherwise I'll attack me for you")
    playerAction = input()    
    attacking()

title_Screen = """
    
                ___                                                                                       .-.                  ___                   ___                
            (   )                                                                                     /    \               (   )  .-.            (   )               
        .-.| |   ___  ___   ___ .-.     .--.     .--.     .--.    ___ .-.       .--.        .--.    | .`. ;      .--.     | |  ( __)   .--.     | | .-.     .--.   
        /   \ |  (   )(   ) (   )   \   /    \   /    \   /    \  (   )   \    /  _  \      /    \   | |(___)    /    \    | |  (''")  /    \    | |/   \   /    \  
        |  .-. |   | |  | |   |  .-. .  ;  ,-. ' |  .-. ; |  .-. ;  |  .-. .   . .' `. ;    |  .-. ;  | |_       |  .-. ;   | |   | |  |  .-. ;   |  .-. .  |  .-. ; 
        | |  | |   | |  | |   | |  | |  | |  | | |  | | | | |  | |  | |  | |   | '   | |    | |  | | (   __)     |  |(___)  | |   | |  |  |(___)  | |  | |  |  | | | 
        | |  | |   | |  | |   | |  | |  | |  | | |  |/  | | |  | |  | |  | |   _\_`.(___)   | |  | |  | |        |  |       | |   | |  |  |       | |  | |  |  |/  | 
        | |  | |   | |  | |   | |  | |  | |  | | |  ' _.' | |  | |  | |  | |  (   ). '.     | |  | |  | |        |  | ___   | |   | |  |  | ___   | |  | |  |  ' _.' 
        | '  | |   | |  ; '   | |  | |  | '  | | |  .'.-. | '  | |  | |  | |   | |  `\ |    | '  | |  | |        |  '(   )  | |   | |  |  '(   )  | |  | |  |  .'.-. 
        ' `-'  /   ' `-'  /   | |  | |  '  `-' | '  `-' / '  `-' /  | |  | |   ; '._,' '    '  `-' /  | |        '  `-' |   | |   | |  '  `-' |   | |  | |  '  `-' / 
        `.__,'     '.__.'   (___)(___)  `.__. |  `.__.'   `.__.'  (___)(___)   '.___.'      `.__.'  (___)        `.__,'   (___) (___)  `.__,'   (___)(___)  `.__.'  
                                        ( `-' ;                                                                                                                     
                                        `.__.                                                                                                                      
    """


## Game begins.
#print("your test health is " + str(newTrollHealth))

print("Welcome to Dungeons of Cliche. ")
time.sleep(2)
print("An adventure you will soon forget ")
time.sleep(2)
print("What is thou name-eth hero?: ")
userName = input()
time.sleep(2)
print("Why hello " + userName + ". Thou has-eth a very original...nameth. Creative parents-eth...")
time.sleep(3)
print("I'm not talking like this the whole fuckin time.")
time.sleep(3)
print("Do you choose to take a sword or bow?: ")
userWeapon = input()
time.sleep(2)
print("A " + userWeapon + "...")
time.sleep(2)
print("what an original choice.")
time.sleep(2)
print("type yes if you're ready to begin, type no if you have something better to do: ")
userAnswer = input()
if userAnswer == "yes":
    print("Alright, lets get this over with...")
else: 
    print("Nice try, " + userName + ", fuck you. Lets go")
time.sleep(3)
print("check this shit out...")
time.sleep(2)
# Displays large title text -- title_screen is a saved function
print(title_Screen) 
time.sleep(3)
print("If it were 1984 you would be blown the fuck away right now.")
time.sleep(3)
print("Check out this bad ass music...starting in")
time.sleep(2)
print("three")
time.sleep(1)
print("two")
time.sleep(1)
print("one")
time.sleep(3)
print("fuck...")
time.sleep(1)
print("Just use your imagination")
time.sleep(3)
print(".I swear it worked earlier ")
time.sleep(2)
print("WOW THIS PROGRAM IS GREAT")
time.sleep(2)
print("that's what you're thinking")
time.sleep(2)
print("Why don't test your weapon...")
time.sleep(2)
print("Go ahead...come at me bro. Just type attack")
playerAction = input()
if playerAction == "attack":
    attacking()
else: 
    attack_error()

time.sleep(2)
print("Whatever, okay moving on. Your starting health is 20. Drop below that and you die.")
time.sleep(3)
print("..be a hero blah blah blah")
time.sleep(3)
print("We enter the dungeon. It smells....awful")
time.sleep(3)
print("No one ever really talks about how terrible places like this smell.")
time.sleep(3)
print("Moving on. We see a troll approaching. Small little fucker but is wielding sword so we should probably kill it")
time.sleep(4)
print("Just type attack to att....")
time.sleep(2)
print("Troll does " + str(attack_Function) + " damage.")
time.sleep(3)
print("lol you're health...is now at uh....")
time.sleep(2)
print(newPlayerHealth)
time.sleep(2)
print("You should probably type att...")
time.sleep(2)
print("Troll does " + str(attack_Function) + " damage.")
time.sleep(2)
print("Just attack!!!")
playerAction = input()
if playerAction == "attack":
     print("your attack damage is " + str(attack_Function))
     time.sleep(2)
     print("whoaa what a tough guy")
     time.sleep(2)
     print("how are you still a virgin????")
     print("Holding place and shit. Type anything to quit")
     userAnswer = input()




    






    
    



