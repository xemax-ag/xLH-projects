# Bidschärfe
Ein Vergrösserung der Bildschärfe entspricht einem Hochpassfilter. 
Das Tutorial

[https://theailearner.com/tag/cv2-addweighted](https://theailearner.com/tag/cv2-addweighted)

beschreibt den Mechanismus ausführlich. Die Funktion `cv2.addWeighted(image, 2, blurred, -1, offset)`
zeigt exemplarisch die geweichtete Addition von zwei Bildarrays.