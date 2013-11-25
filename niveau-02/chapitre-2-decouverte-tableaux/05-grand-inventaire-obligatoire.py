##################################
# fichier 05-grand-inventaire-obligatoire.py
# nom de l'exercice : Grand inventaire
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=7
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

compte = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
numingredient = -1

nbTransactions = int(input())

for loop in range(nbTransactions):
    stock = 0
    ingredient = int(input())
    operation = int(input())
    compte[ingredient-1] = compte[ingredient-1] + operation
    
for loop in range(10):
   numingredient += 1
   print(compte[numingredient])
