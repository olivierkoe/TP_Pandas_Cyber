# Importer les bibliothèques nécessaires
import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV contenant les données
df = pd.read_csv('incidents.csv')

# Afficher les premières lignes du DataFrame pour un aperçu des données
print(df.head())

# Afficher des informations sur les colonnes et les types de données pour mieux comprendre la structure du DataFrame
print(df.info())

# Résumé statistique des colonnes numériques (si disponibles), comme les moyennes et les quartiles
print(df.describe())

# Vérifier et afficher le nombre de valeurs manquantes dans chaque colonne
print(df.isnull().sum())

# Remplir les valeurs manquantes avec le texte 'Inconnu' dans toutes les colonnes
df.fillna('Inconnu', inplace=True)

# Supprimer les lignes contenant des valeurs manquantes (optionnellement si nécessaire)
df.dropna(inplace=True)

# Analyse des données : Calculer le nombre d'incidents par type
# La méthode value_counts compte les occurrences de chaque type d'incident
incidents_par_type = df['Type_Incident'].value_counts()
print(incidents_par_type)

# Convertir la colonne 'Date' en type datetime pour permettre des analyses temporelles
df['Date'] = pd.to_datetime(df['Date'])

# Grouper les données par mois et compter le nombre d'incidents dans chaque période (par mois)
incidents_par_mois = df.groupby(df['Date'].dt.to_period('M')).size()
print(incidents_par_mois)

# Analyse des données : Fréquence des incidents par lieu
# La méthode value_counts compte les occurrences pour chaque lieu d'incident
incidents_par_lieu = df['Lieu'].value_counts()
print(incidents_par_lieu)

# Visualisation : Diagramme en barres pour le nombre d'incidents par type
incidents_par_type.plot(kind='bar', title='Nombre d\'incidents par type')
plt.xlabel('Type d\'incident')  # Légende de l'axe X
plt.ylabel('Nombre d\'incidents')  # Légende de l'axe Y
plt.show()

# Visualisation : Graphique de l'évolution des incidents dans le temps (par mois)
incidents_par_mois.plot(title='Évolution des incidents dans le temps')
plt.xlabel('Temps (Année, Mois)')  # Légende de l'axe X
plt.ylabel('Nombre d\'incidents')  # Légende de l'axe Y
plt.show()

# Visualisation : Diagramme en barres pour la fréquence des incidents par lieu
incidents_par_lieu.plot(kind='bar', title='Fréquence des incidents par lieu')
plt.xlabel('Lieu')  # Légende de l'axe X
plt.ylabel('Nombre d\'incidents')  # Légende de l'axe Y
plt.show()

# Exporter les résultats de l'analyse dans un fichier CSV pour sauvegarder les données traitées
df.to_csv('resultats_analyse.csv', index=False)
