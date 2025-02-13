def funzione1():
  lista=[]
  categoria=input("Di quale categoria fa parte il tuo articolo: ")
  f=open(categoria+".csv","r")
  articolo=input("Quale articolo vuoi modificare? ")
  quantità=int(input("Qual è la nuova quantità? "))
  riga=f.readline()
  while riga!="":
    dati=riga.strip().split(",")
    lista.append(dati)
    riga=f.readline()
  f.close()
  for i in range(0,len(lista)):
    if lista[i][0]==articolo:
      lista[i][1]=quantità
  f=open(categoria+".csv","w")
  for elemento in lista:
    f.write(",".join(elemento)+ "\n")
  f.close()
