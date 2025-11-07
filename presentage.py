from unittest import case

print("Welk type procentsom wil je oplossen; maak je keuze:")
print("[1] Hoeveel is x% van y?")
print("[2] Hoeveel % is x van y")
print("[3] y neemt toe met x%, hoeveel heb je nu? ")
print("[4] y neemt af met x%, hoeveel heb je nu?")
print("[5] x is toegenomen naar y, hoeveel procent is het toegenomen?")
print("[6] x is afgenomen naar y, met hoeveel procent is het afgenomen?")
kies = input("Welke optie kies je?")
match kies:
    case "1":
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        answer = x / 100 * y
        print("De vraag is: hoeveel is " + str(x) + "% van " + str(y) + "?")
        print("Het antwoord is: " + str(answer))
    case "2":
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        print(f"De vraag is: hoeveel % is {x} van {y}")
        answer = x / y * 100
        print(f"Het antwoord is : {answer}")
    case "3":
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        print(f"De vraag is: {x} neemt toe met {y}%, hoeveel heb je nu? ")
        answer = x *((y / 100) +1)
        print(f"Het antwoord is : {answer}")
    case "4":
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        answer = ((100 - x)/100) * y
        print(f"Het antwoord is : {answer}")
    case "5":
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        answer = ((y / x) -1) * 100
        print(f"Het antwoord is : {answer:.0f}%")
    case "6":
        x = float(input("Wat is x?"))
        y = float(input("Wat is y?"))
        answer = (1 - (x / y) )* 100
        print(f"Het antwoord is : {answer:.0f}%")       
    case _:
        print("je hebt een ongeldige optie gekozen")