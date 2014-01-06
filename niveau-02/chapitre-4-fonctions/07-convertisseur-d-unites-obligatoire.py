##################################
# fichier 07-convertisseur-d-unites-obligatoire.py
# nom de l'exercice : Convertisseur d'unités
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=14
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

N = int(input())

def conversion():
   
   for caractere in range(N):
      valeur = input()
      
      if valeur[-1] == 'm':
         valeur = valeur[:-1]
         valeur = float(valeur)
         multiplication = 1 / 0.3048
         valeur *= multiplication
         valeur = round(valeur, 6)
         valeur = str(valeur)
         print(valeur + " p")
      
      if valeur[-1] == 'g':
         valeur = valeur[:-1]
         valeur = float(valeur)
         multiplication = 0.002205 / 1
         valeur *= multiplication
         valeur = round(valeur, 6)
         valeur = str(valeur)
         print(valeur + " l")
      
      if valeur[-1] == 'c':
         valeur = valeur[:-1]
         valeur = float(valeur)
         valeur = 32+(1.8 * valeur)
         valeur = round(valeur, 6)
         valeur = str(valeur)
         print(valeur + " f")
      
   return valeur
   
   
         
         
         
        
         
conversion()
