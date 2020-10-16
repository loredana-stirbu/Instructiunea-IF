print("Se dau trei numere. Să se afişeze aceste numere unul sub altul, afişând în dreptul fiecăruia unul dintre cuvintele PAR sau IMPAR.")
a=int(input("Dati primul numar: ")) 
b=int(input("Dati al doilea numar: ")) 
c=int(input("Dati al treilea numar: ")) 
if ((a%2==0)and(b%2==0)and(c%2==0)): 
    print("Toate numerele sunt pare")
if ((a%2==0)and(b%2==0)and(c%2!=0)): 
    print(a,"e PAR,",b,"e PAR,",c,"e IMPAR,",sep=" ") 
if ((a%2==0)and(b%2!=0)and(c%2==0)): 
    print(a,"e PAR,",b,"e IMPAR,",c,"e PAR,",sep=" ") 
if ((a%2!=0)and(b%2==0)and(c%2==0)): 
    print(a,"e IMPAR,",b,"e PAR,",c,"e PAR,",sep=" ") 
if ((a%2!=0)and(b%2!=0)and(c%2==0)): 
    print(a,"e IMPAR,",b,"e IMPAR,",c,"e PAR,",sep=" ") 
if ((a%2!=0)and(b%2==0)and(c%2!=0)): 
    print(a,"e IMPAR,",b,"e PAR,",c,"e IMPAR,",sep=" ") 
if ((a%2==0)and(b%2!=0)and(c%2!=0)): 
    print(a,"e PAR,",b,"e IMPAR,",c,"e IMPAR,",sep=" ") 
if ((a%2!=0)and(b%2!=0)and(c%2!=0)): 
    print("Toate numerele sunt impare")