from random import randint


def lireUnCandidat(cands):
    entree = input("Entrez le nom d'un candidat: ")

    while entree == "" or entree in cands:
        entree = input("Entrez le nom d'un autre candidat: ")

    return entree


def lireListeCandidats(n):
    i = 0
    liste_candidats = []

    while i < n:
        nom = lireUnCandidat(liste_candidats)
        liste_candidats.append(nom)
        i += 1

    return liste_candidats


def genererUnVotant(n):
    liste_pref = []

    for i in range(n):
        liste_pref.append(randint(0, n - 1))

    return liste_pref


def main():
    print(genererUnVotant(5))


if __name__ == "__main__":
    main()
