# Dungeons of Cliche python game 
# Created by @kaycebec 
# Developed by @kaycebec and @tmeralus
## creates a delay in action prints by the entered second -- use integers only...real numbers fucks shit up
import time
## generates random number for attacks -- 0 - 5
import random
# import consule menu for menu driven testing
#from simple-term-menu import TerminalMenu 
#from consolemenu import *
#from consolemenu.items import *


# call for any attack
attack_Function = random.randint(0,5)

# var for player and any enemy appears below. Keep it neat...ish
trollHealth = 12
attack_Function = random.randint(0,5)
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
        time.sleep(3)
        print("!!!!")
        time.sleep(3)
        print("fuck man, I wasn't serious.")
        time.sleep(3)
        print("That actually hurts...")

def attack_error():
    print("...either you cannot spell or you're being a dick. Either way, try again " + userName)
    time.sleep(1)
    print("Let's try this again...write attack. Otherwise I'll attack me for you")
    playerAction = input()
    attacking()

menu_screen = """
    ___                                                         __     ___  _  _        _           
   /   \ _   _  _ __    __ _   ___   ___   _ __   ___    ___   / _|   / __\| |(_)  ___ | |__    ___  
  / /\ /| | | || '_ \  / _` | / _ \ / _ \ | '_ \ / __|  / _ \ | |_   / /   | || | / __|| '_ \  / _ \'
 / /_// | |_| || | | || (_| ||  __/| (_) || | | |\__ \ | (_) ||  _| / /___ | || || (__ | | | ||  __/
/___,'   \__,_||_| |_| \__, | \___| \___/ |_| |_||___/  \___/ |_|   \____/ |_||_| \___||_| |_| \___|
                       |___/                                                                        
    """

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

credits_Screen = """
        Developers
        Kevin Becchio 
        url: https://github.com/Kcbec
        Twitter: (pending)

        Tedley Meralus 
        Twitter: @techgameteddy
        url: meralus.com                                                    
    """
## Game begins.
#print("your test health is " + str(newTrollHealth))

def main_menu(): 
    print(menu_screen)
    print("\n New Dungeon Game?")
    print("\t1. Start Game")
    print("\t2. Credits")
    print("\t3. Quit") 
    menu_select = int(input("\n Choose an option: "))
    
    while menu_select < 1 or menu_select > 3:
        print("Your choices, like your life, are invalid")
        menu_select = int(int("\n New Dungeon Game?"))
    if menu_select == 1:
        start_game()
    elif menu_select == 2:
        print(credits_Screen)
    elif menu_select == 3:
        exit()

def start_game():
    print("\n Welcome to Dungeons of Cliche. ")
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
        time.sleep(2)
        print("Troll does " + str(attack_Function) + " damage.")


# Stars main menu by running this function
main_menu()