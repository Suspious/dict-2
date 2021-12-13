from os import error
import random 
#dit is de basis AKA Stap 1

rood = ['-2','','','','','','','','']
blauw = ['','','','','','','','','-2']
wit = []
itrood = [s for s in rood if s.isdigit()]

#ik ga nu het score bord maken aka de frontend van deze code
def scorebord(rood,blauw,wit):
    Scorebord = ('''
         0    1   2   3   4   5   6   7   8
       \x1b[0;37;41m{0}\x1b[1;40m\n
       \x1b[0;37;44m{1}\x1b[1;40m\n
              {2}
''').format(rood,blauw,wit)
    print(Scorebord)
#hier ben ik verder gegaan met de code voor het rollen van de dobbelstenen

dice = []
def dobbbelstenen():
    global dice
    dice.clear()
    while len(dice) < 3:
        
        blauwenrood = random.sample(range(1, 6), 2)
        witte = [1,1,1,2,2,3]
        dice.append(blauwenrood[0])
        dice.append(blauwenrood[1])
        getalwit = random.choice(witte)
        dice.append(getalwit)
dobbbelstenen()
   
listandtwoorden = []

def opties(dice):
    global listandtwoorden
    listandtwoorden.clear()
    blauwgetal = max(dice)
    roodgetal = min(dice)
    witgetal = dice[2]
    #nu gaan we iets doen met die 3 getallen die we hier hebben gemaakt

    andwoord1 = roodgetal + blauwgetal + witgetal
    andwoord2 = roodgetal + blauwgetal - witgetal
    andwoord3 = roodgetal + blauwgetal 
    andwoord4 = max(dice) + min(dice)
    listandtwoorden = [andwoord1,andwoord2,andwoord3,andwoord4]
    Opties = (f'''
    A {blauwgetal} + {roodgetal} + {witgetal} = {andwoord1}
    B {roodgetal} + {blauwgetal} - {witgetal} = {andwoord2}
    C {roodgetal} + {blauwgetal} = {andwoord3}
    D {max(dice)} + {min(dice)}  = {andwoord4}
    ''')
    print(Opties)
    
    return listandtwoorden



#nu ik mensen een keuze heb laten maken gaan we het invullen in de scorebord
scorebord(rood,blauw,wit)
optie = opties(dice)

antwoord1 = optie[0]
antwoord2 = optie[1]
antwoord3 = optie[2]
antwoord4 = optie[3]
print(dice)

while len(wit) < 4:  
    keuze = input('Welke optie kies je?  ').lower()
    if keuze=='a' or keuze == 'b':
        plek = int(input(' op welke positie?  '))
        if keuze == 'a':
   
            rood[plek] = antwoord1
            scorebord(rood,blauw,wit)
            opties(dice)
            print(dice)
        
            dobbbelstenen()
            
        if keuze == 'b':

            blauw[plek] = antwoord2
            scorebord(rood,blauw,wit)
            antwoord2 = optie[1]
            opties(dice)
            print(dice)


            dobbbelstenen()
    if keuze == 'c':

            wit.append(antwoord3)
            scorebord(rood,blauw,wit)
            opties(dice) 


            print(dice)

            dobbbelstenen()

    if keuze == 'd':
       
            wit.append(antwoord4)
            scorebord(rood,blauw,wit)
            opties(dice) 

            print(dice)


       
            dobbbelstenen()

    


else:
    print('je hebt verloren helaas je eindscore is')
#nu ik de twee belangerijkste heb gedaan ga ik andere werkzaamheden doen

