#file main
Reload = True

while reload == True:
  try:
    scelta = int(input("Inserisci l'opzione \n >>    "))
    reload = False
  except ValueError:
    print("Errore nell'inserimento del comando. Ricontrolla.")
    reload = True
  except TypeError:
    print("Errore nell'inserimento del comando. Ricontrolla.")
    reload = True

if scelta == 0:
  print("Fine esecuzione programmi")
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
