""" °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
    °                                                                                                               °
    °                                 Projet de BlackJack - Benjamin Pellieux-Abram                                 °
    °                                                  UE : [INF131]                                                °
    °                                                Année : 2018-2019                                              °
    °                                                                                                               °
    °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"""


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


print(color.PURPLE,
      "  ---------------------------------------------------------  ",
      "              Bienvenue dans Blackjack Game                  ",
      "  ---------------------------------------------------------  ",
      "    Programme réalisé par Benjamin Pellieux-Abram dans le    ",
      "               cadre du projet de l'UE [INF131]              ", "\n", color.END, sep="\n")


""" On importe les modules nécéssaires à nos différentes fonctions """

from random import sample

"""On définit les variables communes à tout notre programme"""


pioche =[]
tour_number = 0
victoires_dico = {}


"""------------------------------------------------------------------------------------------------------------------
                                                      Partie A.1
   ------------------------------------------------------------------------------------------------------------------"""


"""" Il s'agit ici d'écrire la fonction paquet() qui permet de générer le paquet de 52 cartes nécessaire au jeu de
Blackjack"""


def paquet():
    valeur_carte = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'valet', 'dame', 'roi']                          # On définit ici les valeurs des cartes
    famille = [' de coeur', ' de trèfle', ' de pique', ' de carreau']                                                   # On définit les puisssances des cartes
    paquet = []                                                                                                         # On définit une liste vide que l'on utilisera pour le paquet

    for range_1 in range(0, len(famille), 1):                                                                           # On distribue les puissances des cartes
        for range_2 in range(0, len(valeur_carte), 1):
            card = str(valeur_carte[range_2] + famille[range_1])
            paquet.append(card)

    return paquet                                                                                                       # On récupère une liste en sortie de fonction


""" Il s'agit ici d'écrire une fonction qui pour une carte donnée (exemple : l'as de trèfle) renvoie la valeur qui lui
est associée (Dans notre exemple : 1) """


def valeurCarte(carte):
    print("Vous avez pioché la carte suivante : ", carte)
    if 'as de' in carte:                                                                                                # On filtre le cas où le joueur a un as
        value = int(input("Souhaitez-vous que sa valeur soit 1 ou 11 ? "))
    for range_1 in range(2, 11, 1):                                                                                     # On filtre ensuite les cartes de 2  à 10
        if str(range_1) in carte :
            value = int(range_1)
    if 'valet' in carte or 'dame' in carte or 'roi' in carte:                                                           # On filtre les têtes
            value = 10
    return value                                                                                                        # On récupère la valeur de la carte en sortie


""" Il s'agit ici d'écrire une fonction qui pour un entier n reçu renvoie une pioche constituée de n paquets de cartes
avec n le nombre de joueurs de la partie """


def initPioche(n):
    global pioche
    for range_1 in range(0,n, 1):                                                                                       # On crée une pioche contenant n paquets de cartes
        for range_2 in range(0, len(paquet()), 1):
            pioche.append(paquet()[range_2])
    return sample(pioche, len(pioche))                                                                                  # On retourne une pioche triée aléatoirement


""" Il s'agit ici d'écrire une fonction qui reçoit la pioche et, de façon optionnelle, le nombre de cartes à piocher,
et renvoit la liste des cartes piochées"""


def piocheCarte(p, x=1):
    taken_cards = []                                                                                                    # On crée une liste qui contiendra les cartes piochées
    for i in range(0, x, 1):
        card = p[0]
        taken_cards.append(card)                                                                                        # On ajoute la carte à la liste des cartes piochées
        p.pop(0)                                                                                                        # On supprime la carte de la pioche
    return taken_cards                                                                                              # On renvoit la liste des cartes piochées


"""------------------------------------------------------------------------------------------------------------------
                                                      Partie A.2
   ------------------------------------------------------------------------------------------------------------------"""


""" Il s'agit ici d'écrire une fonction qui reçoit le nombre de joueurs, demande à l'utilisateur le nom de chaque joueur
et renvoit la liste qui les contient """


def initJoueurs(n):
    players = []                                                                                                        # On crée une liste pour les noms des joueurs
    for range_1 in range(0, n, 1):
        name = str(input("Entrez le nom du joueur " + str(range_1+1) + " : "))
        players.append(name)                                                                                            # On ajoute le nom du joueur à la liste pré-établie
    return players                                                                                                      # On renvoit la liste de joueurs


""" Il s'agit ici d'écrire une fonction qui reçoit la liste des noms des joueurs  et une valeur initiale de score pour
les joueurs et renvoit un dictionnaire qui associe les joueurs à leurs scores initiaux """


def initScores(joueurs, v=0):
    players_dico = {}                                                                                                   # On crée un dictionnaire vide pour stocker les noms des joueurs et leurs scores
    for range_1 in range(0, len(joueurs), 1):
        players_dico[joueurs[range_1]] = v
    return players_dico                                                                                                 # On retourne le dictionnaire qui contient les joueurs et leurs scores


""" Il s'agit ici d'écrire une fonction qui reçoit la liste des joueurs et construit un dictionnaire de scores après
avoir pioché deux cartes pour chaque joueur et avoir ajouté la valeur des deux cartes à leur score qu'elle renvoit 
ensuite """


def premierTour(joueurs):
    players_dico = initScores(joueurs)                                                                                  # On crée le dictionnaire de joueurs
    pioche = initPioche(len(joueurs))                                                                                   # On crée la pioche
    for range_1 in range(0, len(joueurs), 1):
        print("\n", color.BLUE, " Premier Tour de ", joueurs[range_1], "  :", color.END)
        taken_cards = piocheCarte(pioche, 2)                                                                            # On crée une liste qui contient les deux cartes piochées
        players_dico[joueurs[range_1]] = valeurCarte(taken_cards[0]) + valeurCarte(taken_cards[1])                      # On ajoute la valeur des cartes piochées à son score
        print(color.RED, "Le score de ", joueurs[range_1], " est maintenant de ",
              players_dico[joueurs[range_1]], color.END, "\n")
    return players_dico                                                                                                 # On retourne le dictionnaire qui associe les joueurs et les scores


"""" Il s'agit ici de créer une fonction qui reçoit un dictionnaire de scores et renvoit le nom du gagnant et son score 
en filtrant les scores supérieurs à 21"""


def gagnant(scores):
    winner_list = {}
    list_scores = list(scores.values())                                                                                 # Pour faciliter les manipulations, on crée une liste qui contient les scores
    list_players = list(scores.keys())                                                                                  # On crée une liste qui contient les joueurs
    list_scores_inrange = []                                                                                            # On crée une liste vide qui va contenir les scores inférieurs ou égaux à 21
    list_players_inrange = []                                                                                           # On crée une liste vide qui va contenir les joueurs ayant des scores inférieurs ou égaux à 21
    for range_1 in range(0, len(list_scores)):                                                                          # On filtre les scores supérieurs à 21
        if list_scores[range_1] <= 21:
            list_scores_inrange.append(list_scores[range_1])
            list_players_inrange.append(list_players[range_1])
    maximum = min(list_scores_inrange) - 1                                                                              # On fixe un maximum arbitraire
    for range_2 in range(0, len(list_scores_inrange), 1):
        if maximum < list_scores_inrange[range_2]:                                                                      # On cherche le maximum des scores
            maximum = list_scores_inrange[range_2]
    print(color.YELLOW, color.BOLD, "\n", "Le(s) gagnant(s) de cette partie est/sont : ", color.END)
    for player in players_dico:
        if players_dico[player] == maximum:
            winner_list[player] = maximum
            print(color.YELLOW, color.BOLD, player, " avec ", maximum, " points !", color.END)
    return winner_list                                                                                                  # On retourne un dictionnaire qui contient le nom du gagnant et son score


"""------------------------------------------------------------------------------------------------------------------
                                                      Partie B.1
   ------------------------------------------------------------------------------------------------------------------"""


""" Il s'agit ici d'écrire une fonction qui demande à l'utilisateur si il veut continuer de jouer ou arrêter """


def continuer():
    ask = str(input("Voulez-vous continuer de jouer ? Oui / Non "))
    if ask == "Oui":
        return True
    else:
        return False

def continuer_partie():
    print("\n")
    ask = str(input("Voulez-vous faire une nouvelle partie ? Oui / Non "))
    if ask == "Oui":
        return True
    else:
        return False


""" Il s'agit ici d'écrire une fonction qui reçoit le nom d'un joueur et gère un tour de jeu """


def tourJoueur(j):
    print("\n", "Tour : ", tour_number, "Score : ", players_dico[j], "Joueur : ", j)                                    # On affiche le numéro du tour, le nom du joueur et son score dans la partie en cours

    player_playing = continuer()                                                                                        # On demande au joueur si il désire continuer
    if player_playing:                                                                                                  # Si c'est le cas, il fait un tour de jeu
        new_score = (valeurCarte(piocheCarte(pioche, 1)[0]) + players_dico[j])                                          # On actualise son score par le biais de la nouvelle carte piochée
        print(color.BOLD, color.RED, "Le score de ", j, " est maintenant de ",
              new_score, color.END, "\n")
        players_dico[j] = new_score                                                                                     # On actualise le score du joueur dans le dictionnaire
        if new_score <= 21:                                                                                             # On vérifie si son score est situé entre 0 et 21
            in_range = True
        else:
            in_range = False
    if not player_playing or not in_range:                                                                              # On supprime le joueur de la liste des joueurs si il a choisi d'arrêter ou si son score a dépassé 21
        index = players.index(j)
        players[index] = "to delete"                                                                                    # A cause des effets de bords, on choisit volontairement de remplacer le nom du joueur qui ne joue plus par "to delete"


"""------------------------------------------------------------------------------------------------------------------
                                                      Partie B.2
   ------------------------------------------------------------------------------------------------------------------"""


""" Il s'agit ici d'écrire une fonction qui donne un tour de jeu à chacun des joueurs encore en jeu dans la partie
courante """


def tourComplet():
    global tour_number
    tour_number = tour_number + 1
    for range_1 in players:
        tourJoueur(range_1)                                                                                             # On permet à chaque joueur de jouer un tour
    while "to delete" in players:
        players.remove("to delete")                                                                                     # On filtre ici les "to delete" pour les supprimer sans causer d'effets de bord sur la fonction


""" Il s'agit ici d'écrire une fonction qui détérmine si la partie est finie ou non et renvoie un booléen """


def partieFinie():
    if not players:                                                                                                     # On vérifie si la liste players est vide ou non
        return True                                                                                                     # Si oui, il n'y a plus de joueur en jeu donc la partie est finie
    else:
        return False                                                                                                    # Sinon, la partie n'est pas finie


""" Il s'agit ici d'écrire une fonction qui effectue une partie complète jusqu'à ce que la partie soit finie """


def partieComplete():
    global victoires_dico
    victoires_dico = initScores(players)                                                                                # On initialise un dictionnaire de victoires avec le nom de chaque joueur et le nombre de victoires à 0
    while not partieFinie():                                                                                            # On applique la fonction tourComplet() tant que la partie n'est pas finie
        tourComplet()
    winner_dico = gagnant(players_dico)                                                                                 # On initialise winner_dico le dictionnaire qui contient les gagnants de cette partie
    for winner in winner_dico:
        victoires_dico[winner] += 1                                                                                     # On ajoute 1 au nombre de victoires des joueurs qui ont atteints le plus haut score inférieur ou égal à 21


"""------------------------------------------------------------------------------------------------------------------
                                                      Partie B.3
                                                  Programme Principal
   ------------------------------------------------------------------------------------------------------------------"""


ask_number = int(input('Quel est le nombre de joueurs de la partie ? '))                                                # On demande le nombre de joueur de cette partie
print("\n")
players = initJoueurs(ask_number)                                                                                       # On initialise la liste des joueurs
ask_continue = True                                                                                                     # Pour le premier tour, on continue la partie
while ask_continue:                                                                                                     # On initialise une boucle pour savoir si on continue de jouer
    players_dico = premierTour(players)                                                                                 # On initialise le dictionnaire de scores
    partieComplete()                                                                                                    # On fait jouer une partie complète
    ask_continue = continuer_partie()                                                                                   # On demande si on recommence une partie


print(color.PURPLE,
      "  ---------------------------------------------------------  ",
      "  Merci de votre participation à notre jeu de Blackjack !!!  ",
      "  ---------------------------------------------------------  ", "\n"
      "    Programme réalisé par Benjamin Pellieux-Abram dans le    ",
      "               cadre du projet de l'UE [INF131]              ", color.END, sep="\n")
