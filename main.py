from candidats import *
from votes import *


def main():
    n = 1
    fin = False

    nb_votants = int(input("Nombre de votants : "))
    nb_cand = int(input("Nombre de candidats : "))

    liste_cand = lireListeCandidats(nb_cand)
    print(liste_cand)
    liste_votants = genererListeVotants(nb_cand, nb_votants)
    print(liste_votants)

    while n >= 1 and n <= nb_cand and not fin:
        n = int(input("Numero de votant : "))
        if n < 1 or n > nb_cand:
            fin = True

        else:
            print(affichePrefs(liste_votants, liste_cand, n))


if __name__ == "__main__":
    main()
