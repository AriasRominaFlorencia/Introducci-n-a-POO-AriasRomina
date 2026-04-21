class Persona():
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.edad=int(input("Ingrese la edad: "))
        
    def mostrar(self):
        if self.edad>=18:
            print (f"La persona {self.nombre} con {self.edad} es mayor de edad")
        else:
            print (f"La persona {self.nombre} con {self.edad} es menor de edad")
            
persona1=Persona()
persona1.mostrar()