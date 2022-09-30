import random

nbr = random.randint(0,100)
var = "?"
while True:
    var = input("Entrez un nombre")
    var = int(var)
    if var < nbr :
        aide = "trop bas"
        print(var, aide)

    else :
        aide = "trop haut"
        print(var, aide)
    if var == nbr:
        aide = "bravo !"
        print(var, aide)
        break
