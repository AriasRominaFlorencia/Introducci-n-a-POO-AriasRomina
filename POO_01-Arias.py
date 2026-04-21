class Alumno():
    def __init__(self):
        self.nombre=input("Ingrese el nombre del alumno: ")
        self.nota=int(input("Ingrese la nota del mismo: "))
        while self.nota<0 or self.nota>10:
            self.nota=int(input("Ingrese la nota del mismo: "))
    
    def mostrar(self):
        if self.nota>=7:
            print(f"El alumno aprobo con {self.nota}")
        else:
            print(f"El alumno reprobo con {self.nota}")
            
alumno1=Alumno()
alumno1.mostrar()
