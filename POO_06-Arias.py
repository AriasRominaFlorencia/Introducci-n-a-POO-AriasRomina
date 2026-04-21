
class Cliente:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
    
    def depositar(self, monto):
        self.cantidad+=monto
    
    def extraer(self,monto):
        self.cantidad-=monto
    
    def mostrar(self):
        print(f"Dinero en la cuenta {self.cantidad}")

class Banco(Cliente):
    def __init__(self):
        super().__init__("Banco", 0)

        print("Cliente1 ")
        self.cliente1 = Cliente("Ana", 100)
        print("Nombre: Ana")
        print("\nCliente2 ")
        self.cliente2 = Cliente("Luis", 200)
        print("Nombre: Luis")
        print("\nCliente3 ")
        self.cliente3 = Cliente("Sofía", 300)
        print("Nombre: Sofía")

    def operar(self):

        print("\nCliente1 ")
        self.cliente1.depositar(50)
        print(" - Depositó $50 ")
        self.cliente1.extraer(20)
        print(" - Extrajo $20 ")
        self.cliente1.mostrar()

        print("\nCliente2 ")
        self.cliente2.depositar(70)
        print(" - Depositó $70 ")
        self.cliente2.extraer(50)
        print(" - Extrajo $50 ")
        self.cliente2.mostrar()

        print("\nCliente3 ")
        self.cliente3.depositar(30)
        print(" - Depositó $30 ")
        self.cliente3.extraer(10)
        print(" - Extrajo $10 ")
        self.cliente3.mostrar()

    def depositoTotal(self):
        total = (
            self.cliente1.cantidad +
            self.cliente2.cantidad +
            self.cliente3.cantidad
        )
        print("\nTotal en el banco:", total)

banco=Banco()
banco.operar()
banco.depositoTotal()