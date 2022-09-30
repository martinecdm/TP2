import random

nombre = input("Entrez un nombre")


n = random.randint(0,100)
appreciation = "?"
while True:
    var = input("Entrez un nombre")
    var = int(var)
    if var < n :
        appreciation = "trop bas"
        print(var, appreciation)

    else :
        appreciation = "trop haut"
        print(var, appreciation)
    if var == n:
        appreciation = "bravo !"
        print(var, appreciation)
        break



