# AR_Robotics_Studien

Dieses Projekt ist zweigeteilt. Im Ordner AR ist die Unityanwendung zu finden, die mit Unity importiert werden kann.
Im Ordner Python_calibrate sind die zwei Ansätze zur Roboterkalibrierung bzw Ansteuerungstests zu finden.
Da der praktische Teil der Arbeit leider aufgrund von Hardware- und Terminschwierigkeiten nicht fertiggestellt werden konnte,
sind die hier hochgeladenen Programme nur Startpunkte bzw. Ansätze, die im Rahmen der Studienarbeit erarbeitet wurden. 
Das Aufsetzen bzw das Benutzen des ROS Frameworks hat Probleme solchermaßen verursacht, dass die verwendeten virtuellen Maschinen
abgestürzt sind, bevor die Skripte getestet werden konnten. Daher wird an dieser Stelle nur an den Installationsguide des ROS Frameworks unter
https://wiki.ros.org/noetic/Installation verwiesen.

Die AR Applikation wurde per Unity entwickelt und muss zur Verwendung auf die HoloLens2 im Entwicklermodus gezogen werden. In der Entwicklung wurde hierfür Visual Studio verwendet, um das Starten der Applikation zu steuern. Dafür muss das Buildziel auf das externe Gerät mit der ARM64 Architektur gestellt werden, nachdem die HoloLens2 verbunden ist. Mit der Verbindung zwischen PC und HoloLens2 gab es öfter Probleme, da sich die HoloLens2 immer wieder an und abmeldet am anderen Computer. Daher ist beim Bauen darauf zu achten, dass alle Parameter noch richtig eingestellt sind. Aufgrund der Commitbeschränkungen von Github wurde nur der ursprünglich erstellte Projektordner ohne Builddateien hochgeladen.

# Pythonskripts
Damit man die Pythonskripts ausführen kann, muss eine vollständige ROS Umgebung aufgesetzt werden. Anschließend muss man die Skripte in die dafür vorgesehenen Ordner kopieren und kann sie danach ausführen. 
