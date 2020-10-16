print("Se introduc trei date de forma număr curent elev, punctaj. Afişaţi numărul elevului cu cel mai mare punctaj.")
n1 = int (input("numarul primului elev este: "))
n2 = int (input("numarul al doilea elev este: "))
n3 = int (input("numarul al treilea elev este: "))
p1 = int (input("punctajul primului elev este: "))
p2 = int (input("punctajul al doilea elev este: "))
p3 = int (input("punctajul al treilea elev este: "))
if (( p1 > p2 ) and ( p1 > p3 )):
    print ( "Punctajul maxim are elevul cu numarul: " , n1 )
if (( p2 > p1 ) and ( p2 > p3 )):
    print ( "Punctajul maxim are elevul cu numarul: " , n2 )
if (( p3 > p1 ) and ( p3 > p2 )):
    print ( "Punctajul maxim are elevul cu numarul: " , n3 )
if (( p1 == p2 ) and ( p1 > p3 ) and ( p2 > p3 )):
    print ( "Elevii cu numerele: " ,n1 , n2 , "au acelasi punctaj" )
if (( p1 == p3 ) and ( p1 > p2 ) and ( p3 > p2 )):
    print (" Elevii cu numerele:", n1 , n3 , "au acelasi punctaj" )
if (( p2 == p3 ) and ( p2 > p1 ) and ( p3 > p1 )):
    print ( "Elevii cu numerele: " , n2 , n3 , "au acelasi punctaj" )
if  (( p2 == p3 ) and ( p2 == p1 ) and ( p3 == p1 )):
    print ( "Toti elevii au acelasi punctaj" )