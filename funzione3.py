import os

def visualizzacategoria():
    current_folder = os.getcwd()  #visualizza il contenuto della cartella in cui si sta lavorando

    nomi_categorie = [os.path.splitext(file)[0] for file in os.listdir(current_folder) if file.endswith('.csv')] #array che contiene 

    print("Categorie:\n")

    for c in range(len(nomi_categorie)):
        print("-", nomi_categorie[c].capitalize())
    print("\n")

    str_visual = str(input("Inserisci la categoria da visualizzare\n    >>      "))

    str_visual = str_visual.lower()

    reload = False

    while reload == False:
        try:
            f = open(str_visual+".csv")
            reload = True

        except FileNotFoundError:
            print("\nCategoria non trovata, assicurati di averlo scritto correttamente.")
            str_visual = str(input("    >>      "))
            reload = False

    row = f.readline()

    while row != "":
        articolo = row.split(",")
        print("-", articolo[0], "  in quantità: ", articolo[1])

        row = f.readline()

    reloadmenu = True

    return reloadmenu

#Mattia Bresciani
