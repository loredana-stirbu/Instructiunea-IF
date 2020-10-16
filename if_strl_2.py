print("La ora de matematică Gigel este scos la tablă. Profesoara îi dictează trei numere şi îi cere să verifice dacă cele trei numere pot fi laturile unui triunghi. Ajutaţi-l pe Gigel  să afle rezultatul. Scrieţi un program care primeşte numerele lui Gigel, care sunt mai mici ca 32000, şi returnează DA sau NU. Observaţie: Trei numere pot fi laturile unui triunghi  numai dacă fiecare este mai mic ca suma celorlalte două.")
a=int(input("Dati primul numar: ")) 
b=int(input("Dati al doilea numar: ")) 
c=int(input("DAti al treilea numar:")) 
if ((a<a+b)and(b<c+a)and(c<a+b)): 
    print("Da") 
else: 
    print("Nu")