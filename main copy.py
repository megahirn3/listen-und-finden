import random as r
import time as t
liste = [0,]
def add_to_list(numbers):
    global liste
    #nummern an liste anfügen
    liste.append(numbers)
def random():
    global anzahl
    #bestimmen wie viele nummern generiert werden sollen
    anzahl = r.randint(50,100)
    print(f"es werden {anzahl} nummern generiert")
    #for loop für nummer generation
    for _ in range(anzahl):
        n = r.randint(1,10)
        print(n)
        add_to_list(numbers=n)
        t.sleep(0.1)
        
    
def main():
    #nummer generation starten
    random()
    print(liste)
    #nach zu suchender zahl fragen
    i = int(input("welche zahl suchst du range=1-10?: "))
    counter = 0
    #such loop starten
    for f in range(anzahl):
        f = f+1
        if liste[f] == i:
            counter = counter +1
        else:
            pass
    print(f"die zahl {i} wurde {counter} mal in der liste aus {anzahl} zahlen gefunden")
            


main()