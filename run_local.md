# Lancement local avec Windows PowerShell

Depuis le dossier `01_candidate_visible` :

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python generate_dataset.py
jupyter notebook
```

Puis ouvrir :

- `candidate_notebook.ipynb`

Le jeu de données généré sera enregistré ici :

```text
data/credit_scoring_interview.csv
```
