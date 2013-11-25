##################################
# fichier 09-journee-des-cadeaux-obligatoire.py
# nom de l'exercice : Journée des cadeaux
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=14
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

from math import*

nbHabitants = int(input())
moyenne = 0
fortune = [0] * nbHabitants


if nbHabitants % 2 == 0 :
   for indice in range(nbHabitants) :
      fortune[indice] = int(input())
   
   fortune.sort()
   
   moyenne = (fortune[nbHabitants / 2 - 1] + fortune[nbHabitants / 2]) / 2
   print(moyenne)

else : 
   for indice in range(nbHabitants):
      fortune[indice] = int(input())
   
   fortune.sort()
      
   moyenne = (fortune[(nbHabitants - 1) / 2])

   print(moyenne)
      
   
