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
