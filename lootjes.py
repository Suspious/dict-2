import random
lijstje_met_namen = []

while True:
     
    naam = input('wat is je naam ')
    lijstje_met_namen.append(naam)
   
    if len(lijstje_met_namen) > 2:
        nogmeer = input('nog meer? ') == 'nee'
        if nogmeer:
            getalletje = random.randint(0 ,len(lijstje_met_namen))
            for i in range(len(lijstje_met_namen)):
                nummer1 = lijstje_met_namen[i]
                nummer2 = lijstje_met_namen[getalletje]
                print('hey {} jij hebt {} '.format(nummer1,nummer2)) 
    if naam in lijstje_met_namen:
        print('deze naam is al in gebruik')        
