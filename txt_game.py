# build a adventure game
# game can save name
# game will have choices
# game choices will lead to good or bad outcomes
# added choice of skill with different outcomes

user = input("What is your name: ")
print("Hello, "+user+" welcome!")

play_the_game = input("So "+user+", would you like to play? Please type Yes or No (Yes/No): ").lower()
if play_the_game == "yes":
    print("Great, we will play!")
    
    skill = input("Please pick between the skill of charisma or haste! (Charisma/Haste): ").lower()
    if skill == "charisma":
        print("Thank you "+user+", you have picked the "+skill+" skill. Lets now begin the game!")
    elif skill == "haste":
        print("Thank you "+user+", you have picked the "+skill+" skill. Lets now begin the game!")
    else:
        skill == "charisma"
        print("Sorry, wrong response, you have been given charisma. ")

    choice = input("You are walking down a path in a forest, however the path splits into two separate paths, the left path or the right path. Choose which path you will take (Left/Right): ").lower()
    if choice == "left":
        print("You have gone down the left path, you then see a pot of gold and rush to claim it, however you dont notice the trap below you and fall down a pit. You died, please try again! ")
    elif choice == "right":
        print("You have gone down the right path, while walking, next to your foot you see a pouch of gold.") 
        
        choice2 = input("Do you take the pouch of gold or leave it? (Take/Leave): ").lower()
        if choice2 == "leave":
            print("You choose not to take the pouch of gold and a Leprechaun notices your good deed, you continue on the path untile the Leprechaun confronts you")
            
            choice3 = input("The Leprechaun begins to talk to you, after some time an altercation breaks out between you and the Leprechaun. To survive this encounter, you can use your "+skill+" skill or you can try fighting the Leprechaun. Which will you choose? (Skill/Fight): ").lower()
            if choice3 == "fight":
                print("You choose to fight the Leprechaun however he is too fast and badly injures you. You DIED! ")
            elif skill == "charisma":
                print("You have chosen to use your "+skill+" skill, this results in the Leprechaun calming down, he then gives you a large coin purse full of gold as an apology! You WIN! ")
            elif skill == "haste":
                print("You have chosen to use your "+skill+" skill, this results in you quickly running away from the Leprechaun, while running you find his pot of gold, you then quickly pick it up and run into the sunset! You WIN!")

        elif choice2 == "take":
            print("You take the pouch of gold however a Leprechaun notices you taking his gold pouch and you die!")
        else:
            print("Sorry, that was not an option, try again!")
    else:
        print("This is not an option, try again!")
elif play_the_game == "no":
    print("You have chosen not to play!")
else:
    print("Sorry, wrong response, please try again")