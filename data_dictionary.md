# Dictionnaire des données

Ce jeu de données est synthétique. Il sert uniquement à l'entretien et ne contient aucune donnée réelle.

Chaque ligne représente une demande de prêt. Certaines anomalies ont été laissées volontairement pour permettre une discussion réaliste sur la qualité des données.

| Colonne | Description |
| --- | --- |
| `customer_id` | Identifiant client synthétique. Un même client peut apparaître plusieurs fois. |
| `application_date` | Date de soumission de la demande de prêt. Les lignes ne sont pas triées chronologiquement. |
| `age` | Âge du client en années. Quelques valeurs peuvent sembler peu plausibles. |
| `income` | Revenu annuel déclaré. |
| `employment_years` | Nombre d'années d'emploi déclarées. |
| `loan_amount` | Montant du prêt demandé. |
| `loan_duration_months` | Durée du prêt demandée, en mois. |
| `existing_debt` | Dette existante estimée au moment de la demande. |
| `debt_to_income` | Ratio dette/revenu approximatif. |
| `credit_history_months` | Ancienneté de l'historique de crédit, en mois. |
| `number_of_previous_loans` | Nombre de prêts précédents connus. |
| `missed_payments_12m` | Nombre de paiements manqués sur les 12 derniers mois. |
| `region` | Région du client. |
| `channel` | Canal de demande : agence, web, mobile ou courtier. |
| `collection_status_after_90d` | Statut de recouvrement enregistré autour de la période de suivi à 90 jours. |
| `default_90d` | Cible à prédire : 1 si le client a fait défaut dans les 90 jours, sinon 0. |

## Points d'attention

Avant de modéliser, pensez à vérifier :

- les valeurs manquantes ;
- les doublons ;
- les valeurs aberrantes ;
- la distribution de la cible ;
- la cohérence des dates ;
- la disponibilité réelle des variables au moment de la décision.
