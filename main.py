import funzione1
import funzione2
import funzione3
import funzione4
import funzione5
import menu

#file main
reload = True #reload sarà la variabile che permetterà di usare il programma all'infinito. 

while reload == True:
  try: #prova a chiedergli in input la scelta del menu
    print(menu.stampamenu()) #visualizza il menu
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
  funzione1.addarticolo()
  reload = True
elif scelta == 2:
  funzione2.acquisto()
  reload = True
elif scelta == 3:
  funzione3.visualizzacategoria()
  reload = True
elif scelta == 4:
  funzione4.adddellcateg()
  reload = True
elif scelta == 5:
  funzione5.savetxt()
  reload = True

else:
  print("Comando non riconosciuto")
  reload = True
