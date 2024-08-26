import random as r
import time as t
liste = [0,]
def add_to_list(numbers):
    global liste
    #nummern an liste anfügen
    liste.append(numbers)
def random():
    global anzahl
    global g
    #bestimmen wie viele nummern generiert werden sollen
    i1 = int(input("""willst du sleber eine range angeben[1], 
oder willst du eine feste zahl angeben[2], 
oder willst du standart zwischen 50-100 eine range haben?[3]?: """))

    if i1 == 1:
        rl1 = int(input("start deiner Range: "))
        rl2 = int(input("ende deiner Range:"))
        anzahl = r.randint(rl1,rl2)    
    elif i1 == 2:
        rl3 = int(input("wie viele zahlen sollen generiert werden?: "))
        anzahl = rl3
    elif i1 == 3:
        anzahl = r.randint(50,100)
    g = int(input("wie groß darf die zahl maximal sein?: "))
    print(f"es werden {anzahl} nummern generiert")
    #for loop für nummer generation
    for _ in range(anzahl):
        n = r.randint(1,g)
        add_to_list(numbers=n)

def main():
    #nummer generation starten
    random()
    print(liste)
    #nach zu suchender zahl fragen
    i = int(input(f"welche zahl suchst du range=1-{g}?: "))

    counter = 0
    #such loop starten
    for f in range(anzahl):
        f = f+1
        if liste[f] == i:
            counter+=1

            print(f"die zahl {i} wurde an stelle {f} in der liste gefunden")
        else:
            pass
    print(f"die zahl {i} wurde {counter} mal in der liste aus {anzahl} zahlen gefunden")
            


if __name__ == "__main__":
    main()