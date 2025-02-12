def funzione1():
  categoria=input("Di quale categoria fa parte il tuo articolo: ")
  f=open(categoria+"csv","r")
  articolo=input("Quale articolo vuoi modificare? ")
  quantità=int("Qual è la nuova quantità? ")
  righe=f.readlines()
  f.close()
  for count in range(0,len(righe)):
    if righe[count[0]]==articolo:
      righe[count[1]]=quantità
  f=open(categoria+"csv","w")
  f.writelines(righe)
  f.close()
  
