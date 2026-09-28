# University Budget App

Application Streamlit pour gérer le budget universitaire avec persistance JSON.

## Structure

- `.github/workflows/ci.yml` : pipeline CI simple
- `data/budget_data.json` : données persistantes
- `src/app.py` : point d'entrée Streamlit
- `src/models.py` : modèles de données
- `src/utils.py` : chargement/sauvegarde JSON

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Lancement

```bash
streamlit run src/app.py
```
