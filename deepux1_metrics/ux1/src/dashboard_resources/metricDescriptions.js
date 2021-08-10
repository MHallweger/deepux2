var metricDescriptions = {
    "distinct_rgb_values": {
        "infoText": "Die Anzahl der eindeutigen Farben im RGB-Spektrum ist ein Hinweis auf die Farbvarianz. Es werden Farben gezählt, die häufiger als ein Schwellenwert auftreten."
    },
    "figure_ground_contrast": {
        "infoText": "Der Leuchtdichte- und Farbkontrast korreliert mit der Wahrnehmungsgeschwindigkeit/-fähigkeit. Wörter und Objekte mit hohem Kontrast sind leichter zu lesen und zu erkennen."
    },
    "white_space": {
        "infoText": "Der Weißraum-/Leerraum-Anteil zeigt zum einen die effektive Nutzung des Raums an und zum anderen die Fähigkeit der Oberfläche, die Aufmerksamkeit auf Regionen auf der Benutzeroberfläche zu lenken. Diese Metrik ist eine Heuristik und basiert nicht auf einer Theorie des menschlichen Sehsystems."
    },
    "grid_quality": {
        "infoText": "Die Rasterqualität gibt die interne Ausrichtung der verschiedenen Komponenten oder identifizierbaren Bereiche der Benutzeroberfläche zueinander an. Es wurde in mehreren Studien festgestellt, dass die Rasterqualität einen starken Einfluss auf den ästhetischen Eindruck hat, der durch das Gesamtlayout hervorgerufen wird."
    },
    "colourfulness": {
        "infoText": "Die Hassler-Susstrunk-Metrik wird auf der Grundlage des RGYB-Farbspektrums berechnet und umfasst hauptsächlich Standardabweichungen. Je höher die Abweichung, desto farbiger wird das Bild wahrgenommen. Dies hat eine hohe Korrelation mit dem ästhetischen Eindruck, wurde aber hauptsächlich mit Bildern und nicht mit Benutzeroberflächen getestet. Die Metrik ist allerdings rechenaufwändig. Zu beachten ist, dass diese Metrik den Farbton nicht berücksichtigt."
    },
    "hsv_colours": {
        "avgSaturation": {
            "infoText": "Der HSV-Farbraum durchschnittliche Sättigung (Saturation) entspricht eher dem menschlichen Sehsystem. Diese Metriken geben den Durchschnitt und die Standardabweichung für jeden Kanal in HSV an. Empirische Untersuchungen haben gezeigt, dass die Kanäle Farbton und Sättigung mit dem ästhetischen Eindruck korrelieren."
        },
        "stdSaturation": {
            "infoText": "Der HSV-Farbraum Standard Sättigung (Saturation) entspricht eher dem menschlichen Sehsystem. Diese Metriken geben den Durchschnitt und die Standardabweichung für jeden Kanal in HSV an. Empirische Untersuchungen haben gezeigt, dass die Kanäle Farbton und Sättigung mit dem ästhetischen Eindruck korrelieren."
        },
        "avgValue": {
            "infoText": "Der HSV-Farbraum (Farbton (Hue), durchschnittlicher Wert (Value)) entspricht eher dem menschlichen Sehsystem. Diese Metriken geben den Durchschnitt und die Standardabweichung für jeden Kanal in HSV an. Empirische Untersuchungen haben gezeigt, dass die Kanäle Farbton und Sättigung mit dem ästhetischen Eindruck korrelieren."
        },
        "stdValue": {
            "infoText": "Der HSV-Farbraum (Farbton (Hue), Standard Wert (Value)) entspricht eher dem menschlichen Sehsystem. Diese Metriken geben den Durchschnitt und die Standardabweichung für jeden Kanal in HSV an. Empirische Untersuchungen haben gezeigt, dass die Kanäle Farbton und Sättigung mit dem ästhetischen Eindruck korrelieren."
        }
    },
    "hsv_unique": {
        "infoText": "Der HSV-Farbraum (Farbton, Sättigung, Wert) entspricht eher dem menschlichen Sehsystem. Diese Metrik gibt die Anzahl der eindeutigen Farben pro Kanal in HSV an. Im Gegensatz zur anderen HSV-Metrik gibt es für diese Metrik keine direkten empirischen Belege. Zu beachten ist, dass diese Metrik stark mit der Anzahl der Farben im RGB-Farbraum korreliert."
    },
    "lab_avg": {                
        "meanLEvaluation": {
            "infoText": "Der LAB-Farbraum nähert sich dem menschlichen Sehvermögen für die Gleichmäßigkeit der Farbwahrnehmung an. Die Ergebnisse sind ähnlich wie bei der HSV-Metrik. Empirische Arbeiten haben die Korrelation zwischen Standard Deviation (Standardabweichung) in der Leuchtdichte und dem ästhetischen Eindruck unterstützt."
        },
        "stdLEvaluation": {
            "infoText": "Der LAB-Farbraum nähert sich dem menschlichen Sehvermögen für die Gleichmäßigkeit der Farbwahrnehmung an. Die Ergebnisse sind ähnlich wie bei der HSV-Metrik. Empirische Arbeiten haben die Korrelation zwischen Standard Deviation (Standardabweichung) in der Leuchtdichte und dem ästhetischen Eindruck unterstützt."
        }
    },
    "static_colour_clusters": {
        "infoText": "Die statischen Farbcluster beziehen sich auf die Anzahl der vorbestimmten Farbcluster im Bild. Das Clustering basiert auf der Aufteilung der RGB-Kanäle. Sie gibt die Anzahl der dominanten Farben an, wird jedoch durch die Farbvarianz beeinträchtigt. Die dynamischen Farbcluster haben zwar eine höhere Korrelation mit dem ästhetischen Eindruck, sind aber auch komplexer zu berechnen."
    },
    "dynamic_colour_clusters": {
        "infoText": "Diese Metrik bestimmt die Anzahl der Farbcluster in einem Bild und die durchschnittliche Anzahl der Farben innerhalb jedes Clusters. Farben werden rekursiv geclustert, wobei als Kriterium ihr Abstand in einem Farbwürfel verwendet wird. Nur Cluster mit mehr als 5 Werten werden in die Berechnung einbezogen. Die Anzahl der Farben pro Cluster korreliert nachweislich mit dem ästhetischen Empfinden. "
    },
    "luminance_sd": {
        "infoText": "Die Standardabweichung der Leuchtdichte gibt an, wie stark die Leuchtdichte im Bild variiert. Sie besitzt keine oder eine geringe Korrelation mit der wahrgenommenen Farbvariabilität, aber eine gewisse Korrelation mit dem ästhetischen Eindruck."
    },
    "wave": {
        "infoText": "Diese Metrik nimmt den mittleren Farbpräferenzwert von jedem Pixel, welcher auf empirisch gewonnenen Farbpräferenzwerten basiert. Diese Farbpräferenzwerte wurden ermittelt, indem die Teilnehmer ihre Präferenzen für Objekte dieser Farben bewertet haben, mit der Theorie, dass sich die Präferenzen für diese Objekte auch auf die Präferenzen für die Farben dieser Objekte übertragen."
    },
    "contour_density": {
        "infoText": "Die Kantendichte/Konturdichte korreliert mit der Wahrnehmung von Unordnung. Sie wird als das Verhältnis der Pixel, die sich an einer Kante ausrichten, im Vergleich zur Gesamtzahl der Pixel im Bild berechnet. Zu beachten ist, dass diese Metrik die Farbvarianz nicht berücksichtigt."
    },
    "contour_congestion": {
        "infoText": "Kantenstau/Konturenstau gibt an, wie gut die Hauptkanten wahrgenommen werden können. Ein überfülltes Bild ist schwer zu verfolgen. Die Anzeige der Kantenüberlastung ist wichtig für komplexe Oberflächen und Graphenvisualisierungen. (Anzahl der überlasteten Pixel geteilt durch die Anzahl der Kantenpixel)."
    },
    "pixel_symmetry": {
        "infoText": "Pixelsymmetrie beschreibt die wahrgenommene Symmetrie über eine Achse. Sie ist mit dem Gestaltprinzip der Symmetrie verbunden. Diese Metrik betrachtet das gesamte Bild und findet eine Achse für maximale Symmetrie. Die Metrik eignet sich möglicherweise besser für Zeichnungen und Fotos als für Benutzeroberflächen, bei denen die Elemente eindeutig sind."
    },
    "quadtree_decomposition": {
        "balance": {
            "infoText": "Balance kann als die Verteilung des optischen Gewichts in einem Bild definiert werden. Das optische Gewicht bezieht sich auf die Wahrnehmung, dass einige Objekte schwerer erscheinen als andere. Größere Objekte sind schwerer, während kleine Objekte leichter sind. Die Balance im Bildschirmdesign wird durch eine gleichmäßige Gewichtung der Bildschirmelemente, links und rechts, oben und unten, erreicht."
        },
        "symmetry": {
            "infoText": "Symmetrie ist eine Achsenverdopplung: eine Einheit auf einer Seite der Mittellinie wird auf der anderen Seite exakt repliziert. Vertikale Symmetrie bezieht sich auf die ausgeglichene Anordnung gleichwertiger Elemente um eine vertikale Achse, und horizontale Symmetrie um eine horizontale Achse. Die radiale Symmetrie besteht aus äquivalenten Elementen, die um zwei oder mehr Achsen ausgeglichen sind, welche sich in einem zentralen Punkt schneiden."
        },
        "equilibrium": {
            "infoText": "Das Gleichgewicht ist eine Stabilisierung, ein mittleres Zentrum der Aufhebung. Das Gleichgewicht auf einem Bildschirm wird durch die Zentrierung des Layouts selbst erreicht. Die Mitte des Layouts stimmt mit der Mitte des Frames überein."
        },
        "numberOfLeaves": {
            "infoText": "Die Gesamtanzahl der Leaves (=Blätter) am Ende der Rekursion. Je höher diese Zahl ist, desto höher ist die Komplexität."
        }
    },
}