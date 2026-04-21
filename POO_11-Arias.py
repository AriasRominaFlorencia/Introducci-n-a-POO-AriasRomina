
import random
vida1=3
vida2=3

monedas=["30","25","35","20"]
opcionesDef=["defenderse","esquivar","nada","nada","nada"]
atacar=["Bola de fuego","Tormenta de viento","Drenar vida"]

class Hechicero:
    def __init__(self):
        return "       /\\","      /  \\","     /____\\","      (• •)","      /|_|\\","     /_| |_\\","       / \\","      /   \\","     /_____\\","       | |","      /   \\","     /_____\\"

class Combate(Hechicero):
    def __init__(self):
        self.hechicero1=super().__init__()
        self.hechicero2=super().__init__()
        self.monedas1=int(random.choice(monedas))
        self.monedas2=int(random.choice(monedas))


        print(f"{'TU HECHICERO':<44}{'SISTEMA'}\n")
        for i in range(len(self.hechicero1)):
            print(f"{self.hechicero1[i]:<40}{self.hechicero2[i]}")
    
    def Ataque(self):
        global vida1,vida2

        if self.monedas1<2 and self.monedas1<2:
            print("\nSe quedaron sin monedas para seguir luchando")
            print("EMPATE\n")
            op=3
            return op
        else:

            print(f"{'TU HECHICERO':<44}{'SISTEMA'}\n")
            for i in range(len(self.hechicero1)):
                print(f"{self.hechicero1[i]:<40}{self.hechicero2[i]}")

            print("\nTUS MONEDAS: ",self.monedas1,"                     SUS MONEDAS: ",self.monedas2)
            print("TUS VIDAS: ",vida1, "                        SUS VIDAS: ",vida2)

            print("\nATAQUES:")
            print("1- Bola de fuego (-2 monedas)")
            print("2- Tormenta de viento (-5 monedas)")
            print("3- Drenar vida (-10 monedas, +1 vida)")

            op=int(input("Opción: "))
            if op==1:
                if self.monedas1>=2:
                    self.monedas1-=2
                    opcion=random.choice(opcionesDef)
                    if opcion=="defenderse":
                        print("\nNo le hiciste daño, se defendió\n")
                    if opcion=="esquivar":
                        print("\nNo le hciste daño, lo esquivó\n")
                    if opcion=="nada":
                        vida2-=1
                        print("\nLe quitaste 1 vida. A tu oponente le quedan ",vida2, " vidas\n")
                else:
                    print("\nNo tienes suficientes monedas\n")
            if op==2:
                if self.monedas1>=5:
                    self.monedas1-=5
                    opcion=random.choice(opcionesDef)
                    if opcion=="defenderse":
                        print("\nNo le hiciste daño, se defendió\n")
                    if opcion=="esquivar":
                        print("\nNo le hciste daño, lo esquivó\n")
                    if opcion=="nada":
                        vida2-=1
                        print("\nLe quitaste 1 vida. A tu oponente le quedan ",vida2, " vidas\n")
                else:
                    print("\nNo tienes suficientes monedas\n")
            if op==3:
                if self.monedas1>=10:
                    self.monedas1-=10
                    opcion=random.choice(opcionesDef)
                    if opcion=="defenderse":
                        print("\nNo le hiciste daño, se defendió\n")
                    if opcion=="esquivar":
                        print("\nNo le hciste daño, lo esquivó\n")
                    if opcion=="nada":
                        vida2-=1
                        vida1+=1
                        print("\nLe quitaste 1 vida. A tu oponente le quedan ",vida2, " vidas")
                        print("Regeneraste 1 vida tuya, tenes ",vida1," vidas\n")
                else:
                    print("\nNo tienes suficientes monedas\n")
        
            sistema=random.choice(atacar)
            if sistema=="Bola de fuego":
                if self.monedas2>=2:
                    self.monedas2-=2
                    defe=random.choice(opcionesDef)
                    if defe=="defenderse":
                        print("\nTe intento tirar una bola de fuego")
                        print("Te defendiste, no te quito vidas")
                    if defe=="esquivar":
                        print("\nTe intento tirar una bola de fuego")
                        print("Lo lograste esquivar, no te quito vidas")
                    if defe=="nada":
                        vida1-=1
                        print("\nTe alcanzó la Bola de fuego, te quito 1 vida. Te quedan",vida1," vidas")
                else:   
                    print("\nEl sistema intento atacar con una bola de fuego, pero se quedo sin monedas\n")
        
            if sistema=="Tormenta de viento":
                if self.monedas2>=5:
                    self.monedas2-=5
                    defe=random.choice(opcionesDef)
                    if defe=="defenderse":
                        print("\nTe intento tirar una tormenta de viento")
                        print("Te defendiste, no te quito vidas")
                    if defe=="esquivar":
                        print("\nTe intento tirar una tormenta de viento")
                        print("Lo lograste esquivar, no te quito vidas")
                    if defe=="nada":
                        vida1-=1
                        print("\nTe alcanzó la Tormenta de viento, te quito 1 vida. Te quedan",vida1," vidas\n")
                else:
                    print("\nEl sistema intento atacar con una tormenta de viento, pero se quedo sin monedas\n")
        
            if sistema=="Drenar vida":
                if self.monedas2>=10:
                    self.monedas2-=10
                    defe=random.choice(opcionesDef)
                    if defe=="defenderse":
                        print("\nTe intento drenar una vida")
                        print("Te defendiste, no te quito vidas\n")
                    if defe=="esquivar":
                        print("\nTe intento drenar una vida")
                        print("Lo lograste esquivar, no te quito vidas\n")
                    if defe=="nada":
                        vida1-=1
                        print("\nTe drenó 1 vida. Te quedan",vida1," vidas\n")
                else:
                    print("\nEl sistema intento drenarte una vida, pero se quedo sin monedas\n")
        
            print(f"{'TU HECHICERO':<44}{'SISTEMA'}\n")
            for i in range(len(self.hechicero1)):
                print(f"{self.hechicero1[i]:<40}{self.hechicero2[i]}")

            print("\nTUS MONEDAS: ",self.monedas1,"                     SUS MONEDAS: ",self.monedas2)
            print("TUS VIDAS: ",vida1, "                        SUS VIDAS: ",vida2)
        
    
    def Curarse(self):
        global vida1
        if self.monedas1>=15:
            self.monedas1-=15
            vida1+=1
            print("Regeneraste 1 vida")
            return
        else:
            print("No tienes suficientes monedas para curarte")

        



combate=Combate()
print("Opciones: ")
print("1- Atacar")
print("2- Curarse (-15 monedas, +1 vida)")
print("3- Terminar juego")
op=int(input("Opción: "))

while op!=3:
    if op==1:
        combate.Ataque()
    
    if op==2:
        combate.Curarse()
    
    if vida1==0:
        print("\nPERDISTE  💀")
        break
    
    if vida2==0:
        print("\nGANASTE  🏆")
        break

    if op==3:
        break
    
    print("Opciones: ")
    print("1- Atacar")
    print("2- Curarse (-15 monedas, +1 vida)")
    print("3- Terminar juego")
    op=int(input("Opción: "))
        