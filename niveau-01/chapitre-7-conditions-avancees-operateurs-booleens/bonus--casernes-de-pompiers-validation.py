##################################
# fichier bonus--casernes-de-pompiers-validation.py
# nom de l'exercice :  Bonus : Casernes de pompiers
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=7
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

for loop in range(int(input())):
   xmin1 = int(input())
   xmax1 = int(input())
   ymin1 = int(input())
   ymax1 = int(input())
   
   xmin2 = int(input())
   xmax2 = int(input())
   ymin2 = int(input())
   ymax2 = int(input())
   
if (xmax1 <= xmin2 or xmax2 <= xmin1) or (ymax1 <= ymin2 or ymax2 <= ymin1):
   print("NON")

else:
   print("OUI")
   




   
   

   
   
   
