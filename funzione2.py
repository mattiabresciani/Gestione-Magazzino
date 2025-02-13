#ALESSIO BENDANDI


articoli = [] 
quantita = []  
articoli1 = [] 
quantita1 = []  
articoli2 = [] 
quantita2 = []  


def acquisto(): 
    categoria = input("Inserisci la categoria dell'articolo che vuoi comprare (cartoleria-abbigliamento-casalinghi): ") 

    if categoria == "cartoleria":  
        articolo = input("Inserisci un articolo da aggiungere o rimuovere: ") 
        
        f = open("cartoleria.csv", "r")  
        righe = f.readlines()  
        f.close()  
        
        for riga in righe:  
            dati = riga.strip().split(",")  
            articoli.append(dati[0])  
            quantita.append(int(dati[1]))  

        if articolo in articoli:  
            for i in range(len(articoli)):  
                if articoli[i] == articolo:  
                    quantita[i] -= 1  
            
            if quantita[i] == 0:  
                articoli.pop(i)  
                quantita.pop(i)  

        else:  
            articoli.append(articolo)  
            quantita.append(1)  

        f = open("cartoleria.csv", "w")  
        for i in range(len(articoli)):  
            f.write(f"{articoli[i]},{quantita[i]}\n")  
        f.close()  

        print("Articoli aggiornati:", articoli)  
        print("Quantità:", quantita)  
     
    elif categoria == "casalinghi":  
        articolo = input("Inserisci un articolo da aggiungere o rimuovere: ") 
        
        f = open("casalinghi.csv", "r")  
        righe = f.readlines()  
        f.close()  
        
        for riga in righe:  
            dati = riga.strip().split(",")  
            articoli1.append(dati[0])  
            quantita1.append(int(dati[1]))  

        if articolo in articoli1:  
            for i in range(len(articoli1)):  
                if articoli1[i] == articolo:  
                    quantita1[i] -= 1  
            
            if quantita1[i] == 0:  
                articoli1.pop(i)  
                quantita1.pop(i)  

        else:  
            articoli1.append(articolo)  
            quantita1.append(1)  

        f = open("casalinghi.csv", "w")  
        for i in range(len(articoli1)):  
            f.write(f"{articoli1[i]},{quantita1[i]}\n")  
        f.close()  

        print("Articoli aggiornati:", articoli1)  
        print("Quantità:", quantita1)  
        
        
    elif categoria == "abbigliamento":  
        articolo = input("Inserisci un articolo da aggiungere o rimuovere: ") 
        
        f = open("abbigliamento.csv", "r")  
        righe = f.readlines()  
        f.close()  
        
        for riga in righe:  
            dati = riga.strip().split(",")  
            articoli2.append(dati[0])  
            quantita2.append(int(dati[1]))  

        if articolo in articoli2:  
            for i in range(len(articoli2)):  
                if articoli2[i] == articolo:  
                    quantita2[i] -= 1  
            
            if quantita2[i] == 0:  
                articoli2.pop(i)  
                quantita2.pop(i)  

        else:  
            articoli2.append(articolo)  
            quantita2.append(1)  

        f = open("abbigliamento.csv", "w")  
        for i in range(len(articoli2)):  
            f.write(f"{articoli2[i]},{quantita2[i]}\n")  
        f.close()  

        print("Articoli aggiornati:", articoli2)  
        print("Quantità:", quantita2)        
