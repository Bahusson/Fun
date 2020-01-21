# Zagadka rzucona przez znajomego.
# Klasa ma dostać dowolny string i wyrzucać jego lustrzane odbicie.
# Zrobione dla zabawy. Enjoy!

yourstring = "Hello darkness my old friend..."


class Echo(object):
    def mirror(self, mystring):
        newstring = ""
        x = len(mystring)
        while x > 0:
            y = len(mystring) - x + 1
            z = -y
            a = mystring[z]
            newstring += a
            x -= 1
        return newstring


E = Echo()
print(E.mirror(yourstring))
