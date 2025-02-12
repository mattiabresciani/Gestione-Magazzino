def function2():
  categoria=input("Inserisci la categoria dell'articolo che vuoi comprare casalinghi-cartoleria-abbigliamento")
  if categoria == "cartoleria":
    artcolo = input("Inserisci un articolo da aggiungiere o da rimuovere")
    f = open("cartoleria.csv","w")
    riga = f.readline()
    if riga != "":
      print(riga)
      riga = f.readline()
      f.close()
                  
                  
                        
