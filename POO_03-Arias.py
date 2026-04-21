class Triangulo():
    def __init__(self):
        self.lado1=int(input("Lado 1: "))
        self.lado2=int(input("Lado 2: "))
        self.lado3=int(input("Lado 3: "))
    
    def tamañoMayor(self):
        
        if self.lado1==self.lado2==self.lado3:
            print("Es un triangulo equilatero")
            print("Todos sus lados valen lo mismo")
        elif self.lado1==self.lado2 or self.lado1==self.lado3 or self.lado2==self.lado3:
            print("Es un triangulo isoseles")
        else: print("Es un triangulo rectangulo")
            
        
        if self.lado1>self.lado2 and self.lado1>self.lado3:
            print(f"El lado mayor es el lado 1 con {self.lado1} ")
        elif self.lado2>self.lado1 and self.lado2>self.lado3:
            print(f"El lado mayor es el lado 2 con {self.lado2} ")
        elif self.lado3>self.lado1 and self.lado3>self.lado2:
            print(f"El lado mayor es el lado 3 con {self.lado3} ")
            
        
triangulo1=Triangulo()
triangulo1.tamañoMayor()