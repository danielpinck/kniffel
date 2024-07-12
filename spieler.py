import zahlen  # import von zahlen.py
import points  # import von points.py
import os  # os import für os.system('cls') zum leeren der Konsole.
import time
import random



class Spieler:
    # Klasse Spieler bekommt Initialisierung
    def __init__(self):
        self.spieler_name = None
        self.spieler_liste = []
        self.spieler_anzahl = None
        self.current_player = None
        self.put_where = None
        self.player_points = None
        self.try_count = 2
        self.a = None

    # Anzahl der Spieler wird eingegeben

    def spieler_anzahl_eingeben(self):
        self.spieler_anzahl = int(input("Wieviele Spieler: "))

    # Funktion dafür Spielernamen ein zugegeben und Punkteliste wird mit Nullen gefüllt
    def namen_eingeben(self):
        self.spieler_name = input("Gebe Name ein: ")
        self.spieler_liste.append([self.spieler_name] + [None] * 18)

    # Funktion um die Funktion namen_eingeben für die Anzahl der Spieler auszuführen
    def ausfuehren(self):

        for i in range(self.spieler_anzahl):
            self.namen_eingeben()

    def ausgabe(self):
        # Konsole wird geleert
        # os.system('cls')
        # Hier werden die Berechnungen für den Punktestand ausgeführt und in die Spielerliste eingefügt
        for i in range(self.spieler_anzahl):
            self.spieler_liste[i][14] = sum(filter(None, self.spieler_liste[i][1:7]))  # Die Summe der Punkte für 1-6 auf index 14
            if self.spieler_liste[i][14] >= 63:  # Bonuspunkte, wenn der obere Block >= 63 Punkte ist
                self.spieler_liste[i][15] = 35  # 35 Bonuspunkte auf index 15
            self.spieler_liste[i][16] = sum(filter(None, self.spieler_liste[i][14:16]))  # Punkte für 1-6 u. Bonus von 35 auf index 16
            self.spieler_liste[i][17] = sum(filter(None, self.spieler_liste[i][7:14]))  # Summe der Punkte unterer Teil. index 17
            self.spieler_liste[i][18] = sum(filter(None, self.spieler_liste[i][16:18]))  # Summe oberer & unterer Teil. index 18

            # Formatierung für die Anzeige des Punktestandes.
            print(self.spieler_liste[i][0].center(70, "="))
            print("Oberer Block".center(35, "=") + "Unterer Block".center(35, "="))
            print("(1) Einer".ljust(30, ".") + f"{str(self.spieler_liste[i][1]).rjust(5)}" + "   (7) Dreierpasch".ljust(30,".") + f"{str(self.spieler_liste[i][7]).rjust(5)}")
            print("(2) Zweier".ljust(30, ".") + f"{str(self.spieler_liste[i][2]).rjust(5)}" + "   (8) Viererpasch".ljust(30,".") + f"{str(self.spieler_liste[i][8]).rjust(5)}")
            print("(3) Dreier".ljust(30, ".") + f"{str(self.spieler_liste[i][3]).rjust(5)}" + "   (9) Full House".ljust(30,".") + f"{str(self.spieler_liste[i][9]).rjust(5)}")
            print("(4) Vierer".ljust(30,".") + f"{str(self.spieler_liste[i][4]).rjust(5)}" + " (10) Kleine Strasse".ljust(30,".") + f"{str(self.spieler_liste[i][10]).rjust(5)}")
            print("(5) Fünfer".ljust(30,".") + f"{str(self.spieler_liste[i][5]).rjust(5)}" + "  (11) Große Strasse".ljust(30,".") + f"{str(self.spieler_liste[i][11]).rjust(5)}")
            print("(6) Sechser".ljust(30, ".") + f"{str(self.spieler_liste[i][6]).rjust(5)}" + "   (12) Kniffel".ljust(30,".") + f"{str(self.spieler_liste[i][12]).rjust(5)}")
            print("Gesamt".ljust(30, ".") + f"{str(self.spieler_liste[i][14])}".rjust(5) + "   (13) Chance".ljust(30,".") + f"{str(self.spieler_liste[i][13]).rjust(5)}")
            print("Bonus bei 63".ljust(30, ".") + f"{str(self.spieler_liste[i][15])}".rjust(5) + "   Summe unten".ljust(30,".") + f"{str(self.spieler_liste[i][17]).rjust(5)}")
            print("Summe".ljust(30, ".") + f"{str(self.spieler_liste[i][16]).rjust(5)}" + "   Summe oben".ljust(30,".") + f"{str(self.spieler_liste[i][16]).rjust(5)}")
            print("=".center(70, "="))
            print("Gesamt".rjust(45, ".") + f"{str(self.spieler_liste[i][18]).rjust(5)}")

    def ausgabe_self(self):
        # Konsole wird geleert
        # os.system('cls')
        print("".center(15, "="))
        print(f"Runde {self.a + 1}")
        print("".center(15, "="))

        self.spieler_liste[self.current_player][14] = sum(filter(None, self.spieler_liste[self.current_player][1:7]))  # Die Summe der Punkte für 1-6 auf index 14
        if self.spieler_liste[self.current_player][14] >= 63:  # Bonuspunkte, wenn der obere Block >= 63 Punkte ist
            self.spieler_liste[self.current_player][15] = 35  # 35 Bonuspunkte auf index 15
        self.spieler_liste[self.current_player][16] = sum(filter(None, self.spieler_liste[self.current_player][14:16]))  # Punkte für 1-6 u. Bonus von 35 auf index 16
        self.spieler_liste[self.current_player][17] = sum(filter(None, self.spieler_liste[self.current_player][7:14]))  # Summe der Punkte unterer Teil. index 17
        self.spieler_liste[self.current_player][18] = sum(filter(None, self.spieler_liste[self.current_player][16:18]))

        print(self.spieler_liste[self.current_player][0].center(70, "="))
        print("Oberer Block".center(35, "=") + "Unterer Block".center(35, "="))
        print("(1) Einer".ljust(30, ".") + f"{'0'.rjust(5) if (self.spieler_liste[self.current_player][1]) is None else str(self.spieler_liste[self.current_player][1]).rjust(5)  }" + "   (7) Dreierpasch".ljust(30,".") + f"{'0'.rjust(5) if (self.spieler_liste[self.current_player][7]) is None else str(self.spieler_liste[self.current_player][7]).rjust(5)}")
        print("(2) Zweier".ljust(30, ".") + f"{'0'.rjust(5) if (self.spieler_liste[self.current_player][2]) is None else str(self.spieler_liste[self.current_player][2]).rjust(5)  }" + "   (8) Viererpasch".ljust(30,".") + f"{'0'.rjust(5) if (self.spieler_liste[self.current_player][8]) is None else str(self.spieler_liste[self.current_player][8]).rjust(5)}")
        print("(3) Dreier".ljust(30, ".") + f"{'0'.rjust(5) if (self.spieler_liste[self.current_player][3]) is None else str(self.spieler_liste[self.current_player][3]).rjust(5)  }" + "   (9) Full House".ljust( 30,".") + f"{'0'.rjust(5) if (self.spieler_liste[self.current_player][9]) is None else str(self.spieler_liste[self.current_player][9]).rjust(5)}")
        print("(4) Vierer".ljust(30, ".") + f"{'0'.rjust(5) if (self.spieler_liste[self.current_player][4]) is None else str(self.spieler_liste[self.current_player][4]).rjust(5)  }" + "   (10) Kleine Strasse".ljust(30,".") + f"{'0'.rjust(5) if (self.spieler_liste[self.current_player][10]) is None else str(self.spieler_liste[self.current_player][10]).rjust(5)}")
        print("(5) Fünfer".ljust(30, ".") + f"{'0'.rjust(5) if (self.spieler_liste[self.current_player][5]) is None else str(self.spieler_liste[self.current_player][5]).rjust(5)  }" + "   (11) Große Strasse".ljust(30,".") + f"{'0'.rjust(5) if (self.spieler_liste[self.current_player][11]) is None else str(self.spieler_liste[self.current_player][11]).rjust(5)}")
        print("(6) Sechser".ljust(30, ".") + f"{'0'.rjust(5) if (self.spieler_liste[self.current_player][6]) is None else str(self.spieler_liste[self.current_player][6]).rjust(5)  }" + "   (12) Kniffel".ljust(30,".") + f"{'0'.rjust(5) if (self.spieler_liste[self.current_player][12]) is None else str(self.spieler_liste[self.current_player][12]).rjust(5)}")
        print("Gesamt".ljust(30, ".") + f"{'0'.rjust(5) if (self.spieler_liste[self.current_player][14]) is None else str(self.spieler_liste[self.current_player][14]).rjust(5)  }" + "   (13) Chance".ljust(30,".") + f"{'0'.rjust(5) if (self.spieler_liste[self.current_player][13]) is None else str(self.spieler_liste[self.current_player][13]).rjust(5)}")
        print("Bonus bei 63".ljust(30, ".") + f"{'0'.rjust(5) if (self.spieler_liste[self.current_player][15]) is None else str(self.spieler_liste[self.current_player][15]).rjust(5)  }" + "   Summe unten".ljust(30, ".") + f"{'0'.rjust(5) if (self.spieler_liste[self.current_player][17]) is None else str(self.spieler_liste[self.current_player][17]).rjust(5)}")
        print("Summe".ljust(30, ".") + f"{'0'.rjust(5) if (self.spieler_liste[self.current_player][16]) is None else str(self.spieler_liste[self.current_player][16]).rjust(5)  }" + "   Summe oben".ljust(30,".") + f"{'0'.rjust(5) if (self.spieler_liste[self.current_player][16]) is None else str(self.spieler_liste[self.current_player][16]).rjust(5)}")
        print("=".center(70, "="))
        print("Gesamt".rjust(45, ".") + f"{'0'.rjust(5) if (self.spieler_liste[self.current_player][18]) is None else str(self.spieler_liste[self.current_player][18]).rjust(5)  }")
        print()
        print("".center(15, "="))
        print(f"{3 - self.try_count}. Wurf")
        print("".center(15, "="))
    # Funktion um self.player_points in die spieler_liste für den self.current_player bei self.put_where einzutragen
    def player_score_save(self):
        # NICHT FERTIG
        # Abfrage, ob die kategorie schon gefüllt wurde

        self.spieler_liste[self.current_player][self.put_where] = self.player_points
        # return self.spieler_liste

    def roll_menu(self):
        # os.system('cls')
        # Leere Liste für den ersten Wurf. Wird später mit zufälligen Zahlen von 1 bis 6 gefüllt
        roll_all = []
        # for-loop um die Variable roll_all mit Zufallszahlen 1 bis 6 zu füllen
        for i in range(0, 5):
            roll_all.append(int(random.randint(1, 6)))
        return roll_all

    def player_score_assign(self):


        # Liste für die Zuordnung. Die Strings werden bei der Zuordnung zu int. q für beenden
        menu_options = ["q", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "p", "l", "w"]

        player_roll = self.roll_menu()

        assign_bool = True
        while assign_bool:
            #os.system('cls')
            self.ausgabe_self()

            print(player_roll)
            # Input um Wurf zuzuordnen
            self.put_where = input(
                "(p) Punkteliste anzeigen \n(l) Punkteliste aller Spieler anzeigen \n(w) Neu würfeln\n(q) Beenden\noder ordne deinen Wurf zu:")
            os.system('cls')

            # if-statement wo die Punkte welche in points.py berechnet werden in die spieler liste eingefügt werden
            # Zuordnung, wenn "self.put_where" 1 bis 6 ist
            if self.put_where in menu_options[1:7]:  # Bei range ist der letzte Wert nicht inbegriffen.
                self.put_where = int(self.put_where)
                if type(self.spieler_liste[self.current_player][self.put_where]) is int:
                    print('Diese Kategorie ist schon gefüllt')
                    time.sleep(3)
                    continue
                else:
                    assign_bool = False
                    self.player_points = points.number_function(player_roll, self.put_where)
                    self.player_score_save()
                    self.ausgabe_self()
                    os.system('cls')
            elif self.put_where in menu_options[14]:
                self.ausgabe_self()
                print(self.roll_menu)
                input('Enter für weiter')
                continue

            elif self.put_where in menu_options[15]:
                self.ausgabe()
                print(player_roll)
                input('Enter für weiter')
                continue

            # Zuordnung, wenn "self.put_where" 7 ist
            elif self.put_where in menu_options[7]:
                assign_bool = False
                self.put_where = int(self.put_where)
                self.player_points = points.dreierpasch(player_roll)
                self.player_score_save()
                self.ausgabe_self()

            # Zuordnung, wenn "self.put_where" 8 ist
            elif self.put_where in menu_options[8]:
                assign_bool = False
                self.put_where = int(self.put_where)
                self.player_points = points.viererpasch(player_roll)
                self.player_score_save()
                self.ausgabe_self()

            # Zuordnung, wenn "self.put_where" 9 ist
            elif self.put_where in menu_options[9]:
                assign_bool = False
                self.put_where = int(self.put_where)
                self.player_points = points.full_house(player_roll)
                self.player_score_save()
                self.ausgabe_self()

            # Zuordnung, wenn "self.put_where" 10 ist
            elif self.put_where in menu_options[10]:
                assign_bool = False
                self.put_where = int(self.put_where)
                self.player_points = points.kstrasse(player_roll)
                self.player_score_save()
                self.ausgabe_self()

            # Zuordnung, wenn "self.put_where" 11 ist
            elif self.put_where in menu_options[11]:
                assign_bool = False
                self.put_where = int(self.put_where)
                self.player_points = points.gstrasse(player_roll)
                self.player_score_save()
                self.ausgabe_self()

            # Zuordnung, wenn "self.put_where" 12 ist
            elif self.put_where in menu_options[12]:
                assign_bool = False
                self.put_where = int(self.put_where)
                self.player_points = points.kniffel(player_roll)
                self.player_score_save()
                self.ausgabe_self()

            # Zuordnung, wenn "self.put_where" 13 ist
            elif self.put_where in menu_options[13]:
                assign_bool = False
                self.put_where = int(self.put_where)
                self.player_points = points.chance(player_roll)
                self.player_score_save()
                self.ausgabe_self()
            # Punkte tabellen ausgabe für den Spieler am zug

            # Zuordnung, wenn "put_where" q oder Q ist um das Programm zu beenden
            elif self.put_where in menu_options[0]:
                quit_programm = input("Wirklich beenden? (q)")
                # if-statement um Programmabbruch zu bestätigen
                if quit_programm == "q" or quit_programm == "Q":
                    quit("Programm beendet")

            elif self.put_where in menu_options[16]:

                # while-loop um die würfe auf 3 zu beschränken
                if self.try_count > 0:
                    self.keep_rolling(player_roll)

    def keep_rolling(self, roll_all):
        # Variable um die Anzahl von Würfen zu zählen
        menu = "1"
        self.try_count = 2
        while self.try_count > 0:
            try:
                # if-statement zur Formatierung der Ausgabe von Würfen 1 bis 3
                # FUNKTIONIERT. KÖNNTE MAN MIT NUTZUNG VON try_count VIELLEICHT ELEGANTER MACHEN??


                if menu != "1":
                    os.system('cls')
                    self.ausgabe_self()
                    menu = (input(' (1) Nochmal Würfeln\n (2) Würfel behalten\n (q) Spiel beenden\n Wähle: '))

                # if-statement, wenn Spieler in "menu" Würfel neu werfen ausgewählt hat
                if menu == "1":
                    os.system('cls')
                    self.ausgabe_self()
                    print(roll_all)
                    menu = "11"
                    # leere Liste für die
                    re_roll = []
                    how_many = int(input('wie viele? 1-5\n'))
                    dice_roll_check = True
                    while dice_roll_check:

                        for b in range(0, how_many):
                            re_roll.append(int(input('Welcher?\n')))
                            dice = re_roll[b]
                            if re_roll.count(dice) > 1:
                                dice_roll_check = False
                                print('Jeder Würfel darf nur einmal geworfen werden.')
                        while dice_roll_check:
                            self.try_count -= 1

                            for x in re_roll:
                                roll_all[x - 1] = random.randint(1, 6)
                                dice_roll_check = False
            except ValueError:
                print('Falsche eingabe')
                continue
            if menu == "2":
                self.try_count = 0
                continue

            elif menu == "q" or menu == "Q":
                quit_programm = input("Wirklich beenden? (q)\n")
                if quit_programm == "q" or quit_programm == "Q":
                    quit("Programm beendet")

        os.system('cls')
        return roll_all
    def game_loop(self):

        for self.a in range(0, 12):
            # Konsole wird geleert
            os.system('cls')


            for current_player in range(self.spieler_anzahl):
                self.current_player = current_player
                self.player_score_assign()

    def winner_method(self):
        spieler_liste_namen = []
        spieler_liste_punkte = []

        for current_player in range(self.spieler_anzahl):
            spieler_liste_punkte.append(self.spieler_liste[current_player][18])
            spieler_liste_namen.append(self.spieler_liste[current_player][0])

        print(spieler_liste_namen)
        print(spieler_liste_punkte)
        gewinner_index = spieler_liste_punkte.index(max(spieler_liste_punkte))
        i = 0
        j = 1
        while i < len(spieler_liste_punkte) and j < len(spieler_liste_punkte):
            if spieler_liste_punkte[i] == spieler_liste_punkte[j]:
                i += 1
                j += 1
                print("Gleichstand")
            else:
                print(f"Der Gewinner ist {spieler_liste_namen[gewinner_index]} mit "
                      f"{spieler_liste_punkte[gewinner_index]} Punkten")
                break

# Konsole wird geleert
# os.system('cls')
