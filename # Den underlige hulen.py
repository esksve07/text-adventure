from random import randint

Liv = 150
Sverd = 0
Skjold = 0
Banan = 1
Bananskall = 0

navn=input

print("Du er ute på tur i skogen en regnfull dag")
print("Etter mye vandring finner du en underlig hule")

print("Hva gjør du","?")
valg=input("A: Gå inn i hulen, B: Gå videre rundt i skogen")

if valg == "A":
    print("Du går inn i hulen for å utforske dens hemmeligheter")
    Skjold+=1
    print("Du finner et stort skjold")

if valg == "B":
    print("DU gikk videre rundt i skogen")
    print("Inne i skogen er det et stor og dypt hull")
    print("Du ser de ikke")
    print("Du snubbler i en stein og faller ned")
    Liv-=150
    print("Du døde, rip")

print("Du går lenger inn i hulen")
print("Stemmningen er mørk og dyster")
print("Ingenting annet en stein og stillhet")
print("Du skimter at lenger inn i hulen er det en bakke")

print("Du begynner å tvile på om du burde fortsette")
print("Hva skal du gjøre","?")
valg=input("A:Gå ut av hulen, B:Fortsett innover")

if valg == "A":
    print("Du drar")
    print("På veien ut hører du brøl fra inne i hulen")
    print("Du blir redd og løper så fort du kan")
    print("Så typisk som det er, snubler du i en stein og blir liggende")
    print("Du våkner øyeblikk senere av lyden av rasende steiner")
    print("Huleinnganger raser","!")
    print("Du kommer deg på beina og løper så fort du kan")
    print("du snubbler ikke denne ganger, men blir truffet av en stein den aller siste meteren")
    Liv-=75
    print("Du brekker begge beina og er nå avhengig av rullestol")
    print("Men du lever")
    print("Men du undres resten av livet på hva brølet var")

if valg == "B":
    print("Du fortsetter inn i hulen")
    print("Du innser at bakken er alt for bratt til å gå ned")