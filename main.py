"""
Projekt 2: Högt/lågt-spel med highscore
Ett spel där användaren gissar ett slumpmässigt tal mellan 1 och 100.
Highscore sparas i JSON-format och visas sorterat efter antal gissningar.
"""

import random
import json


# === FILHANTERING ===

def ladda_highscore(filnamn="highscore.json"):
    """
    Laddar highscore-listan från en JSON-fil.

    Parametrar:
        filnamn (str): Namnet på filen att läsa från. Standard: "highscore.json"

    Returnerar:
        list: En lista med dictionaries där varje dictionary har nycklarna
              "namn" (str) och "gissningar" (int).
              Returnerar en tom lista om filen inte finns.
    """
    try:
        # Försök öppna och läsa JSON-filen
        with open(filnamn, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        # Om filen inte finns ännu, returnera en tom lista
        return []


def spara_highscore(highscore_lista, filnamn="highscore.json"):
    """
    Sparar highscore-listan till en JSON-fil.

    Parametrar:
        highscore_lista (list): Listan med spelresultat som ska sparas.
        filnamn (str): Namnet på filen att skriva till. Standard: "highscore.json"
    """
    # Öppna filen i skrivläge och spara listan som formaterad JSON
    with open(filnamn, "w") as f:
        json.dump(highscore_lista, f, indent=4, ensure_ascii=False)


# === SPELMEKANIK ===

def spela_omgang():
    """
    Spelar en omgång av Högt/lågt-spelet.

    Väljer ett slumpmässigt hemligt tal och låter användaren gissa
    tills rätt svar anges. Ger ledtrådar om gissningen är för hög eller låg.

    Returnerar:
        int: Antalet gissningar som behövdes för att gissa rätt.
    """
    # Välj ett slumpmässigt hemligt tal mellan 1 och 100
    hemligt_tal = random.randint(1, 100)
    antal = 0  # Räknare för antal gissningar

    print("Gissa ett tal mellan 1 och 100!")

    while True:
        # Felhantering om användaren skriver något som inte är ett heltal
        try:
            gissa = int(input("Gissa: "))
        except ValueError:
            print("Ange ett heltal!")
            continue

            # Kontrollera att gissningen är inom det giltiga intervallet
        if gissa < 1 or gissa > 100:
            print("Fel! Du måste ange ett heltal mellan 1 och 100!")
            continue

        antal += 1  # Öka gissningsräknaren

        # Ge feedback beroende på om gissningen är för låg, hög eller rätt
        if gissa < hemligt_tal:
            print("För lågt!")
        elif gissa > hemligt_tal:
            print("För högt!")
        else:
            print(f"Rätt! Du klarade spelet på {antal} gissningar.")
            return antal  # Returnera antal gissningar när spelaren lyckas


# === HIGHSCORE-VISNING ===

def visa_highscore(highscore_lista):
    """
    Visar highscore-listan sorterad med bästa spelaren (minst gissningar) först.

    Parametrar:
        highscore_lista (list): Listan med spelresultat som ska visas.
    """
    print("\n--- HIGHSCORE ---")

    # Kontrollera om det finns några resultat att visa
    if not highscore_lista:
        print("Inga resultat ännu.")
        return

    # Sortera listan i stigande ordning baserat på antal gissningar
    # (färre gissningar = bättre placering)
    sorterad = sorted(highscore_lista, key=lambda x: x["gissningar"])

    # Skriv ut varje spelare med placering, namn och antal gissningar
    for i, spelare in enumerate(sorterad, start=1):
        print(f"{i}. {spelare['namn']} - {spelare['gissningar']} gissningar")


# === HUVUDPROGRAM ===

def huvudprogram():
    """
    Huvudprogrammet som styr menyn och programmets flöde.

    Laddar befintlig highscore, visar en meny i loop och hanterar
    spelarens val tills användaren väljer att avsluta.
    """
    # Ladda eventuell befintlig highscore från fil
    highscore = ladda_highscore()

    while True:
        # Visa huvudmenyn
        print("\n--- HÖGT / LÅGT ---")
        print("1. Spela ny omgång")
        print("2. Visa highscore")
        print("3. Avsluta")

        val = input("Välj: ").strip()

        if val == "1":
            # Starta en ny spelomgång och hämta antal gissningar
            antal = spela_omgang()

            # Be spelaren ange sitt namn
            namn = input("Skriv ditt namn: ").strip()

            # Skapa en dictionary med spelarens resultat
            spelare = {"namn": namn, "gissningar": antal}

            # Lägg till resultatet i highscore-listan och spara till fil
            highscore.append(spelare)
            spara_highscore(highscore)
            print("Ditt resultat har sparats!")

        elif val == "2":
            # Visa den aktuella highscore-listan
            visa_highscore(highscore)

        elif val == "3":
            # Avsluta programmet
            print("Tack för att du spelade! Hejdå!")
            break

        else:
            # Hantera ogiltigt menyval
            print("Ogiltigt val! Välj 1, 2 eller 3.")


# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram()