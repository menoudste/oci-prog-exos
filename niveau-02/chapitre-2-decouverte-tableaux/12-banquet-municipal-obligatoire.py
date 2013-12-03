##################################
# fichier 12-banquet-municipal-obligatoire.py
# nom de l'exercice : Banquet municipal
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=17
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

nbInvites = int(input())
nbChange = int(input())
positions = [0] * nbInvites 

for place in range (nbInvites):
   positions[place] = int(input()) 

for loop in range (nbChange):
   changement1 = int(input())
   changement2 = int(input())

   aChanger1 = positions[changement1]
   aChanger2 = positions[changement2]

   positions[changement1] = aChanger2
   positions[changement2] = aChanger1

for i in range (nbInvites):
   print(positions[i])






   
