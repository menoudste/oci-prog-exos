##################################
# fichier 01-code-secret-deux-fois-obligatoire.py
# nom de l'exercice : Code secret deux fois
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=1
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

script = 0

def code():

      print("Entrez le code :")
      
      script = int(input())
      
      while script != 4242 :
         script = int(input())
         print("Entrez le code :")
      
      
      return script
      
code()

print("Encore une fois.")

code()

print("Bravo.")
