import random  # import von random. Wird für randint genutzt, um die Würfel zu füllen.
import os  # os import für os.system('cls') zum leeren der Konsole.


def roll_menu(current_player):
    #os.system('cls')
    # Leere Liste für den ersten Wurf. Wird später mit zufälligen Zahlen von 1 bis 6 gefüllt
    roll_all = []
    # Variable um die Anzahl von Würfen zu zählen
    try_count = 2

    # for-loop um die Variable roll_all mit Zufallszahlen 1 bis 6 zu füllen
    for i in range(0, 5):
        roll_all.append(int(random.randint(1, 6)))

    # while-loop um die würfe auf 3 zu beschränken
    while try_count > 0:
        try:
            # if-statement zur Formatierung der Ausgabe von Würfen 1 bis 3
            # FUNKTIONIERT. KÖNNTE MAN MIT NUTZUNG VON try_count VIELLEICHT ELEGANTER MACHEN??
            if try_count == 2:

                print("".center(15, "="))
                print('Versuch 1 von 3')
                print("".center(15, "="))
                print(f"{roll_all}\n")

            elif try_count == 1:
                print("".center(15, "="))
                print('Versuch 2 von 3')
                print("".center(15, "="))
                print(f"{roll_all}\n")
            elif try_count == 0:
                print("".center(15, "="))
                print('Versuch 3 von 3')
                print("".center(15, "="))
                print(f"{roll_all}\n")

            menu = (input(' (1) Nochmal Würfeln\n (2) Würfel behalten\n (q) Spiel beenden\n Wähle: '))

            # if-statement, wenn Spieler in "menu" Würfel neu werfen ausgewählt hat
            if menu == "1":

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
                        try_count -= 1

                        for x in re_roll:
                            roll_all[x - 1] = random.randint(1, 6)
                            dice_roll_check = False
        except ValueError:
            print('Falsche eingabe')
            continue
        if menu == "2":
            try_count = 0
            continue

        elif menu == "q" or menu == "Q":
            quit_programm = input("Wirklich beenden? (q)\n")
            if quit_programm == "q" or quit_programm == "Q":
                quit("Programm beendet")

    return roll_all
