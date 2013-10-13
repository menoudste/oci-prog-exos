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
nbEtages = 1
total = 0
cote = 1


while nbPierresDispo > total :
   nbPierres = cote**2
   cote = cote + 1
   nbEtages = nbEtages + 1
   total = total + nbPierres
   
if nbPierresDispo > 1:   
    total = total - ((cote-1)**2)#Sinon, un étage de pierres en trop est comptabilisé

    print(nbEtages - 2) #Sinon, il y aurait 2 étages de trop
    print(total)

if nbPierresDispo == 1 :
    print("1")
    print("1")

if nbPierresDispo <= 0 :
    print("0")
    print("0")

