szam1 = int(input("Írja be az első számot: "))
szam2 = int(input("Írja be a második számot: "))
if szam1 >= szam2:
    if szam1 == szam2:
        print("Mindkét szám egyenlő.")
    else:
        print("Az első szám nagyobb, mint a második")
else:
    print("A második szám nagyobb, mint az első szám.")