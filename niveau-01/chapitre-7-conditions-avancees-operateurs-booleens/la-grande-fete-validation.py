##################################
# fichier la-grande-fete-validation.py
# nom de l'exercice :  La grande fête
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=11
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

debut = int(input())
fin = int(input())
nbInvites = int(input())
nbsuspects = 0

for loop in range(nbInvites):
   debutinvite = int(input())
   fininvite = int(input())
   
   if ( not (debutinvite > fin)) and ( not (fininvite < debut)) :
      nbsuspects = nbsuspects + 1

print(nbsuspects)
