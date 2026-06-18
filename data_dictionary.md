# Dictionnaire des données

Ce jeu de données est entièrement synthétique et a été créé pour un exercice d'entretien technique.

| Colonne | Type | Description |
| --- | --- | --- |
| `customer_id` | Entier | Identifiant client synthétique. Certains identifiants dupliqués sont volontairement présents. |
| `application_date` | Date au format texte | Date de soumission de la demande de prêt. Les dates ne sont pas triées et contiennent quelques anomalies. |
| `age` | Entier | Âge du client en années. Contient quelques valeurs aberrantes peu plausibles. |
| `income` | Nombre décimal | Revenu annuel déclaré. Contient des valeurs manquantes et des valeurs aberrantes. |
| `employment_years` | Nombre décimal | Nombre d'années d'emploi. Contient des valeurs manquantes et quelques valeurs peu plausibles. |
| `loan_amount` | Nombre décimal | Montant du prêt demandé. Contient quelques valeurs très élevées. |
| `loan_duration_months` | Entier | Durée du prêt demandée, en mois. |
| `existing_debt` | Nombre décimal | Dette existante estimée au moment de la demande. Contient des valeurs manquantes. |
| `debt_to_income` | Nombre décimal | Ratio dette/revenu approximatif, dérivé de la dette, du montant du prêt et du revenu. |
| `credit_history_months` | Nombre décimal | Ancienneté de l'historique de crédit, en mois. Contient des valeurs manquantes. |
| `number_of_previous_loans` | Entier | Nombre de prêts précédents dans l'historique de crédit du client. |
| `missed_payments_12m` | Entier | Nombre de paiements manqués sur les 12 derniers mois. |
| `region` | Catégoriel | Région du client. Contient des valeurs manquantes. |
| `channel` | Catégoriel | Canal de demande : agence, web, mobile ou courtier. Contient des valeurs manquantes. |
| `collection_status_after_90d` | Catégoriel | Statut de recouvrement enregistré autour de la période de suivi à 90 jours. |
| `default_90d` | Entier | Variable cible : 1 si le client a fait défaut dans les 90 jours, sinon 0. |
