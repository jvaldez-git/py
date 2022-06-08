#!/usr/bin/python3

import random

# creates 5 unique elements from 1..70 and  a [0-25]+1 number
randlist = random.sample(range(1,71),k=5) + [" _and_ ", random.choice(range(26))+1]
print("Mega Lottery")
print("First Five:")
first_5 = randlist[:5]
print(*first_5)
print(" ")
print("Random:")
print(randlist[-1])
print(" ")
