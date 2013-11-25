##################################
# fichier 07-repartition-du-poids-obligatoire.py
# nom de l'exercice : Répartition du poids
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=10
# type : obligatoire
#
# Chapitre : chapitre-2-decouverte-tableaux
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

nbCharettes = int(input())
poidsTotal = 0
numCharette = 0
numCharette2 = 0

listeCharettes = [0] * nbCharettes

for loop in range(nbCharettes):
   poids = float(input())
   listeCharettes[numCharette] = poids
   poidsTotal += listeCharettes[numCharette]
   numCharette += 1
   
poidsMoyen = poidsTotal / nbCharettes

for loop in range(nbCharettes):
   listeCharettes[numCharette2] = poidsMoyen - listeCharettes[numCharette2]
   print(listeCharettes[numCharette2])
   numCharette2 += 1
   
