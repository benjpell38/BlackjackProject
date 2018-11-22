""" °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
    °                                                                                                               °
    °                                 Projet de BlackJack - Benjamin Pellieux-Abram                                 °
    °                                                  UE : [INF131]                                                °
    °                                                Année : 2018-2019                                              °
    °                                                                                                               °
    °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°"""

""" On importe les modules nécéssaires à nos différentes fonctions """

from random import sample

"""" Il s'agit ici d'écrire la fonction paquet() qui permet de générer le paquet de 52 cartes nécessaire au jeu de Blackjack"""

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
    for range_1 in range(2, 11, 1):                                                                                    # On filtre ensuite les cartes de 2  à 10
        if str(range_1) in carte :
            value = range_1
    if 'valet' in carte or 'dame' in carte or 'roi' in carte:                                                           # On filtre les têtes
            value = 10
    return value                                                                                                        # On récupère la valeur de la carte en sortie


""" Il s'agit ici d'écrire une fonction qui pour un entier n reçu renvoie une pioche constituée de n paquets de cartes
avec n le nombre de joueurs de la partie """

def initPioche(n):
    pioche = []                                                                                                         # On crée une liste "Pioche" qui sera utilisée pour stocker les cartes
    for range_1 in range(0,n, 1):                                                                                      # On crée une pioche contenant n paquets de cartes
        for range_2 in range(0, len(paquet()), 1):
            pioche.append(paquet()[range_2])
    return sample(pioche, len(pioche))                                                                                  # On retourne une pioche triée aléatoirement


