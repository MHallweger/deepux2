# Notebooks

## How to run
Das Notebook benötigt zur Ausführung zwei csv-Dateien `mass_evaluations.csv` und `app_details.csv`. Die `mass_evaluations.csv`-Datei wird durch das Python-Script `mass_analysis.py` erzeugt und automatisch an die korrekte Stelle (/data/mass_evaluations.csv) abgelegt. Die andere Datei stammt von interactionmining.org aus dem Rico-Datenset und ist die [Play Store Metadata](https://storage.googleapis.com/crowdstf-rico-uiuc-4540/rico_dataset_v0.1/app_details.csv) - Datei aus diesem. Abgelegt wird diese ebenfalls im Ordner "data" auf Root-Ebene des Repositories.

Es ist Wichtig zu Wissen, dass ein Unterordner namens ’combined’ unter dem Ordner ’data’ existieren muss. Der ’combined’ Ordner muss auch Bilder enthalten um die weiteren Funktionalitäten des Notebooks ausführen zu können.
Die Bilder sind aus dem Rico-Datenset, welche unter [diesem Link](https://storage.googleapis.com/crowdstf-rico-uiuc-4540/rico_dataset_v0.1/unique_uis.tar.gz) heruntergeladen werden kann. Da der Ordner zu groß ist, sind die Dateien als tar.gz verpackt.
Es sind auch JSON Dateien enthalten, jedoch kümmert sich Python darum, in dem es nur Dateien nimmt die den Format ’jpg’ haben.

####Wichtig: Ein Ordner namens ’data’ muss eventuell manuell erstellt werden, damit Python keine Pfadprobleme bekommt.