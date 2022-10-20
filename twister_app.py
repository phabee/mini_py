import random

while True:
    print('Enter fuer weiter!')
    x = input()
    a = random.randint(0, 3)
    txt = ""
    if a == 0:
        txt = "Rechte Hand"
    elif a == 1:
        txt = "Rechter Fuss"
    elif a == 2:
        txt = "Linke Hand"
    else:
        txt = "Linker Fuss"

    b = random.randint(0, 5)
    farbe = ""
    if b == 0:
        farbe = "Twister"
    elif b == 1:
        farbe = "rot"
    elif b == 2:
        farbe = "gruen"
    elif b == 3:
        farbe = "Luft"
    elif b == 4:
        farbe = "gelb"
    else:
        farbe = "blau"
    
    print(txt, farbe)
