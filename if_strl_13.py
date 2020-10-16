print("La un concurs se dau ca premii primilor 100 de concurenţi, tricouri de culoare albă, roşie, albastră şi neagră, în această secvenţă. Ionel este pe locul x. Ce culoare va avea tricoul  pe care-l va primi?")
x=int(input("Locul ocupat de Ionel: ")) 
if (x>100): 
    print("Nu primeste tricou") 
if (x%4==1): 
    print("alb") 
if (x%4==2): 
    print("rosu") 
if (x%4==3): 
    print("albastru") 
else:
    print("negru")