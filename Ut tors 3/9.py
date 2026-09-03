import random
namn = input("Hej, vad heter du?")
print(f"Hej {namn}! du ska få så nära 10 som möjligt men inte gå över. Jag slår första kastet och du får    bestämma om du vill slå igen.")
tärning = random.randint (1,6)
tarning = random.randint (1,6)
tarnung = random.randint (1,6)

svar = input(f"Du fick {tärning} vill då slå igen? ")

if svar == "ja":
    svara = input(f"Du fick {tarning}, nu har du {tärning + tarning}. Vill du fortsätta slå? ")
else:
    svara = print(f"Du stannade på {tärning}. Bra jobbat, vill du spela igen? ")
if svara == "ja":
     svara = input(f"Du fick {tarnung}, nu har du {tärning + tarning + tarnung}. Vill du fortsätta slå? ")
else:
    print(f"Du stannade på {tärning + tarning}. ")