##################################
# fichier 04i-analyse-d-une-langue-obligatoire.py
# nom de l'exercice : Analyse d’une langue
# url : http://www.france-ioi.org/algo/task.php?idChapter=595&idTask=0&sTab=task&iOrder=26
# type : obligatoire
#
# Chapitre : chapitre-3-chaines-de-caracteres
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

lettre = input()
nbLignes = int(input())
compteur = 0


for loop in range(nbLignes) :

   ligne = input()
   longueur = len(ligne)
   
   for alphabet in range(len(ligne)):
   
      if ligne[alphabet] == lettre[0]:
         compteur += 1
      
print(compteur)
   
