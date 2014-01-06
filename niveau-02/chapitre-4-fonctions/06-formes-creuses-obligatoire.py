##################################
# fichier 06-formes-creuses-obligatoire.py
# nom de l'exercice : Formes creuses
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=13
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

def forme(ligne, lignesRectangle, colonnesRectangle, lignesTri):
   
   # Ligne
   for loop in range(ligne):
      print("X", end = "")
   
   print()
   print()
   
   #Rectangle creux
   for loop in range(colonnesRectangle):
      print("#", end = "")
   
   print()
   
   # Dans le cas où il y aurait plus qu'une seule colonne
   if colonnesRectangle > 1:
      for loop in range(lignesRectangle - 2):
         print("#" + " "*(colonnesRectangle - 2) + "#",)
     
      for loop in range(colonnesRectangle):
         print("#", end = "")
   
   # Dans le cas où il n'y aurait qu'une seule colonne
   if colonnesRectangle == 1:
   
      for loop in range(lignesRectangle - 1): # Sinon il y un "#" de trop, la première ligne est déjà rajoutée plus haut
         print("#")
         
   
   print()
   print()
   
   #Triangle
   print("@")
   
   for nbRepetitions in range(lignesTri - 2):
      print("@" + " " * nbRepetitions + "@")
   
   for loop in range(lignesTri):
      print("@", end = "")
      

forme(int(input()), int(input()), int(input()), int(input()))
