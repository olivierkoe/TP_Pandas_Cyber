# TPs Python/Pandas pour la Cybersécurité

Ce projet regroupe deux TPs axés sur l'analyse et la visualisation de données liées à la cybersécurité. Les scripts utilisent Python et Pandas pour traiter des fichiers CSV et fournir des analyses claires et exploitables.

---

## Contenu des TPs

### TP01 : Détection de Tentatives de Connexion Échouées
**Description** :  
Ce TP analyse des logs de connexions pour identifier les adresses IP suspectes ayant effectué un grand nombre de tentatives échouées.  
**Objectifs** :
1. Charger un fichier de logs CSV contenant des informations de connexion.
2. Filtrer les tentatives échouées.
3. Compter les tentatives échouées par adresse IP.
4. Identifier et afficher les IP avec plus de 2 échecs.

**Fichier à analyser** : `logs.csv`  
Structure du fichier :  
```csv
timestamp,ip_address,status
2025-01-05 12:34:56,192.168.1.10,success
2025-01-05 12:35:01,192.168.1.11,failed
```	
## Commande pour lancer le TP01

 python .\chargementDonnees.py


### TP02 : Analyse des Logs de Connexions

**Description :**
Ce TP analyse et visualise des incidents de cybersécurité enregistrés dans un fichier CSV pour en comprendre la fréquence et l’évolution dans le temps.
**Objectifs** :

1. harger un fichier d’incidents CSV.
2. Nettoyer les données en gérant les valeurs manquantes.
3. Effectuer des analyses (par type, date et lieu).
4. Visualiser les résultats (diagrammes en barres, courbes d'évolution).

**Fichier à analyser** : `incidents.csv`
Structure du fichier :
```csv
Date,Type_Incident,Lieu,Gravité
2023-01-15,Cyberattaque,Paris,Moyenne
2023-02-20,Vol de données,Lyon,Élevée
```	

## Commande pour lancer le TP02

python .\analyseDonnees.py

### Dépendances nécessaires ###
Les scripts nécessitent les bibliothèques Python suivantes :

pandas : Pour manipuler et analyser les données.
matplotlib : Pour générer les visualisations.
Installation des dépendances :
Assurez-vous d’avoir Python 3.13.0 installé, puis utilisez la commande suivante pour installer les bibliothèques nécessaires :

pip install pandas matplotlib