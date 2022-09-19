
from operator import truediv
from random import randint

Gassmaske = 0
Kniv = 0
Tau = 0
Nøkkel = 0
Hammer = 0




def room0():
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
    print("Room 2")
    print("Mellom deg og de neste dørene er de et stort svart hull")
    print("På andre siden kan du skimte en bro")
    print("Du ser et nøkkelhull på veggen")
    print("Du trenger en nøkkel")
    asking = True
    while asking == True:
        valg = input("Bruk nøkkel A: Gå tilbake B:->")

        if  valg == "A":
            asking = False
            if Nøkkel >= 1:
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
                room1()
        elif valg == "B":
            asking = False
            room1()
        else:
            print("Error",valg)
        

def room3():
    pass

def room4(): # nøkkelrom
    global Nøkkel, Hammer
    print("Room 4")
    print("Rommet har ingen annen vei ut enn tilbake")
    print("Du ser nøkkelen ligge i en glassboks mids i rommet")
    print("Du trenger en hammer")
    asking = True
    while asking == True:
        valg = input("Ødelegg glasset A: Gå tilbake B:->")

        if valg == "A":
            asking = False
            if Hammer >= 1:
                print("Glasset gikk i tusen biter")
                print("Nøkkelen er fri")
                Nøkkel += 1
                
            elif Hammer <= 0:
                print("Du mangler nøkkelen")
                room13

        elif valg == "B":
            asking = False
            room13
        else:
            print("Error",valg)


def room5():
    print("Room 5")
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
    print("Room 7")
    

def room8():
    pass

def room9():
    pass

def room10():
    pass

def room11():
    pass

def room12(): #bare gjennom rom 2
    pass

def room13(): # havner hær etter å gå ut av rom 4
    print("Room 13")

def room15():
    pass

def room101():
    pass

room0()





