print("Pe o masă de biliard sunt bile albe, roşii şi verzi. Din fiecare culoare sunt bile de două dimensiuni: mari şi mici. Să se afişeze câte bile sunt în total pe masa de biliard. Un jucător vrea să-i spuneţi care bile sunt mai multe , cele mici sau cele mari, afişând numărul lor. De ce culoare sunt bilele cele mai numeroase? Precizaţi numărul lor.")
xa=int(input("Numarul de bile albe mici: ")) 
xr=int(input("Numarul de bile rosii mici: ")) 
xv=int(input("Numarul de bile verzi mici: ")) 
ya=int(input("Numarul de bile albe mari: ")) 
yr=int(input("Numarul de bile rosii mari: ")) 
yv=int(input("Numarul de bile verzi mari: ")) 
xt=xa+xr+xv 
yt=ya+yr+yv 
print("Numarul total de bile:",xt+yt) 
if (xt>yt): 
    print("Mai multe bile mici (",xt,")") 
if (yt>xt): 
    print("Mai multe bile mari (",yt,")")
if (yt==xt): 
    print("Numarul de bile mici si mari sunt egale") 
if ((xa+ya>xr+yr)and(xa+ya>xv+yv)): 
    print("Bile albe:",xa+ya) 
if ((xr+yr>xa+ya)and(xr+yr>xv+yv)):
    print("Bile rosii:",xr+yr) 
if ((xv+yv>xa+ya)and(xv+yv>xr+yr)): 
    print("Bile verzi:",xv+yv) 
if ((xa+ya==xr+yr)and(xr+yr>xv+yv)): 
    print("Numarul de bile albe si rosii sunt egale:",xa+ya) 
if ((xr+yr==xv+yv)and(xr+yr>xa+ya)): 
    print("Numarul de bile verzi si rosii sunt egale:",xr+yr) 
if ((xa+ya==xv+yv)and(xa+ya>xr+yr)): 
    print("Numarul de bile albe si verzi sunt egale:",xa+ya) 
if ((xa+ya==xv+yv)and(xa+ya==xr+yr)and(xr+yr==xv+yv)):
    print("Numarul de bile albe, rosii si verzi sunt egale:", xa+ya)