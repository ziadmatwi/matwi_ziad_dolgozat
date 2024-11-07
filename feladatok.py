import random

def parosfeladat():
    print("Első feladat:")
    szam:int=int(input("Kérem adjon meg egy páros számot: "))
    while szam % 2 != 0:
        szam=int(input("Hiba! A megadott szám nem volt páros! Kérem páros számot adjon meg: "))
    print (f"A megadott páros szám: {szam}")
            

def veletlenosztható():
    print("Második feladat:")
    i:int=0
    szam:int=0
    oszthato:int=0
    while i < 13:
        szam=int(random.random()*(151-10)+10)
        print (szam)
        if szam % 3 == 0:
            oszthato += 1
        i+=1
    print(f"A számok között {oszthato}db 3-al osztható van!")
    
def szoveghossz(text:str, N:int):
    if len(text) < N:
        print("Nincs N. karakter!")
    else: 
        nagybetu:str=text[N-1]
        print(f"A szöveg {N}. karaktere: {nagybetu.upper()*3}")