import os
def funzione4():
    categoria = input("Inserisci il nome della categoria che vuoi aggiungere o rimuovere: ")
    if os.path.exists(categoria+".csv"):
        os.remove(categoria+".csv")
    else:
        f=open(categoria+".csv","w")
        f.close()
