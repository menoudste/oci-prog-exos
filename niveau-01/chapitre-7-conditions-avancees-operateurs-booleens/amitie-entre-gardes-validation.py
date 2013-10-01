##################################
# fichier amitie-entre-gardes-validation.py
# nom de l'exercice :  Amitié entre gardes
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=5
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

debut1 = int(input())
fin1 = int(input())
debut2 = int(input())
fin2 = int(input())

if (debut2 <= fin1 and fin2 >= debut1) or (debut1 <= fin2 and debut2 <= fin1):
   print("Amis")

else:
   print("Pas amis")
