print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the Kingdom of Arthur.")
print("Your mission is to find the Holy Grail.")
print("Two roads diverged in a yellow wood, And sorry you could not travel both. Two roads diverged in a wood,and you consider the one less traveled by, And hoping it will make all the difference.")
choice1 = input('Do you choose to take the road less traveled by? Type "Yes" or "Turn Around".')

if choice1 == "Yes" or choice1 == "yes":
    print ("Continue on the road.")
else:
    print("You may go home, defeated.")

choice2 = input('You have traveled far and now have come to a body of water. Do you want to swim? Type "I will swim" or "No, it is too cold".')

if choice2 == "I will swim" or choice2 == "i will swim":
    print("As Dory says, Just keep swimming, just keep swimming.")
else:
    print("You are indeed the wimp we all believed you are. Sad.")

choice3 = input("Thankfully, the weather is quite dry in these parts of Northern England,'though you're chainmail has started to rust. The time has come and you have arrived at the Sir Lancelots Castle. "
"The choice has been yours since you can remember. Would you like to knock?")

if choice3 == "Yes" or choice3 == "yes":
    print("I am one the who knocks.")
else:
    print("The shortest route back to Loserville is a couple blocks that way!")

choice4 = input("God answers the door, she asks you, 'What is the air-speed velocity of an unladen swallow?' 20 knots or 50 knots")

if choice4 == "What do you mean? An African or European swallow?":
    print("Well, you have to know these things when you're a king, you know.")
elif choice4 == "20 knots":
    print("Explosion from the distance quickly becomes an explosion throwing you from a cliff")
elif choice4 == "50 knots":
    print("God slaps you across the face. You have to now sit in time out.")
else:
    print("We are Knights who says 'Nee'")

print("Lord  Python, you were brave in your quest. Now, it is time to party like it is 1969.")
print("Congratulations on finishing the simulation. This message will self destruct in 3...2...1...")





