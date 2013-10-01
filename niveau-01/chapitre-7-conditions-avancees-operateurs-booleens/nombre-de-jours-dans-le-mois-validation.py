##################################
# fichier nombre-de-jours-dans-le-mois-validation.py
# nom de l'exercice :  Nombre de jours dans le mois
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=4
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

M1 = 30
M2 = 30
M3 = 30
M4 = 31
M5 = 31
M6 = 31
M7 = 30
M8 = 30
M9 = 30
M10 = 31
M11 = 29

M = int(input())

if (M >= 1 and M <=3) or (M >= 7 and M <= 9):
   print("30")

if (M >= 4 and M <=6) or (M == 10):
   print("31")
   
if (M ==11):
   print("29")
