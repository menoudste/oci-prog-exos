##################################
# fichier 04e-inscription-d-etudiants-obligatoire.py
# nom de l'exercice : Inscription d’étudiants
# url : http://www.france-ioi.org/algo/task.php?idChapter=595&idTask=0&sTab=task&iOrder=22
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

nom = input()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lettre = 0

while alphabet[lettre] != nom[0]:

   if alphabet[lettre] == nom[0]:
      idLettre = lettre

   lettre += 1


lettre -= 1 #Sinon, "lettre" a été incrémenté une fois de trop.

if lettre <=5 :
   print(1)
   
elif lettre <= 15 :
   print(2)
   
else :
   print(3)
