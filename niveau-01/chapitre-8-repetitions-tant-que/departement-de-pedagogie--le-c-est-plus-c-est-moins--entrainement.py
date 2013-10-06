##################################
# fichier departement-de-pedagogie--le-c-est-plus-c-est-moins--entrainement.py
# nom de l'exercice :  Département de pédagogie : le c'est plus, c'est moins !
# url : http://www.france-ioi.org/algo/task.php?idChapter=649&idTask=0&sTab=task&iOrder=5
# type : entrainement
#
# Nom du chapitre : 
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

nombre = int(input())
prop = 0
essais = 1

while prop != nombre:
   prop = int(input())
   if prop > nombre:
      print("c'est moins")
      essais = essais + 1
   
   if prop < nombre:
      print("c'est plus")
      essais = essais + 1



print("Nombre d'essais nécessaires :")
print(essais)
      
