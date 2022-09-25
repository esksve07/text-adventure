
from operator import truediv

from random import randint
visited_keyroom = False
visited_hammerroom = False
visited_gassroom = False

Gassmaske = 0
Nøkkel = 0
Hammer = 0




def room0():
    print("")
    print("Velkommen")
    print("Du er nå låst inne og fanget")
    print("Finn veien ut, lykke til")
    asking = True
    while asking:
        valg = input("Start?->")

        if valg == "Start":
            asking = False
            room1()
        else:
            print("Error",valg)



def room1(): #start rom 2,4 og 6
    print("")
    print("Rom 1")
    print("Velg en dør")
    asking = True
    while asking:
        valg = input("Dør A: Dør B: Dør C:->")

        if  valg == "A":
            asking = False
            room2()
        elif valg == "B":
            asking = False
            room4()
        elif valg == "C":
            asking = False
            room6()
        else:
            print("Error",valg)

def room2(): #trenger nøkkel for å senke broa # 3,5 
    global Nøkkel
    print("")
    print("Rom 2")
    print("Mellom deg og de neste dørene er de et stort svart hull")
    print("På andre siden kan du skimte en bro")
    print("Du ser et nøkkelhull på veggen")
    print("Du trenger en nøkkel")
    asking = True
    while asking == True:
        print("")
        valg = input("Bruk nøkkelen A: Gå tilbake B:->")

        if  valg == "A":
            asking = False
            if Nøkkel >= 1:
                print("")
                print("Du fant nøkkelen")
                print("Godt jobba")
                print("Du setter nøkkelen i hullet og vrir om")
                print("Broen går ned")
                print("Du kan nå gå over")
                print("Velg en dør")
                asking2 = True
                while asking2 == True:
                    print("")
                    valg = input("Dør A: Dør B:->")

                    if valg == "A":
                        asking2 = False
                        room3()
                    elif valg == "B":
                        asking2 = False
                        room5()

            elif Nøkkel <= 0:
                print("")
                print("Kom tilbake når du har nøkkelen")
                room1()
        elif valg == "B":
            asking = False
            room1()
        else:
            print("Error",valg)
        

def room3():
    print ("")
    print("Rom 3")
    print("På veggen ser du et morsomt bilde")
    print("Du ler og går videre")
    room13()

def room4(): # nøkkelrom # 13
    global Nøkkel, Hammer, visited_keyroom
    if visited_keyroom == True:
        room13()
    else:
        print("")
        print("Rom 4")
        print("Rommet har ingen annen vei ut enn tilbake")
        print("Du ser nøkkelen ligge i en glassboks mids i rommet")
        print("Du trenger en hammer")
        asking = True
        while asking == True:
            print("")
            valg = input("Ødelegg glasset A: Gå tilbake B:->")

            if valg == "A":
                asking = False
                if Hammer >= 1:
                    print("")
                    print("Glasset gikk i tusen biter")
                    print("Nøkkelen er fri")
                    Nøkkel += 1
                    visited_keyroom = True
                    print("Du tar med deg nøkkelen og forlater rommet")
                    room1()
                    
                elif Hammer <= 0:
                    print("")
                    print("Du mangler nøkkelen")
                    print("Finn den!")
                    print("")
                    room1()

            elif valg == "B":
                asking = False
                room1()
            else:
                print("Error",valg)


def room5(): #
    print("")
    print("Rom 5")
    print("Velg en dør")
    asking = True
    while asking == True:
        print("")
        valg = input("Dør A: Dør B:->")

        if  valg == "A":
            asking = False
            room3()
        elif valg == "B":
            asking = False
            room5()
        else:
            print("Error",valg)


def room6():
    global Hammer, visited_hammerroom
    if visited_hammerroom == True:
        room1()
    else:
        print("")
        print("Rom 6")
        print("Det er ingenting hær")
        print("Bare et tomt rom")
        print("Du ser deg rundt å får øye på en hammer")
        Hammer += 1
        print("Du plukker opp hammeren og går ut av rommer")
        visited_hammerroom = True
        room1()


def room7():
    global Gassmaske, Nøkkel
    print("")
    print("Rom 7")
    print("Rommet er fullt av gass")

    if Gassmaske >= 1:
        print("Du kommer deg gjennom rommet")
        print("Takked være gassmasken")
        print("Men på veien gjennom rommet fester noe seg under skoen din")
        print("Det er en nøkkel")
        Nøkkel += 1
        room3()

    elif Gassmaske <=1:
        print("Du får ikke puste")
        print("Du løper tilbake ut av rommet")
        room9()


def room8():
    global Gassmaske
    print("")
    print("Rom 8")
    print("Som rom tidligere har dette rommet også bare en dør")
    print("På veggen et stykke inn i rommet henger en gassmaske")
    print("Du går å henter den og forlater rommet")
    Gassmaske += 1
    room9()


def room9(): # gjennom døra i rom 13
    print("")
    print("Rom 9")
    print("Det er 2 dører i rommet")
    print("Velg en dør")
    print("")
    asking = True
    while asking == True:
        valg = input("Dør A: Dør B: Gå tilbake C:->")

        if valg == "A":
            room7()
        elif valg == "B":
            room8()
        elif valg == "C":
            room13()
        else:
            print("Error",valg)


def room12(): #bare gjennom rom 2
    print("")
    print("Rom 12")
    print("Det er ingenting hær")
    print("Du går videre")
    room101()

def room13(): # havner hær etter å gå ut av rom 4
    print("")
    print("Rom 13")
    print("Det er 2 dører i rommet")
    asking = True
    while asking == True:
        valg = input("Gå inn døra A: Gå tilbake B:->")

        if valg == "A":
            asking = False
            room14()
        elif valg == "B":
            asking = False
            room12()
        else:
            print("Error",valg)
        
def room14():
    print("")
    print("Rom 14")
    print("Det er 2 dører i rommet")
    asking = True
    while asking == True:
        valg = input("Gå inn døra A: Gå tilbake B:->")

        if valg == "A":
            asking = False
            room9()
        elif valg == "B":
            asking = False
            room13()
        else:
            print("Error", valg)


def room101():
    print("")
    global Nøkkel
    print("Rom 101")
    print("Du fant siste dør!")
    print("Godt jobba")
    print("Den siste døra har 2 nøkkelhull")
    print("Fikk du tak i alle nøkklene?")
    print("")
    asking = True
    while asking == True:
        valg = input("Lås opp døra A: Gå tilbake B:->")

        if valg == "A":
            if Nøkkel >= 2:
                print("")
                print("Du setter begge nøkklene i døra og vrir om")
                print("Du trykker ned håndtaket og døra sklir opp")
                room00()
                
            elif Nøkkel <= 2:
                print("")
                print("Du mangler 1 nøkkel")
                print("Finn den!")
                print("")
                room3()

        elif valg == "B":
            asking = False
            room1()
        else:
            print("Error",valg)


def room00():
    print("Gratulerer, du fant veien ut!")


room0()





