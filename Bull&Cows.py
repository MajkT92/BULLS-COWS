"""
Bull&Cows.py: druhý projekt do Engeto Online Python Akademie
author: Michal Toman
email: mtoman92@gmail.com
discord: majk923278
"""

import random

cara = 47 * "-"

#zdravící už. funkce
def hello_user():
    print("Hi there!")
    print(cara)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(cara)

#volání funkce
hello_user()

#funkce na generování čísel
def generovani_cisel():

    while True:
        nahodne = random.randint(1000, 9999)
        nahodne_str = str(nahodne)
        if len(set(nahodne_str)) == 4:
            return nahodne

nahodne_cislo = generovani_cisel()

#uži. funkce pro zadání vstupu uživatelem
#uži. funkce pro zadání vstupu uživatelem
def vstup_uzivatele():
    while True:
        zadane_cislo = input("Enter a number: ")
        print(cara)

    #ověření zda uživatel zadal pouze 4 znaky nebo písmeno
        if len(zadane_cislo) != 4 or not zadane_cislo.isdigit():
            print("Enter only a 4-digit number!")
            continue

        # ověření zda uživatel nezadal duplicitní hodnoty
        if len(set(zadane_cislo)) != 4:
            print("Entered number contains duplicate digits!")
            continue

        # ověření zda uživatel nezadal nulu na začátku
        if zadane_cislo[0] == "0":
            print("The number must not start with 0!")
            continue

        return zadane_cislo

#uži. funkce na počítání Bull & Cows
def pocet_bulls_cows(spravny_vystup_uzivatele, nahodne_cislo):
    bulls = 0
    cows = 0

#for loop pro ověření počtu bull & cow
    for i in range(4):
        if spravny_vystup_uzivatele[i] == str(nahodne_cislo)[i]:
            bulls += 1

        elif spravny_vystup_uzivatele[i] in str(nahodne_cislo)[i]:
            cows += 1

#ověření jednotného / množného čísla bull & cow
    pocet_bull = "bull" if bulls == 1 else "bulls"
    pocet_cow = "cow" if cows == 1 else "cows"
    print(f"{bulls} {pocet_bull}, {cows} {pocet_cow}")

    return bulls


#uži. funce zda chce uživatel pokračovat v hraní nebo ne
def pokracovani_hry():
    odpoved = input('Next round? (y/n): ')
    if odpoved in ('y', 'n'):
        return odpoved == 'y'

#while loop samotné hry

while True:
    spravny_vystup_uzivatele = vstup_uzivatele()
    bulls = pocet_bulls_cows(spravny_vystup_uzivatele,nahodne_cislo)

    if bulls == 4:
        print("Correct, you’ve guessed the right number!")
        print(cara)

    if not pokracovani_hry():
        print("Thank you for playing! :)")
        print(cara)
        break

    else:
        print("Starting a new game...")
        print(cara)