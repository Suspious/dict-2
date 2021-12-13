# dit is een eind opdracht van dobbel trobbel
import random
# Een rode en blauwe dobbelsteen met nummers 1 t/m 6
blauw_nummers = [1,2,3,4,5,6]
rood_nummers = [1,2,3,4,5,6]
# Een witte dobbelsteen met de nummers: 1,1,1,2,2,3
wit_nummers = [1,1,1,2,2,3]
#Een score blad met 2 rijen van ieder 10 vakjes (rood en blauw) en 1 rij met 5 vakjes (wit)
rood = ['-2','','','','','','','','','','','']
blauw = ['','','','','','','','','','','','','-2']
wit = []

#ik ga nu het score bord maken aka de frontend van deze code
def scorebord(rood,blauw,wit):
    Scorebord = ('''
         0    1   2   3   4   5   6   7   8
       \x1b[0;37;41m{0}\x1b[1;40m\n
       \x1b[0;37;44m{1}\x1b[1;40m\n
              {2}
''').format(rood,blauw,wit)
    print(Scorebord)
#Iedere ronde worden alle 3 dobbelstenen gerold.
def dobbelstenen_gooien(blauw_nummers,wit_nummers,rood_nummers):
    ronde = 1
    dobbelstenen = []
    while ronde >= 1:
        print('ik gooi nu de stenen')
        dobbelstenen.clear()
        blauwdobbel = random.choice(blauw_nummers)
        rooddobbel = random.choice(rood_nummers)
        witdobbel = random.choice(wit_nummers)
        dobbelstenen.append(blauwdobbel)
        dobbelstenen.append(rooddobbel)
        dobbelstenen.append(witdobbel)
        ronde = ronde - 1
        return dobbelstenen
stenen = dobbelstenen_gooien(blauw_nummers,wit_nummers,rood_nummers)
#Uit de waarden van de dobbelstenen kunnen verschillende getallen worden berekend.

def berekeningen(stenen):   
    rood_getal = stenen[0]
    blauw_getal = stenen[1]
    wit_getal = stenen[2]
    andwoord1 = rood_getal + blauw_getal + wit_getal
    andwoord2 = rood_getal + blauw_getal - wit_getal
    andwoord3 = rood_getal + blauw_getal 
    andwoord4 = max(stenen) + min(stenen)

    Opties = (f'''
    
    A {blauw_getal} + {rood_getal}+ {wit_getal} = {andwoord1}
    B {rood_getal} + {blauw_getal} - {wit_getal} = {andwoord2}
    C {rood_getal} + {blauw_getal} = {andwoord3}
    D {max(stenen)} + {min(stenen)}  = {andwoord4}
    ''')
    print(Opties)
    antwoorden_lijst = [andwoord1,andwoord2,andwoord3,andwoord4]
    return antwoorden_lijst
#De speler moet één berekend getal kiezen en invullen op het scoreblad als dat mogelijk is.
while len(wit) <= 4:
    scorebord(rood,blauw,wit)
    stenen = dobbelstenen_gooien(blauw_nummers,wit_nummers,rood_nummers)
    
    antwoorden = berekeningen(stenen)
    print(stenen)
# hier stel ik de vragen en wat ze doen dus de gaten vullen
#de eindscore
eindscorebl = 0
eindscorew = 0 
eindscore =  0 
    keuzes = input('a,b,c,d ')
    positie = int(input('Op welke positie wil je het hebben? '))
    if keuzes == 'a':
        rood[positie] = antwoorden[0]
        eindscorebl = antwoorden + eindscorebl
    if keuzes == 'b':
        blauw[positie] = antwoorden[1]
        eindscorere= antwoorden + eindscorere

    if keuzes == 'c':
        wit.append(antwoorden[2])
        eindscorew = antwoorden + eindscorew

    if keuzes == 'd':
        wit.append(antwoorden[3])
        eindscorew = antwoorden + eindscorew
print(f'je eindscore is {(eindscorew*eindscore*eindscorebl)}')





#
#
