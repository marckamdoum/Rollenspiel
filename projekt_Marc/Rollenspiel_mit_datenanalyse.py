import random
from datetime import datetime

# Funktion zur Erstellung eines neuen Spielercharakters
def erstelle_spieler():
    """
    Erstellt einen Standard-Spielercharakter mit voreingestellten Attributen.
    """
    spieler = {
        "name": "Held",  # Name des Spielers
        "gesundheit": 100,  # Gesundheitspunkte des Spielers
        "angriff": 10,  # Angriffskraft des Spielers
        "verteidigung": 5,  # Verteidigungswert des Spielers
        "inventar": []  # Liste der Gegenstände im Inventar
    }
    return spieler

# Funktion zur Simulation eines Levelaufstiegs
def levelaufstieg(spieler):
    """
    Erhöht die Attribute des Spielers beim Levelaufstieg.
    """
    spieler['gesundheit'] += 10
    spieler['angriff'] += 2
    spieler['verteidigung'] += 1
    print(f"{spieler['name']} ist aufgestiegen! Neue Attribute: "
          f"Gesundheit: {spieler['gesundheit']}, Angriff: {spieler['angriff']}, Verteidigung: {spieler['verteidigung']}.")

# Funktion zum Hinzufügen eines Gegenstands zum Inventar des Spielers
def inventar_hinzufuegen(spieler, gegenstand):
    """
    Fügt dem Inventar des Spielers einen neuen Gegenstand hinzu.
    """
    spieler['inventar'].append(gegenstand)
    print(f"{gegenstand} wurde zum Inventar hinzugefügt.")

# Funktion zur Erstellung eines neuen Gegners
def erstelle_gegner():
    """
    Erstellt einen Standard-Gegnercharakter mit voreingestellten Attributen.
    """
    gegner = {
        "name": "Kriegsmarine",  # Name des Gegners
        "gesundheit": 50,  # Gesundheitspunkte des Gegners
        "angriff": 8,  # Angriffskraft des Gegners
        "verteidigung": 3  # Verteidigungswert des Gegners
    }
    return gegner

# Funktion zur Analyse und Anzeige der Spielstatistiken
def analysiere_statistiken(statistiken):
    """
    Analysiert und zeigt die Spielstatistiken an (z. B. Kämpfe, Siegquote, Kampfdauer).
    """
    kaempfe = statistiken['Kaempfe']
    siege = statistiken['siege']
    niederlagen = statistiken['niederlagen']

    # Gewinnrate berechnen
    gewinnrate = (siege / kaempfe * 100) if kaempfe > 0 else 0

    # Statistiken ausgeben
    print("\nSpielstatistiken:")
    print(f"Gesamte Kämpfe: {kaempfe}")
    print(f"Siege: {siege}")
    print(f"Niederlagen: {niederlagen}")
    print(f"Gewinnrate: {gewinnrate:.2f}%")

    # Durchschnittliche Kampfdauer berechnen, falls vorhanden
    if 'kampfzeiten' in statistiken:
        kampfzeiten = statistiken['kampfzeiten']
        durchschnitt_dauer = sum(kampfzeiten) / len(kampfzeiten)
        print(f"Durchschnittliche Kampfdauer: {durchschnitt_dauer:.2f} Sekunden")

# Funktion zur Simulation eines Kampfes
def kampf(spieler, gegner, statistiken):
    """
    Simuliert einen Kampf zwischen dem Spieler und einem Gegner.
    """
    print(f"Ein Kampf zwischen {spieler['name']} und {gegner['name']} beginnt!\n")
    statistiken['Kaempfe'] += 1  # Erhöhe die Anzahl der Kämpfe

    start_zeit = datetime.now()  # Startzeit des Kampfes erfassen

    # Der Kampf läuft, solange beide Kämpfer noch Gesundheitspunkte haben
    while spieler['gesundheit'] > 0 and gegner['gesundheit'] > 0:
        # Spieler greift an
        kritischer_treffer = random.random() < 0.1  # 10% Chance auf kritischen Treffer
        spezieller_angriff = random.random() < 0.05  # 5% Chance auf speziellen Angriff
        schaden = max(0, spieler['angriff'] - gegner['verteidigung'])
        if kritischer_treffer:
            schaden *= 2
            print("Kritischer Treffer!")
        if spezieller_angriff:
            schaden *= 10
            print("Spezieller Angriff!")
        gegner['gesundheit'] -= schaden
        print(f"{spieler['name']} greift an und verursacht {schaden} Schaden bei {gegner['name']}. "
              f"{gegner['name']} hat noch {gegner['gesundheit']} Gesundheit.\n")

        # Überprüfen, ob der Gegner besiegt wurde
        if gegner['gesundheit'] <= 0:
            print(f"{gegner['name']} wurde besiegt!")
            statistiken['siege'] += 1
            break

        # Gegner greift an
        kritischer_treffer = random.random() < 0.1  # 10% Chance auf kritischen Treffer
        schaden = max(0, gegner['angriff'] - spieler['verteidigung'])
        if kritischer_treffer:
            schaden *= 2
            print("Kritischer Treffer!")
        spieler['gesundheit'] -= schaden
        print(f"{gegner['name']} greift an und verursacht {schaden} Schaden bei {spieler['name']}. "
              f"{spieler['name']} hat noch {spieler['gesundheit']} Gesundheit.\n")

        # Überprüfen, ob der Spieler besiegt wurde
        if spieler['gesundheit'] <= 0:
            print(f"{spieler['name']} wurde besiegt!")
            statistiken['niederlagen'] += 1
            break

        end_zeit = datetime.now()  # Endzeit des Kampfes erfassen
        kampf_dauer = (end_zeit - start_zeit).total_seconds()  # Kampfdauer berechnen
        print(f"Der Kampf dauerte: {kampf_dauer:.2f} Sekunden.\n")

        # Kampfdauer zu den Statistiken hinzufügen
        if 'kampfzeiten' not in statistiken:
            statistiken['kampfzeiten'] = []
            statistiken['kampfzeiten'].append(kampf_dauer)

# Hauptfunktion zum Start des Spiels
def spiel_starten():
        """
        Startet das textbasierte Rollenspiel und initiiert den ersten Kampf.
        """
        print("Willkommen zum textbasierten Rollenspiel!")  # Begrüßungstext
        print("Du bist ein Held, der gegen die Kriegsmarine kämpft.")
        print("Viel Glück auf deinem Abenteuer!\n")

        # Spieler und Gegner erstellen
        spieler = erstelle_spieler()
        gegner = erstelle_gegner()

        # Spielstatistiken initialisieren
        spiel_statistiken = {
                    "Kaempfe": 0,
                    "siege": 0,
                    "niederlagen": 0
                }

        # Spieler- und Gegnerattribute anzeigen
        print(f"Spieler:{spieler['name']} - Gesundheit: {spieler['gesundheit']}, Angriff:{spieler['angriff']}, Verteidigung: {spieler['verteidigung']}")
        print(f"Gegner: {gegner['name']} - Gesundheit: {gegner['gesundheit']}, Angriff: {gegner['angriff']}, Verteidigung: {gegner['verteidigung']}")

         # Kampf initiieren und Statistiken auswerten
        kampf(spieler, gegner, spiel_statistiken)
        analysiere_statistiken(spiel_statistiken)


# Wenn dieses Skript direkt ausgeführt wird, starte das Spiel
if __name__ == "__main__":
    spiel_starten()


