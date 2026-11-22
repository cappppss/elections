from votes import *
from candidats import *
from analyse import *

from random import choice, randint


def main():
    candidats = ["A", "I", "J", "M", "S", "D"]
    not_candidats = "BUFHKLNVXWYTRE./!?'"

    def shuffleBulletin(n, bulletin):
        for i in range(1, n + 1):
            if i % randint(7, 19) == 0 and i % randint(9, 21) == 0:
                bulletin.append(choice(not_candidats))
            elif i % randint(23, 37) == 0:
                bulletin.append("")
            else:
                bulletin.append(choice(candidats))

        return bulletin

    liste_votants = genererListeVotants(len(candidats), 100)
    bulletin = []

    dico = compterBulletins(candidats, shuffleBulletin(1000, bulletin))
    afficheClassement(dico)


if __name__ == "__main__":
    main()
