print("Cunoscând data curentă exprimată prin trei numere întregi reprezentând anul, luna, ziua precum şi data naşterii unei persoane, exprimată la fel, să se facă un program care să  calculeze vârsta persoanei respective în număr de ani împliniţi.")
ac=int(input("Anul curent: ")) 
lc=int(input("Luna curenta: ")) 
zc=int(input("Ziua curenta: ")) 
an=int(input("Anul nasterii: ")) 
ln=int(input("Luna nasterii: ")) 
zn=int(input("Ziua nasterii: ")) 
if (ln==lc): 
    if ((zc>zn)or(zc==zn)): 
        print(ac-an,"ani") 
    else: 
        print((ac-an)-1,"ani") 
if (ln<lc): 
    print(ac-an,"ani") 
else: 
    print((ac-an)-1,"ani")