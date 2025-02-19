def addarticolo():
    lista = []
    categoria = input("Di quale categoria fa parte il tuo articolo: ")
    
    # Modifica la modalità di apertura del file per permettere la lettura senza perdita di dati
    try:
        f = open(categoria + ".csv", "r")
    except FileNotFoundError:
        print(f"Il file {categoria}.csv non esiste.")
        return
    
    # Lettura dei dati esistenti
    riga = f.readline()
    while riga != "":
        dati = riga.strip().split(",")
        lista.append(dati)
        riga = f.readline()
    f.close()

    articolo = input("Quale articolo vuoi modificare? ")
    while articolo not in lista:
        articolo = input("Errore! L'articolo che cerci di modificare non è presente nel magazzino, riprova ")
    quantità = int(input("Qual è la nuova quantità? "))
    while quantità < 0:
        quantità=int(input("Errore! Inserisci una quantità possibile ")

    # Modifica la quantità dell'articolo
    for i in range(len(lista)):
        if lista[i][0] == articolo:
            lista[i][1] = str(quantità)  # Assicurarsi che la quantità sia convertita in stringa

    # Scrittura dei dati aggiornati nel file
    f = open(categoria + ".csv", "w")
    for elemento in lista:
        f.write(",".join(elemento) + "\n")
    f.close()

#Matteo Saladino
