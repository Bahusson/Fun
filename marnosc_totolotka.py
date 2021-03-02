import random
score = 0
# Licz dopóki nie stracimy miliona
# lub aż nie wygramy
while -500000 < score < 1:
    roll = random.randint(1, 13983816)
    if roll == 3:
        score += 2000000
    else:
        score -= 3
    print(score)
    