import random
choice = "Rock","Paper","Scissors"
print('''
Type 1 to Select Rock.
Type 2 to Select Paper.
Type 3 to Select Scissors.
If you want to exit the game press the "q" key and press enter.
''')

while True:
    com_choice = random.choice(choice)
    player_choice = input("Type Your Choice: ")

    if(player_choice != "1" and player_choice != "2" and player_choice != "3"):
        print("Please Enter A Valid Choice")

    else:
        if(player_choice == "1"):
            if(com_choice == "Rock"):
                print("Draw")
            elif(com_choice == "Paper"):
                print("Swallowed You")
            elif(com_choice == "Scissors"):
                print("You Smashed")
    
        elif(player_choice == "2"):
            if(com_choice == "Rock"):
                print("You Swallowed It")
            elif(com_choice == "Paper"):
                print("You Are Of The Same Mind")
            elif(com_choice == "Scissors"):
                print("It Tore You Apart")
    
        else:
            if(com_choice == "Rock"):
                print("Turned You To Dust")
            elif(com_choice == "Paper"):
                print("You Smashed It")
            elif(com_choice == "Scissors"):
                print("Draw")
    
    if(player_choice == "q"):
        quit()
