import random
#Program demonstruje jak długo trzeba rzucać kostkami, żeby uzyskać rządany wynik.


def fullhand(rolls, dice):
    var = rolls
    rnum = random.randint(1, dice)   
    while var > 0:
        if rnum < dice:
           rnum = random.randint(1, dice)
           var = rolls
           print(rnum)
        elif rnum == dice:    
           rnum = random.randint(1, dice)
           var -= 1
           print(rnum)
    print("streak!")
   
    
fullhand(6,49)