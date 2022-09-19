if Nøkkel >= 1:
        print("Velg en dør")
        valg = input("Dør A: Dør B: Dør C:->")

        if valg == "A":
            room1()
        if valg == "B":
            room5()
        if valg == "C":
            room4()

    elif Nøkkel <= 0:
       room1()