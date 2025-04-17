##Zufallsautomat - "gemeine Getränke!"

import random

start = input("""Guten Tag, herzlich Willkommen & Bienvenue
    Was willste trinken?
    Es gibt:
     Pepsi: 2,30 EUR
     Mangosaft-Schorle: 3,40 EUR
     Sprudeli: 0,90 EUR
     Lauwarmes Wasser: 3,80 EUR
     Mezzomix: 1,80 EUR
     und Kakao für 2,50 EUR \
     """).lower().replace("-", "")

print(start)

getraenke_dict = {"pepsi": 2.3, "mangosaftschorle": 3.4, "sprudeli": 0.9, "lauwarmeswasser": 3.8, "mezzomix": 1.8, "kakao": 2.5 }
zufallswahl =random.choice(list(getraenke_dict.keys()))
if zufallswahl== start:
    print (f"Sie wissen, was gut ist und jetzt {getraenke_dict.get(zufallswahl):.2f} EUR her!")
else:
    match start:
        case "pepsi":
            print(f"Pepsi ist nur für coole Leute.")
        case "mangosaftschorle":
            print("Fruchtzucker ist auch Zucker!")
        case "sprudeli":
            print("Sprudel ist langweilig.")
        case "lauwarmeswasser":
            print(f"Da haben Sie sich wohl verwählt.")
        case "mezzomix":
            print(f"Mixen ist was für Cocktailbars!")
        case "kakao":
            print(f"Kakao? Wie alt sind Sie???")

    match zufallswahl:
        case "pepsi":
            print(f"Sie kriegen Pepsi - das ist was für coole Leute. Geben Sie {getraenke_dict.get(zufallswahl):.2f} EUR her!.")
        case "mangosaftschorle":
            print(f"Sie brauchen Exotik in der Flasche - Mango Saft Schorle: {getraenke_dict.get(zufallswahl):.2f} EUR her!")
        case "sprudeli":
            print(f"Sprudel ist was Freshes! Zahl {getraenke_dict.get(zufallswahl):.2f} EUR .")
        case "lauwarmeswasser":
            print(f"Lauwarmes Wasser ist gut für die Verdauung; rück {getraenke_dict.get(zufallswahl):.2f} EUR raus.")
        case "mezzomix":
            print(f"Sie trinken Mezzomix, bis Sie sich richtig entscheiden können. Gib {getraenke_dict.get(zufallswahl):.2f} EUR")
        case "kakao":
            print(f"Hm... Kakao für dein inneres Kind. Das macht {getraenke_dict.get(zufallswahl):.2f} EUR von deinem Taschengeld.")



    geldeingabe = float(input("Gib die Kohle her: "))


    preis = getraenke_dict[zufallswahl]

while True:
    if geldeingabe < preis:
        print("Das ist nicht genug. Wirf mehr ein!")
        geldeingabe_neu = float(input("Gib die Kohle her: "))
        geldeingabe += geldeingabe_neu
        #print (geldeingabe_neu)
        continue
    else:
        break

if geldeingabe > preis:
        rueckgeld = geldeingabe - preis
        print(f"Hier ist dein Drecksgetränk. Nimm deine {rueckgeld:.2f} EUR mit und schau, dass du Land gewinnst")


if geldeingabe == preis:
            print("Hier ist dein Zeug.")