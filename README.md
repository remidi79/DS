# Cas pratique - Data Scientist Finance

Vous allez travailler sur un mini-cas de notation crédit. Le but n'est pas de produire le meilleur modèle possible en 15 minutes, mais de montrer comment vous réfléchissez face à un jeu de données imparfait.

## Situation

Une équipe de crédit à la consommation veut mieux identifier les demandes de prêt qui risquent de faire défaut dans les 90 jours suivant l'approbation.

Vous disposez d'un jeu de données synthétique contenant des informations sur les clients, les demandes de prêt, l'historique crédit et le canal de souscription.

Comme dans un vrai projet, les données ne sont pas parfaitement propres. Certaines valeurs peuvent manquer, certaines lignes peuvent être douteuses, et toutes les variables ne sont pas forcément utilisables telles quelles.

## Temps

L'entretien dure 30 minutes :

- 15 minutes pour explorer le jeu de données et préparer votre approche ;
- 15 minutes pour discuter de vos choix techniques et métier.

Vous n'avez pas besoin de tout finir. Une analyse claire, structurée et honnête vaut mieux qu'un modèle complexe construit trop vite.

## Ce que vous pouvez faire

Commencez par ouvrir `candidate_notebook.ipynb`, puis avancez dans les sections proposées :

- chargement des données ;
- exploration rapide ;
- contrôles de qualité ;
- construction de variables ;
- proposition de modèle ;
- choix des métriques ;
- interprétation métier.

Si vous avez le temps, vous pouvez entraîner un modèle simple de départ. Sinon, expliquez clairement ce que vous feriez et pourquoi.

## Ce qu'on attend surtout

Pendant la discussion, soyez prêt à expliquer :

- les premiers contrôles que vous avez faits ;
- les problèmes de qualité de données repérés ;
- les variables que vous utiliseriez, excluriez ou vérifieriez davantage ;
- le type de modèle que vous choisiriez en premier ;
- les métriques adaptées à un problème de défaut rare ;
- la manière d'expliquer un refus de crédit à un interlocuteur non technique ;
- les grandes étapes pour passer d'un carnet Jupyter à une mise en production.

## Règles du jeu

- Aucune donnée réelle n'est utilisée.
- Internet n'est pas nécessaire.
- Un modèle simple suffit.
- Le raisonnement compte plus que la performance brute.
- Ne supposez pas que toutes les colonnes sont disponibles au moment de la décision crédit.
