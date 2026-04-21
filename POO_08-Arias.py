import random 

class Personaje:
    def __init__(self):
        return "   O   ","  /|\  ","   |   ","  / \  "

class Combate(Personaje):
    def __init__(self):
        personaje1=super().__init__()
        personaje2=super().__init__()
        for i in range(len(personaje1)):
            print(f"{personaje1[i]}                    {personaje2[i]}")
        c1=("<3"*5).center(17)
        c2=("<3"*5).center(19)
        print("\nTU PERSONAJE               SISTEMA\n")
        print(f"|   TUS   VIDAS   |          |  VIDAS   SISTEMA  |")
        print(f"|-----------------|          |-------------------|")
        print(f"|{c1}|          |{c2}|")
        print(f"|-----------------|          |-------------------|")
    
    def ataquesPers(self,v1,v2):
        if v1!=0 and v2!=0:
            print("ATAQUES")
            print(" 1- Golpear (1)")
            print(" 2- Apuñalar (2)")
            print(" 3- Derribar (1)")
            op=int(input("Opcion de ataque: "))
            if op==1:
                v1-=1
                print(f"Golpeaste al sistema \n")
                print(f"Le quitaste 1 vida\n")
            if op==2:
                v1-=2
                print(f"Apuñalaste al sistema \n")
                print(f"Le quitaste 2 vida\n")
            if op==3:
                v1-=1
                print(f"Derribaste al sistema \n")
                print(f"Le quitaste 1 vida\n")
            personaje1=super().__init__()
            personaje2=super().__init__()
            for i in range(len(personaje1)):
                print(f"{personaje1[i]}                    {personaje2[i]}")
            
            c1=("<3"*v2).center(17)
            c2=("<3"*v1).center(19)
            print("\nTU PERSONAJE               SISTEMA\n")
            print(f"|   TUS   VIDAS   |          |  VIDAS   SISTEMA  |")
            print(f"|-----------------|          |-------------------|")
            print(f"|{c1}|          |{c2}|")
            print(f"|-----------------|          |-------------------|")
        
            return v1
        else:
            pass

    def ataqueSist(self,v1,v2):
        if v1!=0 and v2!=0:
            self.ataque=random.randint(1,3)
            if self.ataque==1:
                v2-=1
                print(f"El sistema te golpeó \n")
                print(f"El sistema te quitó 1 VIDAS\n")
            if self.ataque==2:
                v2-=2
                print(f"El sistema te apuñaló \n")
                print(f"El sistema te quitó 2 VIDAS\n")
            if self.ataque==3:
                v2-=1
                print(f"El sistema te derribó \n")
                print(f"El sistema te quitó 1 VIDAS\n")
            personaje1=super().__init__()
            personaje2=super().__init__()
            for i in range(len(personaje1)):
                print(f"{personaje1[i]}                    {personaje2[i]}")
            c1=("<3"*v2).center(17)
            c2=("<3"*v1).center(19)
            print("\nTU PERSONAJE               SISTEMA\n")
            print(f"|   TUS   VIDAS   |          |  VIDAS   SISTEMA  |")
            print(f"|-----------------|          |-------------------|")
            print(f"|{c1}|          |{c2}|")
            print(f"|-----------------|          |-------------------|")
            return v2
        else:
            pass
        

combate=Combate()
vida1=5
vida2=5
vida1=combate.ataquesPers(vida1,vida2)
vida2=combate.ataqueSist(vida1,vida2)
while vida1!=0 and vida2!=0:
    vida1=combate.ataquesPers(vida1,vida2)
    vida2=combate.ataqueSist(vida1,vida2)

print("GAME OVER")
