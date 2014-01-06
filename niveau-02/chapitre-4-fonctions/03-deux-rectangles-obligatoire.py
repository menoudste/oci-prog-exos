##################################
# fichier 03-deux-rectangles-obligatoire.py
# nom de l'exercice : Deux rectangles
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=5
# type : obligatoire
#
# Chapitre : chapitre-4-fonctions
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

def dessin(caractere, nbLignes, nbColonnes):
   
   for loop in range(nbLignes):
      print()
      for loop in range(nbColonnes):
         print(caractere, end = "")
   
   return

caractere = 'X'

dessin(caractere, 4, 10)

caractere = 'O'

dessin(caractere, 6, 5)
