##################################
# fichier departement-d-architecture--construction-d-une-pyramide-validation.py
# nom de l'exercice :  Département d'architecture : construction d'une pyramide
# url : http://www.france-ioi.org/algo/task.php?idChapter=649&idTask=0&sTab=task&iOrder=6
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

nbPierresDispo = int(input())
nbPierres = 0
nbEtages = 0


while nbPierresDispo > (nbPierres + nbEtages**2):
   nbEtages += 1
   nbPierres = nbPierres + nbEtages**2
   
print(nbEtages)
print(nbPierres)



