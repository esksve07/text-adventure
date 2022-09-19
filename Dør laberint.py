from random import randint

#1-5-105-33-12-100

def room0():
    print("Velkommen")
    print("Du er nå låst inne og fanget")
    print("Finn veien ut, lykke til")
    valg = input("Start:")

    if valg == "Start":
        room1()



def room1():
    print("Velg en dør")
    valg = input("Dør A: Dør B: Dør C:->")

    if valg == "A":
        room2()
    if valg == "B":
        room5()
    if valg == "C":
        room101()

def room2():
    print("Room 2")
    print("Velg en dør")
    valg = input("Dør A: Dør B: Dør C:->")

    if valg == "A":
        room1()
    if valg == "B"
        room5()
    if valg == "C"
        room101()