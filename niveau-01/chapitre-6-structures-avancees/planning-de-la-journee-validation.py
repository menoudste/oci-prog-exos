##################################
# fichier planning-de-la-journee-validation.py
# nom de l'exercice :  Planning de la journée
# url : http://www.france-ioi.org/algo/task.php?idChapter=647&idTask=0&sTab=task&iOrder=2
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

position = int(input())
nbrvillages = int(input())
villagepossible = 0


for loop in range(nbrvillages):
   distancevillage = int(input())
   distancevillage = position - distancevillage
   if -50 <= distancevillage <= 50:
      villagepossible = villagepossible + 1
      
print(villagepossible)
