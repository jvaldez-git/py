#!/usr/bin/python3

import random


"""

Randomly  outputs 5 (between 1-70) and a Random 1 number (between 1-25)

"""

randlist = random.sample(range(1,71),k=5) + [" _and_ ", random.choice(range(26))+1]
print("Mega Lottery")
print("First Five:")
first_5 = randlist[:5]
print(*first_5)
print(" ")
print("Random:")
print(randlist[-1])
print(" ")
