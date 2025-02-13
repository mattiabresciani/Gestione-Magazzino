#ALESSIO BENDANDI
dati = []
dati1 = []
dati2 = []
dati3 = []
dati4 = []
dati5 = []

def function5():
    dati.clear()
    dati1.clear()
    dati2.clear()
    dati3.clear()
    dati4.clear()
    dati5.clear()

    f = open("abbigliamento.csv", "r")
    riga = f.readline()
    while riga != "":
        rig = riga.strip().split(",")
        if len(rig) == 2:
            dati.append(rig[0])
            dati1.append(rig[1])
        riga = f.readline()
    f.close()

    s = open("cartoleria.csv", "r")
    line = s.readline()
    while line != "":
        lin = line.strip().split(",")
        if len(lin) == 2:
            dati2.append(lin[0])
            dati3.append(lin[1])
        line = s.readline()
    s.close()

    t = open("casalinghi.csv", "r")
    linea = t.readline()
    while linea != "":
        li = linea.strip().split(",")
        if len(li) == 2:
            dati4.append(li[0])
            dati5.append(li[1])
        linea = t.readline()
    t.close()

    x = open("file.txt", "w")
    for i in range(len(dati)):
        x.write("ABBIGLIAMENTO:")
        x.write(dati[i] + " " + dati1[i] + "\n")
    
    for i in range(len(dati2)):
        x.write("CARTOLERIA:")
        x.write(dati2[i] + " " + dati3[i] + "\n")
    
    for i in range(len(dati4)):
        x.write("CASALINGHI:")
        x.write(dati4[i] + " " + dati5[i] + "\n")

function5()

