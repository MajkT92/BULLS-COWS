"""
Bull&Cows.py: druhý projekt do Engeto Online Python Akademie
author: Michal Toman
email: mtoman92@gmail.com
discord: majk923278
"""

import random

cara = 47 * "-"

#úvodní text
print("Hi there!")
print(cara)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(cara)

#funkce na generování čísel
def generovani_cisel():

    nahodne = random.randint(1000,9999)
    return nahodne

nahodne_cislo = generovani_cisel()

print(f"Random number (for debugging): {nahodne_cislo}")

while True:

    #vstup uživatele
    zadane_cislo = input("Enter a number: ")
    print(cara)

    #ověření zda uživatel zadal pouze 4 znaky nebo písmeno
    if len(zadane_cislo) != 4 or not zadane_cislo.isdigit():
        print("Enter only 4 digit number!")
        continue

    #ověření zda uživatel nezadal duplicitní hodnoty
    if len(set(zadane_cislo)) != 4:
        print("Entered numeric duplicate numbers!")
        continue

    #ověření zda uživatel nezadal nulu
    if zadane_cislo[0] == "0":
        print("It must not start with 0!")
        continue

    bulls = 0
    cows = 0


    #for ověření počet bull & cow
    for i in range(4):
        if zadane_cislo[i] == str(nahodne_cislo)[i]:
            bulls += 1

        elif zadane_cislo[i] in str(nahodne_cislo)[i]:
            cows += 1

    #ověření množství
    if bulls == 1:
        pocet_bull = "bull"
    else:
        pocet_bull = "bulls"

    if cows == 1:
        pocet_cow = "cow"
    else:
        pocet_cow = "cows"


    #výsledá hláška
    print(f"{bulls} {pocet_bull}, {cows} {pocet_cow}")


    #oznamání o vítěství
    if bulls == 4:
        print("Correct, you´ve guessed the right number in 4 guesses!")
        print(cara)
        break

