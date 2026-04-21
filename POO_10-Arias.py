import random

opciones=["acelerar","mantener","nitro"]
pos1=0
pos2=0
pos3=0
meta=46

class Auto:
    def __init__(self):
        return r"      ______",r"     /|_||_\`.__",r"    (   _    _ _\\",r"    =`-(_)--(_)-'"


class Carrera(Auto):
    def __init__(self):
        print(" " * meta + "🏁\n")
        self.auto1=super().__init__()
        self.auto2=super().__init__()
        self.auto3=super().__init__()


        print("\n    TU AUTO")
        for i in range(len(self.auto1)):
            print(self.auto1[i])
        
        for a in range(len(self.auto2)):
            print(self.auto2[a])
        
        for e in range(len(self.auto3)):
            print(self.auto3[e])
    
    def Acelerar(self):
        global pos1,pos2,pos3,op
        print(" " * meta + "🏁\n")
        pos1+=4
        print(" "*pos1+"TU AUTO")
        for q in range(len(self.auto1)):   
            print(" "*pos1,self.auto1[q])
        
        opcion1=random.choice(opciones)
        if opcion1=="acelerar":
            pos2+=4
            for linea in self.auto2:
                print(" "*pos2,linea)
        elif opcion1=="mantener":
            for linea in self.auto2:
                print(" "*pos2, linea)
        elif opcion1=="nitro":
            pos2+=8
            for linea in self.auto2:
                print(" "*pos2,linea)
        
        opcion2=random.choice(opciones)

        if opcion2=="acelerar":
            pos3+=4
            for linea1 in self.auto3:
                print(" "*pos3,linea1)
        elif opcion2=="mantener":
            for linea1 in self.auto3:
                print(" "*pos3,linea1)
        elif opcion2=="nitro":
            pos3+=8
            for linea1 in self.auto3:
                print(" "*pos3,linea1)
        
        if pos1 >= meta:
            print("🏁 ¡Ganaste!")
            op=4
            return op
        elif pos2 >= meta:
            print("🏁 Perdiste 😢")
            op=4
            return op
        elif pos3 >= meta:
            print("🏁 Perdiste 😢")
            op=4
            return op
    def Mantener(self):
        global pos1,pos2,pos3,op
        print(" " * meta + "🏁\n")
        print(" "*pos1+"TU AUTO")
        for q in range(len(self.auto1)):   
            print(" "*pos1,self.auto1[q])
        
        opcion1=random.choice(opciones)
        if opcion1=="acelerar":
            pos2+=4
            for linea in self.auto2:
                print(" "*pos2,linea)
        elif opcion1=="mantener":
            for linea in self.auto2:
                print(" "*pos2, linea)
        elif opcion1=="nitro":
            pos2+=8
            for linea in self.auto2:
                print(" "*pos2,linea)
        
        opcion2=random.choice(opciones)

        if opcion2=="acelerar":
            pos3+=4
            for linea1 in self.auto3:
                print(" "*pos3,linea1)
        elif opcion2=="mantener":
            for linea1 in self.auto3:
                print(" "*pos3,linea1)
        elif opcion2=="nitro":
            pos3+=8
            for linea1 in self.auto3:
                print(" "*pos3,linea1)

        if pos1 >= meta:
            print("🏁 ¡Ganaste!")
            op=4
            return op
        elif pos2 >= meta:
            print("🏁 Perdiste 😢")
            op=4
            return op
        elif pos3 >= meta:
            print("🏁 Perdiste 😢")
            op=4
            return op

    def Nitro(self):
        global pos1,pos2,pos3,op
        print(" " * meta + "🏁\n")
        pos1+=8
        print(" "*pos1+"TU AUTO")
        for q in range(len(self.auto1)):   
            print(" "*pos1,self.auto1[q])
        
        opcion1=random.choice(opciones)
        if opcion1=="acelerar":
            pos2+=4
            for linea in self.auto2:
                print(" "*pos2,linea)
        elif opcion1=="mantener":
            for linea in self.auto2:
                print(" "*pos2, linea)
        elif opcion1=="nitro":
            pos2+=8
            for linea in self.auto2:
                print(" "*pos2,linea)
        
        opcion2=random.choice(opciones)

        if opcion2=="acelerar":
            pos3+=4
            for linea1 in self.auto3:
                print(" "*pos3,linea1)
        elif opcion2=="mantener":
            for linea1 in self.auto3:
                print(" "*pos3,linea1)
        elif opcion2=="nitro":
            pos3+=8
            for linea1 in self.auto3:
                print(" "*pos3,linea1)
        
        if pos1 >= meta:
            print("🏁 ¡Ganaste!")
            op=4
            return op
        elif pos2 >= meta:
            print("🏁 Perdiste 😢")
            op=4
            return op
        elif pos3 >= meta:
            print("🏁 Perdiste 😢")
            op=4
            return op
        

        
carrera=Carrera()
print("¿Qué querés hacer?")
print("1. Acelerar")
print("2. Mantener velocidad")
print("3. Usar nitro")
op=int(input("Opcion: "))
while op!=4:
    if op==1:
        carrera.Acelerar()
        if op==4:
            break
    if op==2:
        carrera.Mantener()
        if op==4:
            break
    if op==3:
        carrera.Nitro()
        if op==4:
            break
    
    print("¿Qué querés hacer?")
    print("1. Acelerar")
    print("2. Mantener velocidad")
    print("3. Usar nitro")
    op=int(input("Opcion: "))
    
        
