import random

vida=100
ataque=["Golpe","Ataque fuerte","Proyectil","Ataque a la base"]
recursos=["3 madera","2 piedra","1 hierro"]
decisiones=["No hacer nada","Defender"]

class Torre:
    def __init__(self):
        return "  ███  ", " █████ "," █ █ █ "," █   █ "," █   █ "," █   █ ","███████"

class Combate(Torre):
    def __init__(self):
        self.torre=super().__init__()
        
        print("TORRE")
        for i in range(len(self.torre)):
            print(self.torre[i])
        
        print("\n|  RECURSOS DE LA TORRE  |")
        for l in range(len(recursos)):
            print(f"| {recursos[l]:^22} |")
        print("|------------------------|\n")
        

        
    def Ataques(self):
        global vida
        while vida>0:
            print("Tu torre esta siendo atacada. ¿Qué quieres hacer?")
            print("1- Reparar")
            print("2- Ver estado de la torre")
            print("3- Nada")
            op=int(input("Opción: "))
            if op==1:
                if vida==100:
                    print("\nTu torre esta al 100%. No necesita reparaciones\n")
                else:
                    print("TORRE")
                    for i in range(len(self.torre)):
                        print(self.torre[i])
                
                    print("\nESTADO DE LA TORRE: ",vida,"%")
    
                    print("\n| RECURSOS DE LA TORRE   |")
                    for l in range(len(recursos)):
                        print(f"| {recursos[l]:^22} |")
                    print("|------------------------|\n")

                    print("\n- Volver")
                    reparar=input("Solo puedes elegir el conjunto: ").lower()
                    if reparar=="madera":
                        recursos.remove("3 madera")
                        vida+=20
                    if reparar=="piedra":
                        recursos.remove("2 piedra")
                        vida+=25
                    if reparar=="hierro":
                        recursos.remove("1 hierro")
                        vida+=35
            if op==2:
                print("TORRE")
                for i in range(len(self.torre)):
                    print(self.torre[i])
                    
                print("\nESTADO DE LA TORRE: ",vida,"%")
        
                print("\n| RECURSOS DE LA TORRE  |")
                for l in range(len(recursos)):
                    print(f"| {recursos[l]:^22} |")
                print("|------------------------|\n")
                
            self.ataque=random.choice(ataque)
            if self.ataque=="Golpe":
                self.defen=random.choice(decisiones)
                if self.defen=="No hacer nada":
                    print("\n¡La torre sufió un golpe!\n")
                    vida-=30
                if self.defen=="Defender":
                    print("\n¡Quisieron golpear la torre! La lograste defender\n")
        
            elif self.ataque=="Ataque fuerte":
                self.defen=random.choice(decisiones)
                if self.defen=="No hacer nada":
                    print("\n¡La torre sufió un ataque fuerte!\n")
                    vida-=30
                if self.defen=="Defender":
                    print("\n¡Quisieron atacar la torre! La lograste defender\n")
            
            elif self.torre=="Proyectil":
                self.defen=random.choice(decisiones)
                if self.defen=="No hacer nada":
                    print("\n¡La torre sufió de un proyectil!\n")
                    vida-=50
                if self.defen=="Defender":
                    print("\n¡Quisieron lanzar un proyectil a la torre! La lograste defender\n")
        
            elif self.ataque=="Ataque a la base":
                self.defen=random.choice(decisiones)
                if self.defen=="No hacer nada":
                    print("\n¡La torre sufió un ataque a la base!\n")
                    vida-=40
                if self.defen=="Defender":
                    print("\n¡Quisieron atacar la base de latorre! La lograste defender\n")

        print("\n¡TU TORRE FUE DESTRUIDA!")


                        

            

combate=Combate()
combate.Ataques()