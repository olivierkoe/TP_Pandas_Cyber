# TP_Pandas_Cyber
## Détection de Tentatives de Connexion Échouées

### Objectif
Ce projet vise à analyser des fichiers de logs pour détecter les adresses IP suspectes ayant un nombre élevé de tentatives de connexion échouées. Cela permet d’identifier des activités potentiellement malveillantes et d’améliorer la sécurité informatique.

---

## Contenu du projet

### 1. Charger les données de logs
Nous utilisons un fichier CSV contenant les informations suivantes :
- **timestamp** : Date et heure de la tentative de connexion.
- **ip_address** : Adresse IP de l’utilisateur.
- **status** : Statut de la tentative (succès ou échec).

#### Exemple de fichier `logs.csv`
```csv
timestamp,ip_address,status
2025-01-05 12:34:56,192.168.1.10,success
2025-01-05 12:35:01,192.168.1.11,failed
2025-01-05 12:35:05,192.168.1.11,failed
2025-01-05 12:35:10,192.168.1.11,failed
2025-01-05 12:36:00,192.168.1.12,success


### Analyse des logs avec Python
Le script Python repose sur la bibliothèque pandas pour effectuer les opérations suivantes :

Charger le fichier CSV contenant les logs.
Filtrer les lignes ayant le statut "failed".
Compter le nombre de tentatives échouées par adresse IP.
Identifier les adresses IP ayant plus de 2 tentatives échouées.
Afficher la liste des adresses IP suspectes avec leur nombre de tentatives échouées.

## Prérequis
Bibliothèques Python nécessaires
pandas : Pour manipuler et analyser les données.
Installation des dépendances
Assurez-vous d’avoir Python installé, puis utilisez pip pour installer pandas :

pip install pandas


## Fichiers inclus
logs.csv : Exemple de fichier de logs.
analyze_logs.py : Script Python pour analyser les logs.