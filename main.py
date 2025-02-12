#file main
reload = True #reload sarà la variabile che permetterà di usare il programma all'infinito. 

while reload == True:
  try: #prova a chiedergli in input la scelta del menu
    scelta = int(input("Inserisci l'opzione \n >>    "))
    reload = False
  except ValueError: #se l'utente inserisce un numero float
    print("Errore nell'inserimento del comando. Ricontrolla.")
    reload = True
  except TypeError: #se l'utente inserisce una stringa
    print("Errore nell'inserimento del comando. Ricontrolla.")
    reload = True


#Inizio parte della selezione e dei controlli. (gestione input)
if scelta == 0:
  print("Fine esecuzione programmi")
  reload = False #siccome non ci sarà nulla da fare il programma si chiude
elif scelta == 1:
  #vai alla funzione1
elif scelta == 2:
  #vai alla funzione2
elif scelta == 3:
  #vai alla funzione3
elif scelta == 4:
  #vai alla funzione4
elif scelta == 5:
  #vai alla funzione5
else:
  print("Comando non riconosciuto")
  reload = True
