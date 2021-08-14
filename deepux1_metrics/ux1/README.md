# Deep UX

Die Dokumentation des Projektes ist [hier im Confulence-Wiki](https://wiki.moxd.io/display/GPDEEPUX/Dokumentation) zu finden.

In dieser und anderen Readmes werden die einzelnen Komponenten nur grob erläutert und beschrieben wie diese Ausgeführt werden können.

## Voraussetzungen
Je nach dem welches Artefakt ausgeführt werden soll, werden unterschiedliche Voraussetzungen benötigt.

- Jedes Artefakt benötigt jedoch `Python3`.
- Zusätzlich gibt es eine `requirements.txt` in welcher die meisten (ggf. unvollständig je nach Python-Installation) benötigten Module stehen. Diese kann mit `python -m pip install -r src/requirements.txt` installiert werden.
- Sollte bei der Ausführung ein "module not found" Fehler aufkommen, so muss dieses noch nachinstalliert werden (`python -m pip install <ModulName>`).


## Auführung
Das Projekt besitzt verschiedene eigenständige, ausführbare Artefakte:

1. Ein Script zur Analyse des Rico-Datensatzes (`mass_analysis.py`)
2. Ein Jupyter-Notebook zur Auswertung der Rico-Analyse (`rico_analysis.ipynb`)
3. Ein Debug-Script um für ein Bild alle Metriken zu analysieren und in der Konsole als JSON auszugeben (`test.py`)
4. Den prototypischen Ansatz des ersten GUI-Tools zur Nutzung des Projektes (`metricUI`)
5. Das "fertige" Kompletttool welches eine APK entgegennimmt, diese Analysiert und ein Dashboard mit den Ergebnissen erzeugt (`deep_ux.py`)


---

## Mass_Analysis
Dieses Modul analysiert den Rico-Datensatz bezüglich aller implementierter Metriken und stellt das Ergebnis als CSV-Datei bereit.

### Weitere Voraussetzungen
- [Rico-Datensatz (1. UI Screenshots and View Hierarchies)](http://interactionmining.org/rico#quick-downloads)

### Ausführung
In dem Script [src/mass_analysis.py](./src/mass_analysis.py) gibt es verschiedene Einstellungsmöglichkeiten:

- `DATA_PATH`: Der Pfad zu dem Rico-Datensatz.
- `NUM_WORKER_THREADS`: Anzahl paralleler Analyse-Prozesse 
- `CHECKPOINT_AFTER_N_FILES`: Nach wie vielen analysierten Bildern die Ergebnisse zwischengespeichert werden.
- `START_INDEX`: Ab welcher Stelle des Datensatzes die Analyse begonnen wird (um bspw. nach einem Checkpoint wieder anzufangen)

Standardmäßig erwartet das Modul den Rico-Datensatz im Repository-Ordner `data`, welcher nicht in git eingecket ist. Demnach muss der Datensatz von [Rico (1. UI Screenshots and View Hierarchies)](http://interactionmining.org/rico#quick-downloads) heruntergeladen, entpackt und der Ordner `combined` aus dem Download in den neu zu erstellenden Ordner `data` im root des Repository kopiert werden.

Anschließend kann das Python Script `src/mass_analysis-py` ausgeführt werden (bspw. über den Play-Button in Visual Studio Code).


---

## Rico_Analysis
Die Rico-Analyse-CSV wird von diesem Jupyter-Notebook eingelesen und ausgewertet.

### Weitere Voraussetzungen
- Jupyter
- mass_evaluations.csv
- [Rico-Datensatz (1. UI Screenshots and View Hierarchies)](http://interactionmining.org/rico#quick-downloads)
- [Rico-Datensatz (6. Play Store Metadata)](http://interactionmining.org/rico#quick-downloads)


### Ausführung

Das Notebook muss dazu in einem [Jupyter-Server](https://jupyter.org/) ausgeführt werden (bspw. durch die Jupyter Extension in VS Code).

Der 1. Rico-Datensatz muss wie bei der Massenalayse in `data/combined` vorliegen. Die Rico-Store-Metadaten (6.) muss in `data/app_details.csv` kopiert werden.

Zusätzlich muss das Daten-CSV aus der Massenanalyse (siehe Modul oben) in `data/mass_evaluations.csv` vorliegen. Der letzte Datensatz aus dem Projekt ist [hier in Confulence](https://wiki.moxd.io/display/GPDEEPUX/Dokumentation#Dokumentation-Anhang) zu finden.


---

## Test .py
Das Bild in `src/TestScreen.png` wird auf alle Metriken analysiert und in der Konsole ausgegeben.

Ausführung über bspw. den Play-Button in VS Code in der Datei `src/test.py`


---

## Metric UI
Dieses Modul erhält als Eingabe ein Bild, zu diesem Bild werden die Metriken analysiert. Die Metriken werden als Balkendiagramm ausgegben.

### Ausführung
- Das Python Script src/main-py kann einfach ausgeführt werden (bspw. über den Play-Button in Visual Studio Code).


---

## Deep UX
Die gegeben APK-Datei wird auf dem an den Rechner angeschlossenen Android-Gerät oder Emulator installiert, traversiert und analysiert.

### Weitere Voraussetzungen
- [Droidbot](https://github.com/honeynet/droidbot) als Python Modul installiert
- Alle Voraussetzungen von Droidbot
- Gestartetes `Android-Gerät` (Emulator oder Physisch)
- `.apk` Datei

### Ausführung
Einstellungen werden in diesem Modul über Kommandozeilen-Parameter gesetzt. Deshalb ist wahrscheinlich ein einfaches ausführen über den VS Code Play-Button nicht möglich.

Alle Parameter können mit `python src/deep_ux.py -h` angezeigt werden.

Eine minimal Konfigurierte Ausführug ist `python src/deep_ux.py -a <PATH_TO_APK>`

Die Ausgabe in Form eines Webseiten-Dashboards landed anschließend in `data/droidbot_output/index.html`.
