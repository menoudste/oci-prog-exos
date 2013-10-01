##################################
# fichier nombre-de-personnes-a-la-fete-validation.py
# nom de l'exercice :  Nombre de personnes à la fête
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=6
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

nbPersonnes = int(input())
présents = 0
nbMax = 0


for loop in range(2*nbPersonnes):
   comptage = int(input())
   
   if comptage > 0:
      présents = présents + 1
      
      if présents > nbMax:
         nbMax = présents
      
   
     
   else:
      présents = présents - 1

print(nbMax)

   
