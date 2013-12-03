##################################
# fichier 11-course-a-trois-jambes-obligatoire.py
# nom de l'exercice : Course à trois jambes
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=16
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

nbCoureurs = int(input())
coureurs = [0] * nbCoureurs



for numero in range (nbCoureurs):
   coureurs[numero] = int(input())

coureurs.sort()

moitie_nbCoureurs = int(nbCoureurs / 2)
petitNum = 0
grandNum = nbCoureurs - 1

for loop in range (moitie_nbCoureurs):
   print("{} {}".format(coureurs[petitNum], coureurs[grandNum]))
   petitNum += 1
   grandNum -= 1
