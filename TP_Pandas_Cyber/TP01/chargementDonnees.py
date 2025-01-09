import pandas as pd

# Étape 1 : Charger les données depuis le fichier CSV
logs = pd.read_csv('logs.csv')

# Étape 2 : Filtrer uniquement les connexions échouées
failed_logs = logs[logs['status'] == 'failed']

# Étape 3 : Compter le nombre de tentatives échouées par adresse IP
failed_counts = failed_logs.groupby('ip_address').size()

# Étape 4 : Détecter les IPs avec plus de 2 tentatives échouées
suspicious_ips = failed_counts[failed_counts > 2]

# Étape 5 : Afficher les résultats
print("Adresses IP suspectes :")
print(suspicious_ips)
