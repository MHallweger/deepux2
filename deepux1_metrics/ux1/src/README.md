# Hauptmodul

Das Hauptmodul `deep_ux.py` steuert das ganze und startet als Erstes den `App Traverser` und leitet die vom Traverser erstellten screenshots an das Modul `MetricsCreator`, damit dieses die Metrik Bewertungen als JSON liefert.
Die zurückgegebenen Metrik Bewertungen, leitet dann das Hauptmodul an das Modul `Metricsevaluator` weiter, um diesbezüglich die Bedeutungen dieser Bewertung zu bekommen. Anschließend werden die bewerteten Metriken an das `Recommendation` Modul übergeben welches für die mit "bad" bewerteten Metriken versucht Verbesserungsempfehlungen zu finden. Abschließend werden alle Daten der Analyse durch ein Dashboard angezeigt.

## Ausführung
Sobald die Voraussetzungen der anderen Module erfüllt sind, kann das Hauptmodul ohne Probleme ausgeführt werden.
Eine komplette Anleitung ist in der [Haupt-Readme](../README.md) des Repositories zu finden.


# App Traverser
Das App Traverser Modul `traverser.py` installiert die zu analysierende APK auf einem angeschlossenen Android Gerät. Anschließend wird die App gestartet und automatisch traversiert. Bei der Traversierung der App werden zu jedem neuen Bildschirminhalt ein Screenshot angelegt.

Zur Traversierung und Erzeugung der Screenshots wird [Droidbot](https://github.com/honeynet/droidbot) verwendet. Die Ausgaben von Droidbot werden anschließend aufbereitet, gefiltert und für die anderen Module über das Filesystem bereitgestellt.


## Voraussetzungen
- `Python` (Version 3.8.5 getestet)
- [Droidbot](https://github.com/honeynet/droidbot) als Python Modul installiert
- `Android-Gerät` (Emulator oder Physisch)
- `.apk` Datei

## Ausführung
Direkt ausgeführt werden kann dieses Modul nicht. Es wird jedoch von dem Modul `deep_ux.py` verwendet.


# Metricscreator

Dieses Modul ist zuständig dafür, die folgenden Metriken

- Anzahl der Farben in RGB-, HSV(avg, unique)- und LAB(avg)-Farbraum / `distinct_rgb_values.py`, `HSV_avg.py`, `HSV_unique.py`, `LAB_avg.py`
- Unterscheidbarkeit des vordergrunds anhand des Kontrasts / `figure_ground_contrast.py`
- Ausrichtung an Gittern / `grid_quality.py`
- Anteil der nicht abgedeckten / weißen Fläche auf der Website / `white_space.py`
- Summe der Abstände aller Pixel zu einem Farbschema / `color_harmony.py`
- Standardabweichung der Pixel im RGB-Farbraum / `colourfulness.py`
- Verhältnis von überlasteten Kantenpixeln zu allen Kantenpixeln / `contour_congestion.py`
- Verhältnis von Kantenpixeln zu allen Pixeln / `contour_density.py`
- Standardabweichung der Leuchtdichte korrigiert für die Display-Wahrnehmung / `luminance_sd.py`
- Verhältnis der Kanten, die entweder horizontal, vertikal oder diagonal gespiegelt werden / `pixel_symmetry.py`
- Quadtree-Zerlegung (zeigt die visuelle Komplexität einer Szene an) / `quadtree_decomposition.py`
- Statische Farbcluster – Anzahl der Bins 5px. (Bins: 32\*32\*32px) (in RGB) / `static_colour_clustering.py`
- Dynamische Farbcluster / `dynamic_colour_clustering.py`
- Wave (Weighted Affective Valence Estimates) nimmt den mittleren Farbpräferenzwert von jedem Pixel, welcher auf empirisch gewonnenen Farbpräferenzwerten basiert / `wave.py`

für die vom `App Traverser` bereit gestellten Screenshots zu berechnen.

Die Ergebnisse des Moduls werden als JSON zurückgegeben.

## Ausführung

Für die Ausführung dieses Modul ist ebenfalls die `deep_ux.py` Python Datei zuständig.


# Metricsevaluator

Dieses Modul ist zuständig dafür, dass die vom `Metricscreator` berechneten Metriken evaluiert werden.

Die Ergebnisse des Moduls werden als JSON zurückgegeben.

## Ausführung
Für die Ausführung dieses Modul ist ebenfalls die `deep_ux.py` Python Datei zuständig.
