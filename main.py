import funzione1
import funzione2
import funzione3
import funzione4
import funzione5
import menu

esegui = True  #variabile di controllo per mantenere il loop attivo

while esegui:
    try:
        print(menu.stampamenu())  #visualizza il menu
        scelta = int(input("Inserisci l'opzione \n >>    "))
    except ValueError:  #se l'utente inserisce un valore non intero
        print("Errore nell'inserimento del comando. Ricontrolla.")
        continue  #torna all'inizio del loop
    except TypeError:
        print("Errore nell'inserimento del comando. Ricontrolla.")
        continue

    #gestione delle scelte
    if scelta == 0:
        print("Fine esecuzione programma")
        esegui = False  #imposta la variabile per uscire dal loop
    elif scelta == 1:
        funzione1.addarticolo()
    elif scelta == 2:
        funzione2.acquisto()
    elif scelta == 3:
        funzione3.visualizzacategoria()
    elif scelta == 4:
        funzione4.adddellcateg()
    elif scelta == 5:
        funzione5.savetxt()
    else:
        print("Comando non riconosciuto")
