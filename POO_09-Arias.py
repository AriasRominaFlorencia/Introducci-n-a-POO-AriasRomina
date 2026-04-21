import random

monedasCofre=[10,20,5,6,8,15]
cofres=["monedas","araña"]
cerrado=["si","no"]

class Personaje:
    def __init__(self):
        return "   O   ","  /|\  ","   |   ","  / \  "

class Cueva(Personaje):
    def __init__(self):
        self.monedas=0
        print("\nTU PERSONAJE")
        explorador=super().__init__()
        for i in range(len(explorador)):
            print(explorador[i])
    
    def cobreAbierto(self):
        global monedasCofre
        print("\nTU PERSONAJE")
        explorador=super().__init__()
        for i in range(len(explorador)):
            print(" "*3+explorador[i])
        print("      |")
        print("      |")
        print("Cofre Abierto")
        print("      |")
        print("      |")
        moned=random.choice(monedasCofre)
        print(f"Contiene {moned} monedas")
        print("\n 1- Recolectar monedas")
        print(" 2- Seguir camino")
        op=int(input("Que quiere hacer: "))
        while op!=2:
            if op==1:
                self.monedas+=moned
                print("\n| MONEDAS RECOLECTADAS |")
                print(f"|{self.monedas:^22}|")
                print("|----------------------|\n")
                return
    
    
    def cofreCerrado(self):
        print("\nTU PERSONAJE")
        explorador=super().__init__()
        for i in range(len(explorador)):
            print(" "*3+explorador[i])
        print("      |")
        print("      |")
        print("Cofre cerrado")
        print("      |")
        print("      |")
        print(" 1- Abrir Cofre")
        print(" 2- Seguir camino")
        op=int(input("Opción: "))
        while op!=2:
            if op==1:
                sePuede=random.choice(cerrado)
                if sePuede=="si":
                    opcion=random.choice(cofres)
                    if opcion=="monedas":
                        self.cobreAbierto() 
                        return    
                    if opcion=="araña":
                        self.monedas-=3
                        if self.monedas<0:
                            self.monedas=0
                        
                        print("\n|------------------------------------------------------|")
                        print(f"| Te picó una araña, por medicinas te quedan {self.monedas} monedas |")
                        print("|------------------------------------------------------|\n")
                elif sePuede=="no":
                    print("\n|-------------------|")
                    print("| No se puede abrir |")
                    print("|-------------------|\n")
                    return
                return

exploracion=Cueva()
print("Opciones: ")
print(" 1- Empezar a explorar ")
print(" 2- No explorar ")
op=int(input("Opción: "))

while op!=2:
    if op==1:
        random.choice([exploracion.cofreCerrado(),exploracion.cobreAbierto()])
    print("Opciones: ")
    print(" 1- Seguir explorando ")
    print(" 2- Dejar de explorar ")
    op=int(input("Opción: "))   