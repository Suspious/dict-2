lijstjewat = []
lijstjehoe = []
aantal = 0
while True:
    Wat = input('wat wil je? ')
    if(Wat.lower()=="stop"):
        break;
    hoeveel = input('hoeveel wil je daarvan?  ')
    lijstjewat.append(Wat)
    lijstjehoe.append(hoeveel)
    aantal + 1
for i in range(len(lijstjewat)):
    print(f"{lijstjewat[i]} x {lijstjehoe[i]}")
    print('u heeft een totaal aantal van ',aantal)