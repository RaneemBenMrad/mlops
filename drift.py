import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

# Charger datasets
reference = pd.read_csv("data/processed/ratings_processed.csv")  # ancien data
current = pd.read_csv("data/processed/ratings_processed.csv")    # nouveau data

# Créer un rapport de drift
report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=reference, current_data=current)

# Exporter en HTML
report.save_html("reports/data_drift.html")
print("Rapport de drift généré : reports/data_drift.html")
