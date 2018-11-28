""" °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
    °                                                                                                               °
    °                                 Projet de BlackJack - Benjamin Pellieux-Abram                                 °
    °                                                  UE : [INF131]                                                °
    °                                                Année : 2018-2019                                              °
    °                                                                                                               °
    °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"""

""" On importe les modules nécéssaires à nos différentes fonctions """

from random import sample


"""------------------------------------------------------------------------------------------------------------------
                                                      Partie A.1
   ------------------------------------------------------------------------------------------------------------------"""


"""" Il s'agit ici d'écrire la fonction paquet() qui permet de générer le paquet de 52 cartes nécessaire au jeu de
Blackjack"""

def paquet():
    valeur_carte = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'valet', 'dame', 'roi']                          # On définit ici les valeurs des cartes
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
    if '1 de' in carte:                                                                                                 # On filtre le cas où le joueur a un as
        value = int(input("Vous disposez d'un as, souhaitez-vous que sa valeur soit 1 ou 11 ? "))
    for range_1 in range(2, 11, 1):                                                                                     # On filtre ensuite les cartes de 2  à 10
        if str(range_1) in carte :
            value = range_1
    if 'valet' in carte or 'dame' in carte or 'roi' in carte:                                                           # On filtre les têtes
            value = 10
    return value                                                                                                        # On récupère la valeur de la carte en sortie


""" Il s'agit ici d'écrire une fonction qui pour un entier n reçu renvoie une pioche constituée de n paquets de cartes
avec n le nombre de joueurs de la partie """

def initPioche(n):
    pioche = []                                                                                                         # On crée une liste "Pioche" qui sera utilisée pour stocker les cartes
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
    joueurs = []                                                                                                        # On crée une liste pour les noms des joueurs
    for range_1 in range(0, n, 1):
        name = str(input("Entrez le nom du joueur " + n+1 + " : "))
        joueurs.append(name)                                                                                            # On ajoute le nom du joueur à la liste pré-établie
    return joueurs                                                                                                      # On renvoit la liste de joueurs


""" Il s'agit ici d'écrire une fonction qui reçoit la liste des noms des joueurs  et une valeur initiale de score pour
les joueurs et renvoit un dictionnaire qui associe les joueurs à leurs scores initiaux """

def initScores(joueurs,v=0):
    dictionnary = {}                                                                                                    # On crée un dictionnaire vide pour stocker les noms des joueurs et leurs scores
    for range_1 in range(0, len(joueurs), 1):
        dictionnary[joueurs[step]] = v
    return dictionnary                                                                                                  # On retourne le dictionnaire qui contient les joueurs et leurs scores


""" Il s'agit ici d'écrire une fonction qui reçoit la liste des joueurs et construit un dictionnaire de scores après
avoir pioché deux cartes pour chaque joueur et avoir ajouté la valeur des deux cartes à leur score qu'elle renvoit 
ensuite """

def premierTour(joueurs):
    players = initScores(joueurs)                                                                                       # On crée le dictionnaire de joueurs
    cards = initPioche(len(joueurs))                                                                                    # On crée la pioche
    for range_1 in range (0, len(joueurs), 1):
        taken_cards = piocheCarte(cards, 2)                                                                             # On crée une liste qui contient les deux cartes piochées
        players[joueurs[range_1]] = valeurCarte(taken_cards[0]) + valeurCarte(taken_cards[1])                           # On ajoute la valeur des cartes piochées à son score
        return players                                                                                                  # On retourne le dictionnaire qui associe les joueurs et les scores


"""" Il s'agit ici de créer une fonction qui reçoit un dictionnaire de scores et renvoit le nom du gagnant et son score 
en filtrant les scores supérieurs à 21"""

def gagnant(scores):
    list_scores = list(scores.values())                                                                                 # Pour faciliter les manipulations, on crée une liste qui contient les scores
    list_players = list(scores.keys())                                                                                  # On crée une liste qui contient les joueurs
    list_scores_inrange = []                                                                                            # On crée une liste vide qui va contenir les scores inférieurs à 21
    list_players_inrange = []                                                                                           # On crée une liste vide qui va contenir les joueurs ayant des scores inférieurs à 21
    for range_1 in range(0, len(list_scores)):                                                                          # On filtre les scores supérieurs à 21
        if list_scores[range_1] <= 21:
            list_scores_inrange.append(list_scores[range_1])
            list_players_inrange.append(list_players[range_1])
    maximum = min(list_scores_inrange) - 1                                                                              # On fixe un maximum arbitraire
    for range_2 in range(0, len(list_scores_inrange), 1):
        if maximum < list_scores_inrange[range_2]:                                                                      # On cherche le maximum des scores
            maximum = list_scores_inrange[range_2]
            maximum_step = range_2
    return {list_players_inrange[maximum_step], list_scores_inrange[maximum_step]}                                      # On retourne un dictionnaire qui contient le nom du gagnant et son score


"""------------------------------------------------------------------------------------------------------------------
                                                      Partie B.1
   ------------------------------------------------------------------------------------------------------------------"""


""" Il s'agit ici d'écrire une fonction qui demande à l'utilisateur si il veut continuer de jouer ou arrêter """

def continuer():
    ask = str(input("Voulez-vous continuer de joueur ? Oui / Non "))
    if ask == "Oui":
        return True
    else:
        return False


""" Il s'agit ici d'écrire une fonction qui reçoit le nom d'un joueur et gère un tour de jeu """

def tourJoueur(j):
    print("Tour : ", tour_number, "Score : ", players_dico[j], "Joueur : ", j)                                          # On affiche le numéro du tour, le nom du joueur et son score dans la partie en cours

    player_playing = continuer()                                                                                        # On demande au joueur si il désire continuer
    if player_playing:                                                                                                  # Si c'est le cas, il fait un tour de jeu
        new_score = (valeurCarte(piocheCarte(pioche, 1)) + players_dico[j])                                             # On actualise son score par le biais de la nouvelle carte piochée
        if new_score <= 21:                                                                                             # On vérifie si son score est situé entre 0 et 21
            in_range = True
        else:
            in_range = False

    players_dico[j] = new_score                                                                                         # On actualise le score du joueur dans le dictionnaire

    if not player_playing or not in_range:                                                                              # On supprime le joueur de la liste des joueurs si il a choisi d'arrêter ou si son score a dépassé 21
        players.pop(j)


"""------------------------------------------------------------------------------------------------------------------
                                                      Partie B.2
   ------------------------------------------------------------------------------------------------------------------"""
