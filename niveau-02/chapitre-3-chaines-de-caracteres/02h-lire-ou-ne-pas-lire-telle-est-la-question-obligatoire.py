##################################
# fichier 02h-lire-ou-ne-pas-lire-telle-est-la-question-obligatoire.py
# nom de l'exercice : Lire ou ne pas lire, telle est la question
# url : http://www.france-ioi.org/algo/task.php?idChapter=595&idTask=0&sTab=task&iOrder=10
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

nbLivres = int(input())
livre = input()

print(livre)
longueurTitreAvant = len(livre)

for loop in range (nbLivres - 1): # Car le premier livre est défini avant 
                                  # la première entrée dans la boucle
   livre = input()
   longueurTitre = len(livre)
   
   if longueurTitre > longueurTitreAvant:
      print(livre)
      longueurTitreAvant = longueurTitre
