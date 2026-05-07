import random #zufällige sachen
import json #json file support
import os #relativer pfad checker
import re #regex für buchstaben erlauben/verbieten

def städte_kette_game():
    print('Willkommen zum Städte-Kette-Spiel! Du musst eine Stadt nennen, die mit dem letzten Buchstaben der vorherigen Stadt beginnt. Viel Spaß!')
    print('Gib "exit" ein, um das Spiel zu beenden.')

    data_path = os.path.join(os.path.dirname(__file__), "../data/städte_kette_game.json")
    with open(data_path, "r", encoding="utf-8") as f:
        cities = json.load(f)


    #prüfen, ob stadt echt
    def is_real_city(user_city, cities):
        
        # beide strings in Kleinschreibung machen für case insensitivity
        user_city = user_city.strip().lower()
        cities_lower = [city.lower() for group in cities.values() for city in group]
        
        valid = is_valid_city_input(user_city)
        
        if valid:
            if user_city in cities_lower:
                return True
            else:
                return False
                # wenn die Internet-Verbindung da ist, soll hier eine API hin,
                # ob die Stadt existiert; wenn ja, wird sie dann auch in die Liste eingetragen.
        else:
            return False

    
    #prüfen, ob input gültig, mit regex
    def is_valid_city_input(text):
        """
        Validiert einen Städtenamen nach folgenden Regeln:

        - Nur Buchstaben (A–Z, a–z, ÄÖÜäöüß), Leerzeichen und Bindestriche erlaubt
        - Kein Leerzeichen am Anfang oder Ende
        - Kein Bindestrich am Anfang oder Ende
        - Keine doppelten Leerzeichen ("  ")
        - Keine doppelten Bindestriche ("--")
        - Mindestens 3 Buchstaben insgesamt
        - Mindestens zwei verschiedene Buchstaben
        """

        # 1. Regex für Struktur
        pattern = r"""
            ^                                  # Anfang
            (?!.*\s\s)                         # keine doppelten Leerzeichen
            (?!.*--)                           # keine doppelten Bindestriche
            [A-Za-zÄÖÜäöüß]                    # beginnt mit Buchstabe
            (?:[A-Za-zÄÖÜäöüß\- ]*             # innen: erlaubte Zeichen
            [A-Za-zÄÖÜäöüß])                   # endet mit Buchstabe
            $                                  # Ende
        """

        if not re.match(pattern, text, re.VERBOSE):
            return False

        # 2. Buchstaben extrahieren
        letters = re.findall(r"[A-Za-zÄÖÜäöüß]", text)

        # 3. Mindestens 3 Buchstaben
        if len(letters) < 3:
            return False

        # 4. Mindestens zwei verschiedene Buchstaben
        if len(set(letters)) < 2:
            return False

        return True
    
    def get_last_letter_of(city):
        return city[-1]
    def get_first_letter_of(city):
        return city[0]
    
    def get_ai_city(previous_city, cities, used_cities):
        letter = get_last_letter_of(previous_city).upper()
        
        liste = cities[letter]
        
        for possible_answer in liste:
            if possible_answer.lower() not in used_cities:
                used_cities.add(possible_answer.lower())
                return possible_answer
        
        return None

    
    #game-loop
    user_city = input('Du fängst an: gebe eine Stadt ein: ')
    used_cities = set()
    used_cities.add(user_city.lower())
    
    while True:
        valid = is_real_city(user_city, cities)
        
        if user_city == "exit":
            print('Du hast das Spiel abgebrochen und damit verlierst du es auch')
            break
        
        if not valid:
            print('ungültige Eingabe, damit verlierst du automatisch')
            break
        
        if user_city.lower() in used_cities:
            print('Diese Stadt wurde schon benutzt damit verlierst du')
        
        ai_city = get_ai_city(user_city, cities, used_cities)
        
        if ai_city == None:
            print('Du hast gewonnen')
            break
        
        print(f"KI: {ai_city}")
        
        user_city = input('DU:')
        

# TODO: eine statistik json, eine api, eine GUI (eine FastAPI zu einem SwiftUI frontend oder Flutter)