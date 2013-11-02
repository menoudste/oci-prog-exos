##################################
# fichier 12-augmentation-de-la-population-obligatoire.py
# nom de l'exercice : Augmentation de la population
# url : http://www.france-ioi.org/algo/task.php?idChapter=650&idTask=0&sTab=task&iOrder=16
# type : obligatoire
#
# Chapitre : chapitre-1-nombres-virgules-autres-outils
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

from math import *

popActu = int(input())
chaPrev = float(input())
popPrev = 0

popPrev = popActu + ((chaPrev / 100) * popActu)

popPrev2 = floor(popPrev)

print(popPrev2)







