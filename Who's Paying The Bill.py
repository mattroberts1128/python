print("Who is paying the bill at dinner?")

friends = ["Jon", "Rachel", "Matthew", "Fran", "August"]
import random

print(random.choice(friends))

random_index = random.randint(0, 4)
print((friends[random_index]))

random_int = random.randint(0, 4)
# print(random_int)

friends_name = random_int

if friends_name == 0:
    print("Jon")
elif friends_name == 1:
    print("Rachel")
elif friends_name == 2:
    print("Matthew")
elif friends_name == 3:
    print ("Fran")
elif friends_name == 4:
    print("August")

