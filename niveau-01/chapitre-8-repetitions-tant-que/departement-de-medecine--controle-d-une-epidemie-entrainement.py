##################################
# fichier departement-de-medecine--controle-d-une-epidemie-entrainement.py
# nom de l'exercice :  Département de médecine : contrôle d'une épidémie
# url : http://www.france-ioi.org/algo/task.php?idChapter=649&idTask=0&sTab=task&iOrder=1
# type : entrainement
#
# Nom du chapitre : 
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

nbHabitants = int(input())
nbMalades = 1
jour = 1




while nbMalades < nbHabitants:
   nbMalades = nbMalades + nbMalades * 2
   jour = jour + 1


print(jour)



