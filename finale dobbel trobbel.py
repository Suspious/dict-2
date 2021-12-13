import random 
#dit is de basis AKA Stap 1

rood =  ['-2','','','','','','','','']
blauw = ['','','','','','','','','-2']
wit = []


#ik ga nu het score bord maken aka de frontend van deze code
Scorebord = (f'''
         0    1   2   3   4   5   6   7   8
       \x1b[0;37;41m{rood}\x1b[1;40m\n
       \x1b[0;37;44m{blauw}\x1b[1;40m\n
              {wit}
''')
#hier ben ik verder gegaan met de code voor het rollen van de dobbelstenen
def gooi_dobbelstenen():
    dice = []
    blauwenrood = random.sample(range(1, 6), 2)
    witte = [1,1,1,2,2,3]
    dice.append(blauwenrood[0])
    dice.append(blauwenrood[1])
    getalwit = random.choice(witte)
    dice.append(getalwit)
    return dice
dice = gooi_dobbelstenen()
blauwgetal = max(dice)
roodgetal = min(dice)
witgetal = dice[2]
#nu gaan we iets doen met die 3 getallen die we hier hebben gemaakt

andwoord1 = roodgetal + blauwgetal + witgetal
andwoord2 = roodgetal + blauwgetal - witgetal
andwoord3 = roodgetal + blauwgetal 
andwoord4 = max(dice) + min(dice)

Opties = (f'''
A {blauwgetal} + {roodgetal} = {andwoord1}
B {roodgetal} + {blauwgetal} - {witgetal} = {andwoord2}
C {roodgetal} + {blauwgetal} = {andwoord3}
D {max(dice)} + {min(dice)}  = {andwoord4}
 ''')

#nu ik mensen een keuze heb laten maken gaan we het invullen in de scorebord
def vragen(rood,blauw,wit):
    optie = input('Welke optie kies je?  ').lower()
    plek = int(input(' op welke positie?  '))
         
    if optie == 'a':
        rood[plek] = andwoord1
    if optie == 'b':
        blauw[plek] = andwoord2
    if optie == 'c':
        wit.append(str(andwoord3))
    if optie == 'd':
        wit.append(str(andwoord4))
#nu ik de twee belangerijkste heb gedaan ga ik andere werkzaamheden doen
def  eindberekening():
    itrood = [s for s in rood if s.isdigit()]
    itblauw = [s for s in blauw if s.isdigit()]
    itwit  =[s for s in wit if s.digit()]
    for i in range(8):
        x = itrood[i] * itblauw[i]
        answer = x - itwit
    print(answer)
def uitvoering():
    print(f'''
{Scorebord}\n

{dice}
''')
uitvoering()
print(Opties)
vragen(rood,blauw,wit)
print(Scorebord)