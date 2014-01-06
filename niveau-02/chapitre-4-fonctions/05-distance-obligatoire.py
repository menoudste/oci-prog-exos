##################################
# fichier 05-distance-obligatoire.py
# nom de l'exercice : Distance
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=9
# type : obligatoire
#
# Chapitre : chapitre-4-fonctions
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

from math import*

def distance(x1, y1, x2, y2):
   
   distanceEuclidienne = sqrt((x2 - x1) **2 + (y2 - y1) **2)
   
   print(distanceEuclidienne)
   
   return distanceEuclidienne


distance(float(input()), float(input()), float(input()), float(input()))


      
      
   
   
