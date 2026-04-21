class Cuenta:
    def titular(self):
        self.nombre=input("Nombre del titular: ")
        self.cantidad=float(input("Cantidad a ingresar: "))
    
    def mostrar(self):
        print(f"Titular de la cuenta: {self.nombre}")
        print((f"Monto a ingresar: {self.cantidad}"))

class PlazoFijo(Cuenta):
    def interes(self):
        super().titular()
        self.interes=self.cantidad*6/100
    
    def mostrar(self):
        print("El plazo fijo tendrá una duracion de 30 días")
        print(f"El interes mensual es {self.interes}")

class CajaAhorro(PlazoFijo):
    def __init__(self):
        super().interes()
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Monto ingresado: {self.cantidad}")

cuenta=Cuenta()
cuenta.mostrar()

plazo=PlazoFijo()
plazo.interes()
plazo.mostrar()

caja=CajaAhorro()
caja.mostrar()
