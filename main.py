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
        nombre_candidat = randint(0, n - 1)
        for i in range(n):
            if nombre_candidat not in liste_pref:
                liste_pref.append(nombre_candidat)
            nombre_candidat = randint(0, n - 1)

    return liste_pref


def genererListeVotants(nc, nv):
    liste_votants = []

    for i in range(nc):
        liste_votants.append(genererUnVotant(nv))

    return liste_votants


def affichePrefs(prefs, cands, v):
    noms = ""
    for i in prefs[v]:
        noms += cands[i] + " ; "

    return f"Prefs du votant {v} : " + noms


def main():
    prefs = genererListeVotants(3, 5)
    cands = ["Felix", "Arthur", "Lucien", "Ariane", "Octave"]
    print(prefs)
    print(affichePrefs(prefs, cands, 2))


if __name__ == "__main__":
    main()
