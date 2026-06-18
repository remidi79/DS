# Lancer l'exercice en local

Depuis Windows PowerShell, placez-vous dans ce dossier puis exécutez :

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python generate_dataset.py
jupyter notebook
```

Ouvrez ensuite :

```text
candidate_notebook.ipynb
```

Le fichier de données est déjà fourni, mais vous pouvez le régénérer avec :

```powershell
python generate_dataset.py
```

Il sera créé ici :

```text
data/credit_scoring_interview.csv
```
