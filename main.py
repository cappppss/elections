from candidats import *
from votes import *


def main():
    prefs = genererListeVotants(3, 5)
    cands = ["Felix", "Arthur", "Lucien", "Ariane", "Octave"]
    print(prefs)
    print(affichePrefs(prefs, cands, 2))


if __name__ == "__main__":
    main()
