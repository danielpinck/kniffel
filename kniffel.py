import os
import spieler



# while loop der das Programm ausführt bis start nicht mehr True ist
start = True
while start:

    try:
        # Start menu das die Zahlen 1 und 2 annimmt
        menu = int(input('Willkommen bei Kniffel\n 1: Start\n 2: Beenden\n'))
        os.system('cls')
    except ValueError:
        print('Falsche eingabe')
        os.system('cls')
        continue

    if menu == 1:
        # Game loop wird ausgeführt
        spieler_object = spieler.Spieler()
        spieler_object.spieler_anzahl_eingeben()
        spieler_object.ausfuehren()
        # Runde wird gestartet. Es gibt 3 Runden
        spieler_object.game_loop()
        spieler_object.winner_method()

    # Bei Eingabe von "2" wird das Programm beendet
    elif menu == 2:
        start = False
