from random import randint


def genererUnVotant(n):
    liste_pref = []

    while len(liste_pref) < n:
        nombre_candidat = randint(0, n - 1)
        if nombre_candidat not in liste_pref:
            liste_pref.append(nombre_candidat)

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


def compterVoix(prefs):
    voix_obtenues = [0] * len(prefs[0])

    for votes in prefs:
        voix_obtenues[votes[0]] += 1

    return voix_obtenues


def gagnant(voix):
    maxi = voix[0]
    max_index = 0

    for i in range(len(voix)):
        if voix[i] >= maxi:
            maxi = voix[i]
            max_index = i

    return max_index + 1  # pour éviter d'avoir le "candidat numéro 0"


def scrutinMaj1Tour(prefs, cands):
    compte_voix = compterVoix(prefs)
    cand_gagnant = gagnant(compte_voix)

    return f"Gagnant : {cands[cand_gagnant - 1]} avec {compte_voix[cand_gagnant - 1]} voix"  # on fait cand_gagnant - 1 pour que l'index corresponde au bon candidat
