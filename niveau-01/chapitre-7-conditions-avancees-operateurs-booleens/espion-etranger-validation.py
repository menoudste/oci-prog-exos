##################################
# fichier espion-etranger-validation.py
# nom de l'exercice :  Espion étranger
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=1
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

entree = int(input())
sortie = int(input())
nbPersonnes = int(input())
suspects = 0

for loop in range(nbPersonnes):
      dates = int(input())
      if dates <= sortie and dates >= entree:
         suspects = suspects + 1

print(suspects)
         
