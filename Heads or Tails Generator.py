import random

random_int = random.randint(0, 1)
print(random_int)

# random_float = random.uniform(1, 10)
# print(random_float)

# random_number_0_to_1 = random.random() * 5
# print(random_number_0_to_1)

heads_vs_tails = random_int

if heads_vs_tails == 1:
    print("Heads")
else:
    print("Tails")