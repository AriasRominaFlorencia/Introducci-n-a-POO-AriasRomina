import random

escenarios=["Bosque","Desierto","Castillo abandonado","Cueva","Aldea"]
objetos=["Mapa","Brújula","Daga","Botas","Piedra","Rama seca","Hierbas raras","Frasco vacío"]

class Aventurero:
    def __init__(self):
        return "      /\\",r"     /__\\",r"    (•_•)",r"    /| |\\",r"     | |",r"    /   \\",r"   /_____\\",r"     | |",r"    /   \\"

class Aventura(Aventurero):
    def __init__(self):
        self.aventurero=super().__init__()
    
    def escenario(self):
        self.objetosRecolectados=[]

        print("TU AVENTURERO\n")
        for l in range(len(self.aventurero)):
            print(self.aventurero[l])

        print("Empezar a explorar? ")
        print("1- Si")
        print("2- No")
        print("3- Consultar inventario")

        op=int(input("Opción: "))
        while op!=2:
            if op==1:
                print("TU AVENTURERO\n")
                for l in range(len(self.aventurero)):
                    print(self.aventurero[l])
                escena=random.choice(escenarios)
                print("\nTe encuentras en: ",escena)
                opcion=input("Quieres explorar? (si-no): ").lower()
                while opcion!="no" and opcion!="si":
                    print("\nEsa opcion no se encuentra en nuestro menú")
                    opcion=input("Quieres explorar? (si-no): \n").lower()
        
                if opcion=="si":
                    objeto=random.choice(objetos)
                    print("\n¡Encontraste un ",objeto, "!")
                    recolectar=input("Lo quieres recolectar? (si-no): ").lower()
                    while recolectar!="no" and recolectar!="si":
                        print("\nEsa opcion no se encuentra en nuestro menú")
                        recolectar=input("Quieres explorar? (si-no): \n").lower()
            
                    if recolectar=="si":
                        self.objetosRecolectados.append(objeto)
            
                    if recolectar=="no":
                        pass

                    seguir=input(f"Quieres seguir explorando {escena}? (si-no): ").lower()
                    while seguir!="no":
                        objeto=random.choice(objetos)
                        print("\n¡Encontraste un ",objeto, "!")
                        recolectar=input("Lo quieres recolectar? (si-no): ").lower()
                        while recolectar!="no" and recolectar!="si":
                            print("\nEsa opcion no se encuentra en nuestro menú")
                            recolectar=input("Quieres explorar? (si-no): \n").lower()
            
                        if recolectar=="si":
                            self.objetosRecolectados.append(objeto)
            
                        if recolectar=="no":
                            pass

                        seguir=input(f"Quieres seguir explorando {escena}? (si-no): ").lower()
        
                if opcion=="no":
                    pass
            
            if op==3:
                print("\nINVENTARIO: ")
                for i in range(len(self.objetosRecolectados)):
                    print(f"- {self.objetosRecolectados[i]}")

            print("\nSeguir explorando? ")
            print("1- Si")
            print("2- No")
            print("3- Consultar inventario")
            op=int(input("Opción: "))

aventura=Aventura()
aventura.escenario()
