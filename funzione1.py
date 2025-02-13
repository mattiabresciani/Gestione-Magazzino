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
  for count in range(0,len(lista)):
    if lista[count][0]==articolo:
      lista[count][1]=quantità
  f=open(categoria+".csv","w")
  f.writelines(str(lista))
  f.close()

