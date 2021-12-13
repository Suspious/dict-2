#dobbel trobbel 2.0
import random
Rood = [1,2,3,4,5,6]
blauw = [1,2,3,4,5,6]
witte = [1,1,1,2,2,3]
positie = ['','1','2','3','4','5','6','7','8']
scorebladrood = ['-2','','','','','','','','','']
scorebladblauw = ['','','','','','','','','','-2']
class scorebord(scorebladblauw,scorebladrood,Rood,blauw,witte,positie):
    def __init__(self,scorebladblauw,scorebladrood,Rood,blauw,witte,positie):
        scorebladblauw = scorebladblauw
        scorebladrood = scorebladrood
        Rood = Rood
        blauw = blauw
        witte = witte
        positie = positie
             
    def scorebord(self):
        
        print(scorebord)
    def dice(self):
        dobbellijst = []
        for i in range(3):
            x = random.randint(0,(len(self.witte)-1))           
            dobbellijst.append(self.witte[x])
      
            return dobbellijst
    def gaatje(dobbelstenen):
        Rood = dobbelstenen[0]
        blauw = dobbelstenen[1]
        wit = dobbelstenen[2]
        and1 = (Rood + blauw + wit)
        and2 = (blauw + Rood - wit)
        and3 = (blauw + Rood)
        and4 = (max(dobbelstenen) - min(dobbelstenen))
        antwoorden =  [and1,and2,and3,and4]
        return antwoorden
    def opties(self):
        reken1 = (f'a {self.blauw} + {self.Rood} + {self.wit}  = {(self.Rood + self.blauw + self.wit)}')
        reken2 =(f'b {self.blauw} + {self.Rood} - {self.wit}  = {(self.blauw + self.Rood - self.wit)}')
        reken3 = (f'c {self.blauw} + {self.Rood} = {(self.blauw + self.Rood)}')
        reken4 = (f'd {max(self.dobbelstenen)} - {min(self.dobbelstenen)} = {(max(self.dobbelstenen) - min(self.dobbelstenen))} ')
play = scorebord()
play.scorebord()