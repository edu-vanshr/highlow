"""
Projekt 2: Högt/lågt-spel med highscore
Ett spel där användaren gissar ett slumpmässigt tal.
Highscore sparas i JSON-format.
"""

import random
import json

# === FILHANTERING ===

def ladda_highscore(filnamn="highscore.json"):
    try:
        with open(filnamn, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def spara_highscore(highscore_lista, filnamn="highscore.json"):
    with open(filnamn, "w") as f:
        json.dump(highscore_lista, f, indent= 4, ensure_ascii=False)


# === SPELMECKANIK ===

def spela_omgang():
    hemligt_tal = rand.randint(1,100)
    antal = 0

    while True:
        gissa = int(input("Gissa: "))
        antal += 1

        if gissa < hemligt_tal:
            print("För lågt!")
        elif gissa > hemligt_tal:
            print("För högt!")
        else:
            print(f"Rätt! Du klarade spelar i {antal} gissningar.")
            return antal



# === HIGHSCORE-VISNING ===

def visa_highscore(highscore_lista):
   print("\n--- HIGHSCORE ---")

   if not highscore_lista:
       print("Inga resultat ännu")
       return

   sorterad = sorted(highscore_lista, key=lambda x: x["gissningar"])

   for i, spelare in enumerate(sorterad, start=1):
       print(f"{i}. {spelare['namn']} - {spelare['gissningar']} gissningar")


# === HUVUDPROGRAM ===

def huvudprogram():
    """
    Huvudprogrammet som styr menyn och programflödet.
    """
    # TODO: Implementera huvudprogrammet
    # 1. Ladda highscore med ladda_highscore()
    # 2. Skapa en while-loop som visar menyn
    # 3. Menyn ska ha alternativen:
    #    1. Spela ny omgång
    #    2. Visa highscore
    #    3. Avsluta
    # 4. Vid val 1:
    #    - Anropa spela_omgang() för att få antalet gissningar
    #    - Fråga efter spelarens namn
    #    - Skapa en dictionary {"namn": namn, "gissningar": antal}
    #    - Lägg till i highscore-listan
    #    - Spara med spara_highscore()
    # 5. Vid val 2: anropa visa_highscore()
    # 6. Vid val 3: avsluta loopen
    pass


# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram()