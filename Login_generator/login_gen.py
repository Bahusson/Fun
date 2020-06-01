# Program generuje login z losowych sylab i 3 cyfr, który
# jest w ten sposób stosunkowo łatwy do zapamiętania.

import random

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
consonants = [
 'b', 'c', 'd', 'f', 'g', 'h', 'j',
 'k', 'l', 'm', 'n', 'p', 'r', 's',
 't', 'w', 'z']

L1 = random.choice(consonants).capitalize()
L2 = random.choice(vowels)
L3 = random.choice(consonants)
L4 = random.choice(vowels)
L5 = random.choice(consonants)
L6 = random.choice(vowels)
L7 = random.choice(consonants)
L8 = random.choice(vowels)
L9 = str(random.randint(100,999))

fulllogin = L1 + L2 + L3 + L4 + L5 + L6 + L7 + L8 + L9
print(fulllogin)