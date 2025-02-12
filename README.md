# Gestione-Magazzino
Compito di informatica in python.- scrivere un programma che gestisca il magazzino di un negozio di articoli vari (abbigliamento, casalinghi, cartoleria, etc )
 - deve essere possibile gestire per ogni articolo la quantità disponibile, ad esempio: gomme ne ho 5, penne blu ne ho 7, quaderni a righe ne ho 11
 - la gestione degli articoli di un certo tipo/categoria deve essere separata, ad esempio: gli articoli di cartoleria dovranno essere gestiti un una struttura dati, gli articoli di casalinghi (piatti, bicchieri, etc) in un'altra, etc.
 - il programma dovrà consentire di memorizzare, modificare la quantità (aumentare o diminuire), inserire e eliminare voci di magazzino di una categoria/tipo scelto dall'utente;

Esempio di menù:

Scegli una opzione:
1 - modifica quantità di un articolo 
2 - aggiungi o rimuovi articolo
3 - stampa elenco articoli in una categoria 
4 - aggiungi o rimuovi categoria di articoli 
5 - salva informazioni di magazzino su un file .txt
0 - esci

Se l'utente sceglie 1 allora il programma:
- chiederà la categoria dell'articolo da modificare
- chiederà l'articolo da modificare 
- chiederà la nuova quantità (oppure chiede se aumentare di quanto o diminuire di quanto)
- aggiornerà il valore della quantità dell l'articolo 

Se l'utente sceglie 2 allora il programma chiederà categoria e articolo da aggiungere o rimuovere

Se utente sceglie 3 stamperà elenco articoli di quella categoria, con quantità di ognuno

Se utente sceglie 4, chiederà il nome della categoria da aggiungere alle categorie possibili (e aggiungerà la categoria)
oppure eliminerà la categoria specificata

Domanda 1: quale strutture dati possono rappresentare/ contenere i dati?

Suggerimento: se un array può contenere degli array, allora anche una .... può contenere...

Domanda 2: come posso evitare di fare input iniziale di tante informazioni?

Suggerimento: abbiamo imparato a utilizzare i file... altrimenti inizializzate i valori direttamente nel codice

Si chiede di realizzare il programma che esegue le funzioni da 1 a 4.
La funzione 5 è facoltativa.
Si chiede di preparare una semplice relazione di spiegazione delle scelte di progettazione fatte.

