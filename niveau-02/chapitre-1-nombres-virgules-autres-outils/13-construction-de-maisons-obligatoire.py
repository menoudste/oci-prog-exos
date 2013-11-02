##################################
# fichier 13-construction-de-maisons-obligatoire.py
# nom de l'exercice : Construction de maisons
# url : http://www.france-ioi.org/algo/task.php?idChapter=650&idTask=0&sTab=task&iOrder=17
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

kgNec = float(input())


nbSacs = kgNec / 60

nbSacs2 = ceil(nbSacs)

print(nbSacs2 * 45)

