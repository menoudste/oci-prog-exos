##################################
# fichier departement-de-chimie--melange-explosif-validation.py
# nom de l'exercice :  Département de chimie : mélange explosif
# url : http://www.france-ioi.org/algo/task.php?idChapter=649&idTask=0&sTab=task&iOrder=7
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

nbMesuresEff = 0


nbMesures = int(input())
tempMin = int(input())
tempMax = int(input())
temp = int(input())

if temp > tempMax or temp < tempMin:
   print("Alerte !!")

while temp >= tempMin and temp <= tempMax and nbMesuresEff <= nbMesures:
   print("Rien à signaler")
   nbMesuresEff += 1
   temp = int(input())
   
if temp > tempMax or temp < tempMin:
   print("Alerte !!")

   

   

   
   
   

   

   
   
