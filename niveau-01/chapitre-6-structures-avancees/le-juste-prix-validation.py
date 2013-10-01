##################################
# fichier le-juste-prix-validation.py
# nom de l'exercice :  Le juste prix
# url : http://www.france-ioi.org/algo/task.php?idChapter=647&idTask=0&sTab=task&iOrder=8
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

nbMarchands = int(input())
position = 0
prixMin = 0
positionOpti = 0

for loop in range(1):
   position = position + 1
   prix = int(input())
   prixMin = prix
   prix = prix - prixMin
     
   if prix >= 0:
      positionOpti = position
        
for loop in range(nbMarchands-1):
   position = position + 1
   prix = int(input())
   prix = prixMin - prix
   
   if prix >= 0:
      positionOpti = position
      prixMin = prix
      
   
print(positionOpti)
