##################################
# fichier 07-moyenne-des-notes-obligatoire.py
# nom de l'exercice : Moyenne des notes
# url : http://www.france-ioi.org/algo/task.php?idChapter=650&idTask=0&sTab=task&iOrder=8
# type : obligatoire
#
# Chapitre : chapitre-1-nombres-virgules-autres-outils
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

nbNotes = int(input())
total = 0

for loop in range (nbNotes) :
   note = int(input()) 
   total = total + note

print(total / nbNotes)
   
