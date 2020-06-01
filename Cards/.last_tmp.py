from great_arcana import *
import random
#dodaj awers revers
arkana = {0: ["Głupiec", fool], 1: ["Mag", wizard], 2: ["Kapłanka", priestess],
 3: ["Cesarzowa", empress], 4: ["Cesarz", emperor], 5: ["Kapłan", pope], 
 6: ["Kochankowie", lovers], 7: ["Rydwan", chariot], 8: ["Sprawiedliwość", justice],
 9: ["Pustelnik", hermit], 10: ["Koło Fortuny", wheel], 11: ["Moc", strength],
12: ["Wisielec", hangman], 13: ["Śmierć", death], 14: ["Umiarkowanie", temperance],
15: ["Diabeł", devil], 16: ["Wieża", tower], 17: ["Gwiazda", star], 18: ["Księżyc", moon], 
19: ["Słońce", sun], 20: ["Sąd Ostateczny", judgement], 21: ["Świat", world],}

omen = ["dobry omen", "zły omen"]
#wylosuj czy karta jest górą czy dołem.

class Card(object):
    
    def draft():
        card_drafted = random.choice(arkana)
        return card_drafted

    def side():
        flip = random.randint(1,2)
        return flip
    

def descript(card_name, card_side, num):
    nums = ["PIERWSZA","DRUGA","TRZECIA"]
    print(" ")
    print("@@@ KARTA " + nums[num] + " @@@")
    print(" ")
    print(card_name[0] + " - " + omen[card_side -1])
    print(" ")
    for item in card_name[1][0]:
        print(item)
        print(" ")
    for item in card_name[1][card_side]:
        print(item)
        print(" ")
    print(" ")
    print("xxx KONIEC KARTA " + nums[num] + " xxx")
    print(" ")   
    


card_1 = Card.draft()
side_1 = Card.side()
descript(card_1,side_1, 0)

card_2 = Card.draft()
side_2 = Card.side()
while card_1[0] == card_2[0]:
    print("repeating...")
    card_2 = Card.draft()
descript(card_2,side_2, 1)

card_3 = Card.draft()
while card_3[0] == card_1[0] or card_3[0] == card_2[0]:
    print("repeating...")
    card_3 = Card.draft()
side_3 = Card.side()
descript(card_3,side_3, 2)

#Pn'glui Mglw'nafh Cthulhu R'ley Wgah'nagl fhtagn!