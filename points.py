# Funktion für 1er bis 6er
def number_function(dice_roll, put_where):
    number = put_where
    number_summe = 0
    single_number_points = 0
    for i in range(len(dice_roll)):
        if dice_roll[i] == number:
            number_summe += 1
            single_number_points = number_summe * number
    return single_number_points


# Full House
def full_house(dice_roll):
    full_house_counter = 0
    for i in dice_roll:
        if dice_roll.count(i) >= 2 and dice_roll.count(i) < 4:
            full_house_counter += 1
    if full_house_counter == 5:
        dice_roll.sort()

        full_house_points = 25

    else:
        full_house_points = 0
    return full_house_points


# Dreierpasch
def dreierpasch(dice_roll):
    dreierpasch_check = False
    for i in dice_roll:
        if dice_roll.count(i) > 2:
            dice_roll.sort()
            dreierpasch_check = True
    if dreierpasch_check:
        drei_points = sum(dice_roll)

    else:
        drei_points = 0
    return drei_points


# Viererpasch
def viererpasch(dice_roll):
    viererpasch_check = False
    for i in dice_roll:
        if dice_roll.count(i) > 3:
            dice_roll.sort()
            viererpasch_check = True
    if viererpasch_check:
        vier_points = sum(dice_roll)

    else:
        vier_points = 0
    return vier_points


# strassen
def kstrasse(dice_roll):
    i = 0
    j = 1
    strasse_length = 0
    dice_roll.sort()
    for k in dice_roll:
        if dice_roll.count(k) > 1:
            dice_roll.remove(k)

    while i < len(dice_roll) and j < len(dice_roll):
        if dice_roll[i] - dice_roll[j] == -1:
            strasse_length += 1
            i += 1
            j += 1
        else:
            break

    if strasse_length >= 3:
        kstrasse_points = 30

    else:
        kstrasse_points = 0
    return kstrasse_points

def gstrasse(dice_roll):
    i = 0
    j = 1
    strasse_length = 0
    dice_roll.sort()
    for k in dice_roll:
        if dice_roll.count(k) > 1:
            dice_roll.remove(k)

    while i < len(dice_roll) and j < len(dice_roll):
        if dice_roll[i] - dice_roll[j] == -1:
            strasse_length += 1
            i += 1
            j += 1
        else:
            break

    if strasse_length == 4:
        gstrasse_points = 40

    else:
        gstrasse_points = 0
    return gstrasse_points

# Kniffel
def kniffel(dice_roll):
    kniffel_counter = 0
    for i in dice_roll:
        if dice_roll.count(i) > 1:
            kniffel_counter += 1

    if kniffel_counter == 5:
        kniffel_points = 50

    else:
        kniffel_points = 0
    return kniffel_points


def chance(dice_roll):
    chance_points = sum(dice_roll)
    return chance_points
