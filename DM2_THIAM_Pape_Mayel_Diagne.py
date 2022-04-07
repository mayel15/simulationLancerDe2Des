#coding:utf-8
from random import*
import numpy as np
#Remarque: mes débuts en python
#---------------------- DM2 | THIAM Pape Mayel Diagne ----------------
"""
Il s'agit de simuler une série de lancers de deux dés (un rouge et un
noir), puis de répondre à une liste de questions sur les résultats de cette
simulation.
• Nombre de tirages de la paire (3 rouge, 4 noir) ?
• Nombre de tirages d'un double ?
• Moyenne des sommes des deux dés ?
• Nombre de tirages du 5 ?
• Nombre de tirages de la somme 10 ?
• Somme obtenue le plus souvent ?
"""
#---------------------------- Sous Programmes ------------------------

def nbTirage():
    N = int(input("\nVeuillez choisir un nombre (peut être très grand) de tirages simultané des 2 dés (rouge et noir) : "))
    #N: variable de type entier , représente le nombre de tirages des dés
    while N < 0 :
        N = int(input("\nValeur entrée non valide.\n\nVeuillez choisir un nombre de tirages simultané des 2 dés (rouge et noir) : "))
    return(N) #type de la valeur retournée : entier

def initTab():
    tab = np.zeros((7,7), dtype=int)
    #tab:tableau d'entiers à 2D, 7x7, initialisé à 0 simule et recense les N tirages
    tab[0] = ([0, 1, 2, 3, 4, 5, 6])
    tab[:,0] = ([0, 1, 2, 3, 4, 5, 6])
    return(tab) #type de la valeur retournée : tableau d'entiers

def simulationTirage(N,tab):
    for cpt in range(0,N):
        deR = randint(1,6)
        deN = randint(1,6)
        tab[deR,deN] +=1
    print("\nNombre de tirages (Dé Rouge, Dé Noire) sur {} lancers.".format(N))
    print("Dé Rouge (faces suivant la verticale à gauche) et Dé Noir (faces suivant l'horizontale en haut)")
    print(tab)
    return(tab) #type de la valeur retournée : tableau d'entiers rempli

def nbTiragePair():
    #permet de savoir le nombre de tirages d'une paire
    print("\nLe nombre de tirages de quelle paire (i rouge, j noir) voulez vous savoir ? ")
    i = int(input("Entrez la valeur de la face i du dé rouge : "))
    #i:entier designe la face du dé rouge
    while i != 1 and i != 2 and i != 3 and i != 4 and i != 5 and i != 6:
        i = int(input("\nValeur entrée incorrecte.\n\nEntrez la valeur de la face i du dé rouge : "))
    j = int(input("Entrez la valeur de la face j du dé noir : "))
    #j:entier designe la face du dé noire
    while j != 1 and j != 2 and j != 3 and j != 4 and j != 5 and j != 6:
        j = int(input("\nValeur entrée incorrecte.\n\nEntrez la valeur de la face j du dé noir : "))
    #le couple (i,j) désigne une paire
    print("Le nombre de tirage de la paire ({} rouge, {} noir) est : {}".format(i,j,tab[i,j]))

def nbTirageFace():
    #permet de savoir le nombre de tirages de chaque face (les 2 confondus)
    tabTirageFace = np.zeros((2,6), dtype=int)
    #tableau d'entiers de 2x6 , 2dimensions , et permet de recenser le nombre de tirages de chaque face
    tabTirageFace[0] = ([1, 2, 3, 4, 5, 6])
    tabTirageFace[1,:] = ([ tab[1,1], tab[2,2], tab[3,3], tab[4,4], tab[5,5], tab[6,6]])
    print("\nNombre de tirages par faces.")
    print(tabTirageFace)

def nbTirageSommeFace():
    #le nombre de tirages de la somme des 2 faces chaque tirage
    tabTirageSommeFace = np.zeros((2,11), dtype=int)
    #tableau d'entiers de 2x6, 2dimensions recensant le nombre de tirages de la somme des 2 faces
    tabTirageSommeFace[0] = ([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    # sN' :  variable de type entier dont la somme des faces est égale à N' avec N' allantde 2 à 12
    s2 = tab[1,1]
    s3 = tab[1,2]+tab[2,1]
    s4 = tab[3,1]+tab[1,3]+tab[2,2]
    s5 = tab[4,1]+tab[1,4]+tab[3,2]+tab[2,3]
    s6 = tab[5,1]+tab[1,5]+tab[4,2]+tab[2,4]+tab[3,3]
    s7 = tab[6,1]+tab[1,6]+tab[2,5]+tab[5,2]+tab[4,3]+tab[3,4]
    s8 = tab[6,2]+tab[2,6]+tab[3,5]+tab[5,3]+tab[4,4]
    s9 = tab[6,3]+tab[3,6]+tab[4,5]+tab[5,4]
    s10 = tab[6,4]+tab[4,6]+tab[5,5]
    s11 = tab[6,5]+tab[5,6]
    s12 = tab[6,6]
    s = s2*2 + s3*3 + s4*4 + s5*5 + s6*6 + s7*7 + s8*8 + s9*9 + s10*10 + s11*11 + s12*12
    #s : variable de type entier, est la somme des sommes des faces
    tabTirageSommeFace[1,:] = ([ s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12])
    print("\nNombre de tirages de chaque somme des 2 faces.")
    print(tabTirageSommeFace)
    return(tabTirageSommeFace,s,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12)

def sommeObP_souv():
    # permet de donner la somme des faces obtenue le plus souvent
    if s3<=s2 and s4<=s2 and s5<=s2 and s6<=s2 and s7<=s2 and s8<=s2 and s9<=s2 and s10<=s2 and s11<=s2 and s12<=s2:
        print("\nLa somme des faces obtenue le plus souvent est : ",tabTirageSommeFace[0,0])
    if s2<=s3 and s4<=s3 and s5<=s3 and s6<=s3 and s7<=s3 and s8<=s3 and s9<=s3 and s10<=s3 and s11<=s3 and s12<=s3:
        print("\nLa somme des faces obtenue le plus souvent est : ",tabTirageSommeFace[0,1])
    if s2<s4 and s3<=s4 and s5<=s4 and s6<=s4 and s7<=s4 and s8<=s4 and s9<=s4 and s10<=s4 and s11<=s4 and s12<=s4:
        print("\nLa somme des faces obtenue le plus souvent est : ",tabTirageSommeFace[0,2])
    if s2<=s5 and s3<=s5 and s4<=s5 and s6<=s5 and s7<=s5 and s8<=s5 and s9<=s5 and s10<=s5 and s11<=s5 and s12<=s5:
        print("\nLa somme des faces obtenue le plus souvent est : ",tabTirageSommeFace[0,3])
    if s2<=s6 and s3<=s6 and s4<=s6 and s5<=s6 and s7<=s6 and s8<=s6 and s9<=s6 and s10<=s6 and s11<=s6 and s12<=s6:
        print("\nLa somme des faces obtenue le plus souvent est : ",tabTirageSommeFace[0,4])
    if s2<=s7 and s3<=s7 and s4<=s7 and s5<=s7 and s6<=s7 and s8<=s7 and s9<=s7 and s10<=s7 and s11<=s7 and s12<=s7:
        print("\nLa somme des faces obtenue le plus souvent est : ",tabTirageSommeFace[0,5])
    if s2<=s8 and s3<=s8 and s4<=s8 and s5<=s8 and s6<=s8 and s7<=s8 and s9<=s8 and s10<=s8 and s11<=s8 and s12<=s8:
        print("\nLa somme des faces obtenue le plus souvent est : ",tabTirageSommeFace[0,6])
    if s2<=s9 and s3<=s9 and s4<=s9 and s5<=s9 and s6<=s9 and s7<=s9 and s8<=s9 and s10<=s9 and s11<=s9 and s12<=s9:
        print("\nLa somme des faces obtenue le plus souvent est : ",tabTirageSommeFace[0,7])
    if s2<=s10 and s3<=s10 and s4<=s10 and s5<=s10 and s6<=s10 and s7<=s10 and s8<=s10 and s9<=s10 and s11<=s10 and s12<=s10:
        print("\nLa somme des faces obtenue le plus souvent est : ",tabTirageSommeFace[0,8])
    if s2<=s11 and s3<=s11 and s4<=s11 and s5<=s11 and s6<=s11 and s7<=s11 and s8<=s11 and s9<=s11 and s10<=s11 and s12<=s11:
        print("\nLa somme des faces obtenue le plus souvent est : ",tabTirageSommeFace[0,9])
    if s2<=s12 and s3<=s12 and s4<=s12 and s5<=s12 and s6<=s12 and s7<=s12 and s8<=s12 and s9<=s12 and s10<=s5 and s11<=s12:
        print("\nLa somme des faces obtenue le plus souvent est : ",tabTirageSommeFace[0,10])

def moySomme():
    #permet de savoir ou de retourner la moyenne des sommes des faces
    moy = s/N
    # moy : variablede type float, est la moyenne des sommes des faces
    print("\nLa moyenne des sommes des faces obtenues est : ",moy)
    return(moy)

#------------------------- Programme Principale ----------------------

print("\nIl s'agit de simuler une série de lancers de deux dés (un rouge et un noir), puis de répondre à une liste de questions sur les résultats de cette simulation.")
N = nbTirage()
tab = initTab()
tab = simulationTirage(N,tab)
nbTiragePair()
nbTirageFace()
(tabTirageSommeFace,s,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12) = nbTirageSommeFace()
sommeObP_souv()
moy = moySomme()



