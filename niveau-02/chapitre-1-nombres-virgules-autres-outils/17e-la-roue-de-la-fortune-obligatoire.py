##################################
# fichier 17e-la-roue-de-la-fortune-obligatoire.py
# nom de l'exercice : La roue de la fortune
# url : http://www.france-ioi.org/algo/task.php?idChapter=650&idTask=0&sTab=task&iOrder=26
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

nbZones = int(input())
zone1 = 0
zone2 = 0

zone1 = nbZones % 25
zone2 = zone1 + ( nbZones // 24 )

print(zone2)
