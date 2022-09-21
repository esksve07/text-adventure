
from operator import truediv

from random import randint
visited_keyroom = False

Gassmaske = 0
Kniv = 0
Tau = 0
Nøkkel = 0
Hammer = 1




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




def room1(): #start rom
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

def room2(): #trenger nøkkel for å senke broa
    global Nøkkel
    print("")
    print("Rom 2")
    print("Mellom deg og de neste dørene er de et stort svart hull")
    print("På andre siden kan du skimte en bro")
    print("Du ser et nøkkelhull på veggen")
    print("Du trenger en nøkkel")
    print("")
    asking = True
    while asking == True:
        valg = input("Bruk nøkkelen A: Gå tilbake B:->")

        if  valg == "A":
            asking = False
            if Nøkkel >= 1:
                print("Du fant nøkkelen")
                print("Godt jobba")
                print("Du setter nøkkelen i hullet og vrir om")
                print("Broen går ned")
                print("Du kan nå gå over")
                print("Velg en dør")
                asking2 = True
                while asking2 == True:
                    valg = input("Dør A: Dør B: Dør C:->")

                    if valg == "A":
                        asking2 = False
                        room3()
                    elif valg == "B":
                        asking2 = False
                        room5()
                    elif valg == "C":
                        asking2 = False
                        room7()

            elif Nøkkel <= 0:
                print("Kom tilbake når du har nøkkelen")
                room1()
        elif valg == "B":
            asking = False
            room1()
        else:
            print("Error",valg)
        

def room3():
    pass

def room4(): # nøkkelrom
    global Nøkkel, Hammer, visited_keyroom
    if visited_keyroom == True:
        room13()
    print("")
    print("Rom 4")
    print("Rommet har ingen annen vei ut enn tilbake")
    print("Du ser nøkkelen ligge i en glassboks mids i rommet")
    print("Du trenger en hammer")
    print("")
    asking = True
    while asking == True:
        valg = input("Ødelegg glasset A: Gå tilbake B:->")

        if valg == "A":
            asking = False
            if Hammer >= 1:
                print("Glasset gikk i tusen biter")
                print("Nøkkelen er fri")
                Nøkkel += 1
                visited_keyroom = True
                print("Du tar med deg nøkkelen og forlater rommet")
                room13()
                
            elif Hammer <= 0:
                print("Du mangler nøkkelen")
                print("Finn den!")
                room13()

        elif valg == "B":
            asking = False
            room13()
        else:
            print("Error",valg)


def room5(): #
    print("Rom 5")
    print("Velg en dør")
    asking = True
    while asking == True:
        valg = input("Dør A: Dør B: Dør C:->")

        if  valg == "A":
            asking = False
            room2()
        elif valg == "B":
            asking = False
            room5()
        elif valg == "C":
            asking = False
            room7()
        else:
            print("Error",valg)

def room6():
    pass

def room7():
    print("Rom 7")
    

def room8():
    pass

def room9(): # gjennom døra i rom 13
    pass

def room10():
    pass

def room11():
    print("Rom 11")

def room12(): #bare gjennom rom 2
    print("Rom 12")

def room13(): # havner hær etter å gå ut av rom 4
    print("Rom 13")
    print("Det er 2 dører i rommet")
    asking = True
    while asking == True:
        valg = input("Gå inn døra A: Gå tilbake:->")

        if valg == "A":
            asking = False
            room9
        elif valg == "B":
            asking = False
            room12

        

def room15():
    print("Rom 15")

def room101():
    print("Rom 101")

room0()





