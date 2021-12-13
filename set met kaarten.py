import random
lijstnummers = [1,2,3,4,5,6,7,8,9,10]
soortenkaarten = ['schoppen','klaver','harte','ruiten']
special = ['joker','koning','boer','vrouw']
kaartje = []
for i in soortenkaarten:
    for j in lijstnummers:
        kaart = str(i) + ' ' + str(j)
        kaartje.append(kaart)
        for p in special:
            kaarstspecial = str(i) + '' + str(p)
            kaartje.append(kaarstspecial)
for k in range(7):
    x = random.choice(kaartje)
    print(x)
print(kaartje)
    