#dobbel 3.0
import random
Rood = [1,2,3,4,5,6]
blauw = [1,2,3,4,5,6]
witte = [1,1,1,2,2,3]
positie = ['','1','2','3','4','5','6','7','8']
scorebladrood = ['-2','','','','','','','','','']
scorebladblauw = ['','','','','','','','','','-2']
scorebladwit = ['','','','']
witterij = []
scorebord = (f'''
        {positie}\n
        \x1b[0;37;41m{scorebladrood}\x1b[1;40m\n
        \x1b[0;37;44m{scorebladblauw}\x1b[1;40m\n
    
        ''')

dobbelijst = []
for x in range(3):
    j = random.choice(witte)
    dobbelijst.append(j)
dobbelstenen = dobbelijst
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
def vullen(and1,and2,and3,and4):
    global scorebladrood
    global scorebladblauw
    Welke = input(' a,b,c,d  welke wil je  hebben? ')
    waar = int(input('Waar wil je hem hebben? '))
    
    if Welke == 'a':
        scorebladrood 
    if Welke == 'b':
        scorebladrood.insert(waar,and2)
    if Welke == 'c':
        scorebladwit.append(and3)
    if Welke == 'd':
        scorebladwit.append(and4)
    print(scorebord)

while True:
    print(dobbelijst)
    calc1()
    vullen(and1,and2,and3,and4)
    break
print(scorebord)


    
    

    
