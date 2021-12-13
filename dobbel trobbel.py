import random
Rood = [1,2,3,4,5,6]
blauw = [1,2,3,4,5,6]
witte = [1,1,1,2,2,3]
positie = ['','1','2','3','4','5','6','7','8']
scorebladrood = ['-2','','','','','','','','','']
scorebladblauw = ['','','','','','','','','','-2']
witterij = []
def dice():
    dobbellijst = []
    for i in range(3):
        x = random.randint(0,(len(witte)-1))           
        dobbellijst.append(witte[x])
      
    print(dobbellijst)
    return j




dobbelstenen = dice()
def berekengetal(dobbelstenen):
    Rood = dobbelstenen[0]
    blauw = dobbelstenen[1]
    wit = dobbelstenen[2]
    and1 = (Rood + blauw + wit)
    and2 = (blauw + Rood - wit)
    and3 = (blauw + Rood)
    and4 = (max(dobbelstenen) - min(dobbelstenen))

    print(f'a {blauw} + {Rood} + {wit}  = {(Rood + blauw + wit)}')
    print(f'b {blauw} + {Rood} - {wit}  = {(blauw + Rood - wit)}')
    print(f'c {blauw} + {Rood} = {(blauw + Rood)}')
    print(f'd {max(dobbelstenen)} - {min(dobbelstenen)} = {(max(dobbelstenen) - min(dobbelstenen))} ')
    lijstje1 = [and1,and2,and3,and4 ]
    
def getalinvullen(positie,scorebladrood,scorebladblauw,witterij):

    Rood = dobbelstenen[0]
    blauw = dobbelstenen[1]
    wit = dobbelstenen[2]
    and1 = (Rood + blauw + wit)
    and2 = (blauw + Rood - wit)
    and3 = (blauw + Rood)
    and4 = (max(dobbelstenen) - min(dobbelstenen))
    print(scorebord)
    welke = input('welke optie kies je? ')
    positie = int(input('welke positie wil je het hebben? '))
    if welke =='c' or welke =='d':
        witterij.apend(and3 or and4)
while True:
    print(scorebord)


    

getalinvullen(positie,scorebladrood,scorebladblauw,witterij) 
dice()
berekengetal(dobbelstenen)


    

    


