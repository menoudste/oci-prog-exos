##################################
# fichier 02-deux-codes-secrets-obligatoire.py
# nom de l'exercice : Deux codes secrets
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=3
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

def code(script) :
      
      scriptTest = 0
      
      while scriptTest != script :
         scriptTest = int(input())
         print("Entrez le code :")
      
      
      return script
      
code(4242)

print("Premier code bon.")

code(2121)

print("Bravo.")
