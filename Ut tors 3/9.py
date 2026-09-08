import random
namn = input("Hej, vad heter du? ")
print(f"Hej {namn}! du ska få så nära 10 som möjligt men inte gå över. Jag slår första kastet och du får bestämma om du vill slå igen.")


tärning = random.randint (1,6)
tarning = random.randint (1,6)
tarnung = random.randint (1,6)
tärnung = random.randint (1,6)
tirnung = random.randint (1,6)
svar = input(f"Du fick {tärning} vill då slå igen? ")



if svar != "ja": 
    print(f"Du stannade på {tärning}. Bra jobbat, vill du spela igen? ")
    exit()
else:
    print(f"Du fick {tarning}, nu har du {tärning + tarning}. ") 

if tärning + tarning == 10:
    print("snyggt jobbat, du vann!")
    print("vill du spela igen")
    exit()
else:
    print()
    
if tärning + tarning > 10:
    print("du blev tjock")
    exit()
else:
    svara = input("Vill du fortsätta slå? ")



if svara == "ja":
    print(f"Du fick {tarnung}, nu har du {tärning + tarning + tarnung}. ")
else:
    print(f"Du stannade på {tärning + tarning}, vill du spela igen? ")
    exit()

if tärning + tarning + tarnung == 10:
    print("snyggt jobbat, du vann!")
    print("vill du spela igen")
    exit()
else:
    print()

if tärning + tarning + tarnung > 10:
    print("du blev tjock")
    exit()
else:
    svarade = input("Vill du fortsätta slå?")


if svarade == "ja":
    print(f"Du fick {tärnung}, nu har du {tärning + tarning + tarnung + tärnung}. ")
else:
    print(f"Du stannade på {tärning + tarning + tarnung}, vill du spela igen? ")
    exit()

if tärning + tarning + tarnung + tärnung == 10:
    print("snyggt jobbat, du vann!")
    print("vill du spela igen")
    exit()
else:
    print()

if tärning + tarning + tarnung + tärnung > 10:
    print("du blev tjock")
    exit()
else:
    svarat = input("Vill du fortsätta slå?")

if svarat == "ja":
    print(f"Du fick {tirnung}, nu har du {tärning + tarning + tarnung + tärnung + tirnung}. ")
else:
    print(f"Du stannade på {tärning + tarning + tarnung + tärnung}. Bra jobbat, vill du spela igen? ")
    exit()

if tärning + tarning + tarnung + tärnung + tirnung == 10:
    print("snyggt jobbat, du vann!")
    print("vill du spela igen")
    exit()
else:
    print()

if tärning + tarning + tarnung + tärnung + tirnung > 10:
    print("du blev tjock")
    exit()
else:
    svarate = input("Vill du fortsätta slå?")

