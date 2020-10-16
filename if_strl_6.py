print("Andrei primeşte într-o zi trei note, nu toate bune. Se hotărăşte ca, dacă ultima notă este cel puţin 8, să le spună părinţilor toate notele primite iar dacă este mai mică decât 8, să le comunice doar cea mai mare notă dintre primele două. Introduceţi notele luate şi afişaţi notele pe care le va comunica părinţilor.")
print("Introdu notele cuprinse intre 1 si 10") 
a=int(input("Prima nota este: ")) 
b=int(input("A doua nota este: ")) 
c=int(input("A treia nota este: ")) 
if (c>=8): 
    print(a,b,c,sep=" ") 
if (c<8): 
    if (a>b): 
        print(a) 
    else: 
        print(b)