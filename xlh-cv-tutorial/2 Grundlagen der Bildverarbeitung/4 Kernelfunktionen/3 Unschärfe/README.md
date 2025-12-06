# Unschärfe
Der Bluralgorithmus (siehe auch Kernelfunktionen, Einleitung) entspricht einem Tiefpassfilter.
Ziel besteht darin, die Details aus einem Bild zu entfernen. Dies wird erreicht durch eine
gewichtete Mittelwertbildung aus dem Zentrumspixel des Kernels sowie den benachbarten Pixeln.
Aus dieser Definition lässt sich auch herleiten warum ein Kernel stehts eine ungerade Grössenangabe
benötigt.  

Das Codebeispiel demonstriert die unterschiedlichen Unschärfealgorithmen mit unterschiedlichen
Kernelgrössen.  
Je grösser der Kernel, umso stärker die Unschärfe.