from votes import *
from candidats import *


def main():
    candidats = ["A", "I", "J", "M", "S", "D"]
    nb_tests_diff = 0
    somme_gagnants_diff = 0
    n = 0

    nb_test = 1000
    nb_votants = 10000

    while n < nb_test:
        liste_votants = genererListeVotants(len(candidats), nb_votants)

        maj1tour = scrutinMaj1Tour(liste_votants, candidats)
        maj2tour = scrutinMaj2Tours(liste_votants, candidats)
        vote_alternatif = voteAlternatif(liste_votants, candidats)
        vote_borda = voteBorda(liste_votants, candidats)

        gagnants = [maj1tour[0], maj2tour[0], vote_alternatif[0], vote_borda[0]]
        gagnants_diff = []

        for gagnant in gagnants:
            if gagnant not in gagnants_diff:
                gagnants_diff.append(gagnant)

        nb_gagnants = len(gagnants_diff)
        somme_gagnants_diff += nb_gagnants

        if nb_gagnants > 1:
            nb_tests_diff += 1

        n += 1

    print(
        "pourcentage de tests avec résultat différents:",
        (nb_tests_diff / nb_test) * 100,
    )

    print("nombre moyen de gagants distincts:", somme_gagnants_diff / nb_test)

    # liste_votants = genererListeVotants(len(candidats), 600)
    # print("Scrutin Maj 1 Tour")
    # scrutinMaj1Tour(liste_votants, candidats)
    # print("\n")

    # print("Scrutin Maj 2 Tours")
    # scrutinMaj2Tours(liste_votants, candidats)
    # print("\n")

    # print("Vote Alternatif")
    # voteAlternatif(liste_votants, candidats, True)
    # print("\n")

    # print("Vote Borda")
    # voteBorda(liste_votants, candidats)


if __name__ == "__main__":
    main()
