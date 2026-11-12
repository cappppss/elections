from candidats import *
from votes import *


def main():
    candidats = ["A", "I", "J", "M", "S", "D"]
    liste_votants = genererListeVotants(len(candidats), 600)
    liste = [170, 170, 170, 230, 1000]

    # print(compterVoix(liste_votants))
    # print(scrutinMaj1Tour(liste_votants, candidats))
    # print(compterVoixSel(liste_votants, [1, 4]))
    # print(deuxPremiers([250, 100, 250, 70, 250]))
    # print(scrutinMaj2Tours(liste_votants, candidats))
    #
    #

    print(voteAlternatif(liste_votants, candidats, True))


if __name__ == "__main__":
    main()
