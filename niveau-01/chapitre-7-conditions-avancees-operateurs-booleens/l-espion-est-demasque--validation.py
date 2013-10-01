##################################
# fichier l-espion-est-demasque--validation.py
# nom de l'exercice :  L'espion est démasqué !
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=14
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

criteres = 0
nbPersonnes = int(input())

for loop in range(nbPersonnes):
   taille = int(input())
   age  = int(input())
   poids  = int(input())
   cheval = int(input())
   cheveux = int(input())
   
   if taille > 178 and taille < 182:
      criteres = criteres + 1
   if age >= 34:
      criteres = criteres + 1
   if poids < 70:
      criteres = criteres + 1
   if cheval == 0:
      criteres = criteres + 1
   if cheveux == 1:
      criteres = criteres + 1

   if criteres == 5:
      print("Très probable")
   elif criteres == 4 or criteres == 3:
      print("Probable")
   elif criteres == 0:
      print("Impossible")
   else:
      print("Peu probable")
   
      
         
