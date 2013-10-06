##################################
# fichier zones-de-couleurs-validation.py
# nom de l'exercice :  Zones de couleurs
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=15
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

nbPersonnes = int(input())


for loop in range(nbPersonnes):
   x = int(input())
   y = int(input())
   
   dehorsfeuille = ( x > 90 or x < 0) or ( y > 70 or y < 0)
   rouge = ( x > 15 or x < 45) or ( y > 60 or y < 90 ) or ( x > 60 or x < 85 ) or ( y > 60 or y < 85)
   bleu = ( x > 10 or x < 85 ) or ( y > 10 or y < 55 )
   jaune = ( x > 0 or x < 90 ) or ( y > 0 or y < 70 )  
   
   if dehorsfeuille :
      print("En dehors de la feuille")
   
   else:
      if bleu and ( not (jaune) ):
         print("Dans une zone bleue") 
         
      else:
         if rouge:
            print("Dans une zone rouge")
            
         else:
            print("Dans une zone jaune")
   

