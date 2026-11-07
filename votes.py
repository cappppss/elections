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

    return max_index + 1  # pour éviter d'avoir un "candidat numéro 0"


def scrutinMaj1Tour(prefs, cands):
    compte_voix = compterVoix(prefs)
    cand_gagnant = gagnant(compte_voix)

    return f"Gagnant : {cands[cand_gagnant - 1]} avec {compte_voix[cand_gagnant - 1]} voix"  # on fait cand_gagnant - 1 pour que l'index corresponde au bon candidat


def compterVoixSel(prefs, qualif):
    voix_obtenues = [0] * len(prefs[0])

    for votes in prefs:
        trouve = False

        for candidat in votes:
            if candidat in qualif and not trouve:
                voix_obtenues[candidat] += 1
                trouve = True

    return voix_obtenues


def deuxPremiers(prefs):
    maxi1 = prefs[0][0]
    maxi2 = prefs[0][1]
    index1 = 0
    index2 = 0

    for i in range(len(prefs)):
        for j in range(len(prefs[i])):
            if prefs[i][j] >= maxi1:
                index2 = index1
                index1 = j
                maxi2 = maxi1
                maxi1 = prefs[i][j]

    return index2, index1


def scrutinMaj2Tours(prefs, cands):
    voix_premier_tour = compterVoix(prefs)
    deux_premiers = list(deuxPremiers(prefs))

    candidat1, candidat2 = deux_premiers

    if voix_premier_tour[candidat1] < voix_premier_tour[candidat2]:
        temp = candidat1
        candidat1 = candidat2
        candidat2 = temp

    print("Premier tour :")
    print("\nPremier :", cands[candidat1], "avec", voix_premier_tour[candidat1], "voix")
    print("Deuxième : ", cands[candidat2], "avec", voix_premier_tour[candidat2], "voix")

    voix_deuxieme_tour = compterVoixSel(prefs, deux_premiers)

    gagnant_index = gagnant(voix_deuxieme_tour) - 1
    gagne = cands[gagnant_index]
    print("\nDeuxième tour :")
    print(
        "\nGagnant :",
        gagne,
        "avec",
        voix_deuxieme_tour[gagnant_index],
        "voix",
    )
