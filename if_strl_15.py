print("Elevii clasei a V-a se repartizează în clase câte 25 în ordinea mediilor clasei a IV-a. Radu este pe locul x în ordinea mediilor. În ce clasa va fi repartizat (A, B, C, D sau E)?.")
x=int(input("Radu se afla pe locul: ")) 
if (x//25==0): 
    print("A") 
if (x//25==1): 
    print("B") 
if (x//25==2): 
    print("C") 
if (x//25==3): 
    print("D") 
if (x//25==4): 
    print("E")