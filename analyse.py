def compterBulletins(cands, bulls):
    # Initialisation du dictionnaire
    dico = {}
    for candidat in cands:
        if candidat not in dico:
            dico[candidat] = 0

    dico["blanc"] = 0
    dico["nul"] = 0

    # Comptage des bulletins
    for bulletin in bulls:
        if not bulletin:
            dico["blanc"] += 1
        elif bulletin not in cands:
            dico["nul"] += 1
        else:  # bulletin in cands
            dico[bulletin] += 1

    return dico


def afficheClassement(dico):
    cles = list(dico.keys())
    dico_trie = {}
    total = 0

    for i in range(len(dico) - 2):
        # len(dico) - 2 pour enlever les votes "blanc" et "nul"
        for j in range(len(dico) - 3):
            if (
                dico[cles[j]] < dico[cles[j + 1]]
                or (dico[cles[j]] == dico[cles[j + 1]] and cles[j] > cles[j + 1])
            ):  # pour classer par ordre alphabétique -> on compare les strings cles[j] et cles[j+1]
                # si cles[j] > cles[j+1] alors on a cles[j] qui est plus bas dans l'alphabet

                temp = cles[j]
                cles[j] = cles[j + 1]
                cles[j + 1] = temp

    for i in range(len(cles) - 2):
        dico_trie[cles[i]] = dico[cles[i]]
        total += dico[cles[i]]

    print("Total des voix exprimées:", total)
    rang = 1
    for i in range(len(cles) - 2):
        pourcentage = round((dico_trie[cles[i]] / total) * 100, 2)
        # on garde 2 chiffres après la virgule pour la lisibilité

        if i > 0 and dico_trie[cles[i]] == dico_trie[cles[i - 1]]:
            print("-", cles[i], pourcentage, "%")

        else:
            rang = i + 1
            print(rang, cles[i], pourcentage, "%")
