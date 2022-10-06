import random

tri = 0
var = "?"


while True:
    f1 = int(input("choisis le nombre minimum"))
    f2 = int(input("choisis le nombre maximum"))
    nbr = random.randint(f1, f2)
    print("j'ai choisi un nombre entre"f1" et"f2", devine le")
    var = int(input("Entrez un nombre"))

    if var < nbr :
        print("le nombre est plus haut que ", var)
        tri = tri + 1
    elif var > nbr:
        print("le nombre est plus bas que", var)
        tri = tri + 1
    if var == nbr:
        print("bravo le nombre était",nbr)
        print("vous avez essayer",tri,"fois")

        q1 = input("voulez-vous recommencer oui/non")

        if q1 == "oui":
            pass
            tri = 0

        elif q1 == "non":
            print("merci et aurevoir")
            break

