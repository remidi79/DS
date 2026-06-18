# Exercice d'entretien technique - Data Scientist Finance

## Contexte métier

Vous travaillez avec une équipe de crédit à la consommation. Le métier souhaite améliorer le processus d'analyse des demandes de prêt en identifiant les clients susceptibles de faire défaut dans les 90 jours suivant l'approbation du crédit.

Le jeu de données est synthétique. Il représente des demandes de prêt avec des informations de profil client, d'historique de crédit, de caractéristiques du prêt et de canal de demande.

Votre objectif n'est pas de construire un modèle parfait. L'objectif est de montrer votre raisonnement sur la qualité des données, la disponibilité des variables, la stratégie de validation, l'évaluation du modèle et l'interprétation métier.

## Temps prévu

Temps total d'entretien : 30 minutes.

- 15 minutes : travail individuel sur le jeu de données.
- 15 minutes : discussion technique à partir de votre approche.

Vous n'êtes pas censé tout terminer. Priorisez un raisonnement clair et expliquez vos arbitrages.

## Consignes candidat

1. Générer le jeu de données s'il n'est pas déjà présent :

   ```powershell
   python generate_dataset.py
   ```

2. Ouvrir le carnet Jupyter `candidate_notebook.ipynb`.
3. Parcourir les sections dans l'ordre :
   - Chargement des données
   - EDA rapide
   - Contrôles de qualité des données
   - Construction de variables
   - Proposition de modèle
   - Évaluation
   - Interprétation métier
4. Vous pouvez utiliser toute approche Python standard avec les packages listés dans `requirements.txt`.

## Livrables attendus

Pendant l'entretien, soyez prêt à expliquer :

- Ce que vous avez vérifié en premier et pourquoi.
- Les problèmes de qualité de données identifiés.
- Les variables que vous utiliseriez ou excluriez, y compris les variables suspectes.
- Une approche de modélisation raisonnable.
- La métrique qui compte le plus et pourquoi.
- Comment expliquer les résultats à des interlocuteurs crédit risque, produit ou conformité.
- Comment passer d'un carnet Jupyter à une mise en production.

## Règles

- Aucune donnée réelle n'est utilisée dans cet exercice.
- L'accès internet n'est pas nécessaire.
- Un modèle de référence simple suffit.
- Une analyse partielle avec un raisonnement solide vaut mieux qu'un modèle complexe fait trop vite.
- Ne supposez pas que toutes les colonnes sont utilisables. Identifiez et justifiez les variables potentiellement problématiques.
