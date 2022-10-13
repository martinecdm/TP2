import random

nb_essai = 0
essaie_joueur = "?"


while True:
    f1 = int(input("choisis le nombre minimum"))
    f2 = int(input("choisis le nombre maximum"))
    nbr = random.randint(f1, f2)
    print(f"j'ai choisi un nombre entre {f1} et {f2} devine le")
    essaie_joueur = int(input("Entrez un nombre"))
    while True:

        if essaie_joueur < nbr :
            print("le nombre est plus haut que ", essaie_joueur)
            nb_essai = nb_essai + 1
        elif essaie_joueur > nbr:
            print("le nombre est plus bas que", essaie_joueur)
            nb_essai = nb_essai + 1
        if essaie_joueur == nbr:
            print("bravo le nombre était",nbr)
            print("vous avez essayer", nb_essai, "fois")

            q1 = input("voulez-vous recommencer oui/non")

            if q1 == "oui":
                pass
                nb_essai = 0

            elif q1 == "non":
                print("merci et aurevoir")
                break



