# MLOps Movie Recommendation Pipeline

Système de recommandation de films industrialisé avec un workflow MLOps complet : versionning des données et modèles (DVC), suivi d'expériences (MLflow), containerisation (Docker) et pipeline reproductible.

## Aperçu du projet

Ce dépôt implémente un pipeline **end-to-end** de recommandation de films en suivant les principes MLOps modernes :

- **Versionning des données** et des modèles → **DVC**
- **Suivi des expériences**, comparaison et registre de modèles → **MLflow**
- **Containerisation** et exécution reproductible → **Docker** + **docker-compose**
- **Pipeline automatisé** → `dvc.yaml` + scripts modulaires
- Objectif : garantir **reproductibilité**, **traçabilité** et **collaboration** sur un projet de machine learning

Technologies principales :
- Python 3.10+
- DVC 3.x
- MLflow 2.x
- scikit-learn / surprise / implicit / LightFM (selon la branche ou l'expérience)
- Docker & docker-compose

## Structure du projet

```text
.
├── data/                 # Données brutes et intermédiaires (gérées par DVC)
│   └── raw/
├── models/               # Modèles entraînés (gérés par DVC)
├── mlruns/               # Artefacts et logs MLflow (gérés par DVC ou exclu)
├── src/                  # Code source principal
│   ├── data/             # Préparation des données
│   ├── models/           # Entraînement et évaluation
│   └── utils/            # Fonctions utilitaires
├── notebooks/            # Exploration initiale (non versionnées dans le pipeline)
├── scripts/              # Scripts d'initialisation, helpers
├── tests/                # Tests unitaires
├── .dvc/                 # Cache DVC (non commité)
├── dvc.yaml              # Définition du pipeline DVC
├── dvc.lock              # Verrouillage des versions (généré)
├── params.yaml           # Hyperparamètres versionnés
├── requirements.txt      # Dépendances Python
├── Dockerfile            # Image pour l'entraînement / inférence
├── docker-compose.yml    # Services MLflow + stockage optionnel
├── .gitignore
└── README.md