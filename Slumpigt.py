import random

gissning = int(input("Gissa vilken siffra jag tänker på. "))

nummer = random.randint (0,9)
while gissning != nummer:
    if nummer != gissning: 
        print("Du hade fel!")
    gissning = int(input("gissa igen apa! "))
else: 
    print("du hade jätte rätt, hahahaha!")
         