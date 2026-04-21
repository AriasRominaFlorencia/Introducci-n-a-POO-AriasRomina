
import random
import time
puntos1=0
puntos2=0
puntos3=0
puntos4=0

dados=[1,2,3,4,5,6]

class Jugador:
    def __init__(self):
        return "     (•‿•)","    /|🎲|\\","     | |","    /   \\"

class Juego(Jugador):
    def __init__(self):
        self.jugador1=super().__init__()
        self.jugador2=super().__init__()
        self.jugador3=super().__init__()
        self.jugador4=super().__init__()

        print(f"{'TU PERSONAJE':<12}{'SISTEMA1':<12}{'SISTEMA2':<12}{'SISTEMA4':<12}")

        for i in range(len(self.jugador1)):
            print(f"{self.jugador1[i]:<12}{self.jugador2[i]:<12}{self.jugador3[i]:<12}{self.jugador4[i]:<12}")
    def Jugar(self):
        global puntos1,puntos2,puntos3,puntos4
        r=0
        while r!=4:
            print(f"\nRONDA {r+1}")
            print("\nEs tu turno")
            self.lanzar=input("Lanzar")
            if self.lanzar=="":
                self.punto1=random.choice(dados)
                print("\nSumas ",self.punto1," puntos")
                puntos1+=self.punto1
                print(f"Puntos: {puntos1}\n")
        
            print("Turno del jugador 2")
            print("Lanzando...")
            time.sleep(2)
            self.punto2=random.choice(dados)
            print(f"Jugador 2 suma {self.punto2} puntos")
            puntos2+=self.punto2
            print(f"Puntos: {puntos2}\n")

            print("Turno del jugador 3")
            print("Lanzando...")
            time.sleep(2)
            self.punto3=random.choice(dados)
            print(f"Jugador 3 suma {self.punto3} puntos")
            puntos3+=self.punto3
            print(f"Puntos: {puntos3}\n")

            print("Turno del jugador 4")
            print("Lanzando...")
            time.sleep(2)
            self.punto4=random.choice(dados)
            print(f"Jugador 4 suma {self.punto4} puntos")
            puntos4+=self.punto4
            print(f"Puntos: {puntos4}\n")

            print(f"{'TU PERSONAJE':<12}{'SISTEMA1':<12}{'SISTEMA2':<12}{'SISTEMA4':<12}")

            for i in range(len(self.jugador1)):
                print(f"{self.jugador1[i]:<12}{self.jugador2[i]:<12}{self.jugador3[i]:<12}{self.jugador4[i]:<12}")

            r+=1
        
        jugadores = [
        [puntos1, "Tu jugador"],
        [puntos2, "Jugador2"],
        [puntos3, "Jugador3"],
        [puntos4, "Jugador4"]
        ]

        jugadores.sort()
        jugadores.reverse()

        print("\nGANADORES:")
        for i in range(4):
            print(i+1, "-", jugadores[i][1], "Puntos:", jugadores[i][0])
        


juego=Juego()
juego.Jugar()