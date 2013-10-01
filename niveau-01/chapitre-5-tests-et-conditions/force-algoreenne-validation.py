##################################
# fichier force-algoreenne-validation.py
# nom de l'exercice :  Force algoréenne
# url : http://www.france-ioi.org/algo/task.php?idChapter=646&idTask=0&sTab=task&iOrder=1
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
total1 = 0
total2 = 0

for loop in range(nbPersonnes):
   total1 = total1 + int(input())
   total2 = total2 + int(input())
   
   

if total1 > total2:
   print("L'équipe 1 a un avantage")

if total2 > total1:
   print("L'équipe 2 a un avantage")
   
print("Poids total pour l'équipe 1 :", end=" ")
print(total1)
print("Poids total pour l'équipe 2 :", end=" ")
print(total2)


