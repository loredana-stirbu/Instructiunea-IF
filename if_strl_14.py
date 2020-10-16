print("Într-o tabără, băieţii sunt cazaţi câte 4 într-o căsuţă, în ordinea sosirii. Ionel a sosit al n-lea. În a câta căsuţă se va afla?")
n=int(input("Ionel a sosit al: ")) 
if (n<=4):
    print("Ionel va fi cazat in casuta cu numarul: 1")
else:
    print("Ionel va fi cazat in casuta cu numarul: ",(n//4)+1)