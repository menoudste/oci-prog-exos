##################################
# fichier personne-disparue-validation.py
# nom de l'exercice :  Personne disparue
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=9
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

numPersonne = int(input())
tailleListe = int(input())


indice = 0

for loop in range(tailleListe):
   numListe  = int(input())
   if numListe == numPersonne :
      indice = indice + 1

if indice > 0:
   print("Sorti de la ville")

else:
   print("Encore dans la ville")
      
      
      
      
      
