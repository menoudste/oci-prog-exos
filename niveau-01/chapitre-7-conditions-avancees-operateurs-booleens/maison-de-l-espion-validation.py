##################################
# fichier maison-de-l-espion-validation.py
# nom de l'exercice :  Maison de l'espion
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=2
# type : validation
#
# Nom du chapitre : 
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

xMinZone = int(input())
xMaxZone = int(input())
yMinZone = int(input())
yMaxZone = int(input())
nbMaisons = int(input())
numMaisons = 0

for loop in range(nbMaisons):
   xMaison = int(input())
   yMaison = int(input())
   if xMaison >= xMinZone and xMaison <= xMaxZone:
      if yMaison >= yMinZone and yMaison <= yMaxZone:
         numMaisons = numMaisons + 1

print(numMaisons)
   
   
