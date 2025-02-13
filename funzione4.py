def funzione4():
    categoria = input("Inserisci il nome della categoria che vuoi aggiungere o rimuovere: ")
    f = open(categoria+".csv", "w")
    f.close()
funzione4()
