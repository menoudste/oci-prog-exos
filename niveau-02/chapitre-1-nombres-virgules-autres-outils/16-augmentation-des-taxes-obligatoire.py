##################################
# fichier 16-augmentation-des-taxes-obligatoire.py
# nom de l'exercice : Augmentation des taxes
# url : http://www.france-ioi.org/algo/task.php?idChapter=650&idTask=0&sTab=task&iOrder=20
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

taxeAvant = float(input())
taxeActuelle = float(input())
prixAvant = float(input())
prixAvantSansTaxe = 0
prixApres = 0

prixAvantSansTaxe = prixAvant / (100+taxeAvant) * 100

prixApres = prixAvantSansTaxe + ((taxeActuelle / 100) * prixAvantSansTaxe)
prixApres = round(prixApres, 2)

print(prixApres)


