from random import randint


def genererUnVotant(n):
    liste_pref = []

    for i in range(n):
        nombre_candidat = randint(0, n - 1)
        for i in range(1, n):
            if nombre_candidat not in liste_pref:
                liste_pref.append(nombre_candidat)
            nombre_candidat = randint(0, n - 1)

    return liste_pref


def genererListeVotants(nc, nv):
    liste_votants = []

    for i in range(nv):
        liste_votants.append(genererUnVotant(nc))

    return liste_votants


def affichePrefs(prefs, cands, v):
    noms = ""

    for i in prefs[v - 1]:
        noms += cands[i] + " ; "

    return f"Prefs du votant {v} : " + noms
