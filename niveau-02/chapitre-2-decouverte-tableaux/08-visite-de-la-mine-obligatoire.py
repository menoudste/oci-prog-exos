##################################
# fichier 08-visite-de-la-mine-obligatoire.py
# nom de l'exercice : Visite de la mine
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=11
# type : obligatoire
#
# Chapitre : chapitre-2-decouverte-tableaux
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

nbDeplacements = int(input())
numDeplacement = nbDeplacements - 1

itineraire = [0] * nbDeplacements

for loop in range(nbDeplacements):
   typeDeplacement = int(input())
   
   if typeDeplacement == 3 :
      itineraire[numDeplacement] = 3
      numDeplacement -= 1
      
   elif typeDeplacement == 1 :
      itineraire[numDeplacement] = 2
      numDeplacement -= 1
      
   elif typeDeplacement == 2 :
      itineraire[numDeplacement] = 1
      numDeplacement -= 1
   
   elif typeDeplacement == 4 :  
      itineraire[numDeplacement] = 5
      numDeplacement -= 1
   
   elif typeDeplacement == 5 :  
      itineraire[numDeplacement] = 4
      numDeplacement -= 1
      
for numDeplacements2 in range(nbDeplacements) :
   print(itineraire[numDeplacements2])
    
      


  
   
   
