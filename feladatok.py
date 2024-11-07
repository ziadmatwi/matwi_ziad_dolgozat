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
    print("Harmadik feladat:")
    if len(text) < N:
        print("Nincs N. karakter!")
    else: 
        nagybetu:str=text[N-1]
        print(f"A szöveg {N}. karaktere: {nagybetu.upper()*3}")

def nevkeres():
    print("Ez a negyedik feladatok:")
    nevszamlalo:int=0
    megadottnev:str=""
    while megadottnev != "@":
        megadottnev=input("Kérem adjon meg egy nevet: ")
        nevszamlalo+=1
    print(f"A felhasználó {nevszamlalo-1} nevet adott meg.")

def kopapirollo():
    print("Ötödik feladat: ")
    felhasznalo_tippje:str=input("Ez egy Kő! Papír! Olló! játék. Tippeljen!: ")
    felhasznalo_tippje=felhasznalo_tippje.lower()
    while felhasznalo_tippje != "kő" and felhasznalo_tippje != "papír" and  felhasznalo_tippje != "olló":
        felhasznalo_tippje:str=input("Hiba! Csak 'kő', 'papír' vagy 'olló' választható. Adjon meg újra egy tippet: ")
        felhasznalo_tippje=felhasznalo_tippje.lower()

    gep_tippje:int=int(random.random()*(4-1)+1)
    if gep_tippje == 1:
        gepmutat:str= "kő"
    elif gep_tippje == 2:
        gepmutat:str= "papír"
    elif gep_tippje == 3:
        gepmutat:str= "olló"
    print(f"A gép ezt mutatja: {gepmutat}")

    if gepmutat == felhasznalo_tippje:
        print("Az eredmény döntetlen!")

    elif gepmutat == "kő" and felhasznalo_tippje == "olló":
        print("A gép nyert")
    
    elif gepmutat == "olló" and felhasznalo_tippje == "papír":
        print("A gép nyert")
    
    elif gepmutat == "papír" and felhasznalo_tippje == "kő":
        print("A gép nyert")

    elif felhasznalo_tippje == "kő" and gepmutat == "olló":
        print("Te nyertél!")

    elif felhasznalo_tippje == "papír" and gepmutat == "kő":
        print("Te nyertél!")

    elif felhasznalo_tippje == "olló" and gepmutat == "papír":
        print("Te nyertél!")

print("A játéknak vége!")

    
   

