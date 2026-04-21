class Calculadora():
    def __init__(self):
        self.num1=int(input("Número 1: "))
        self.num2=int(input("Número 2: "))
    
    def suma(self):
        self.suma=(self.num1)+(self.num2)
    
    def resta(self):
        self.resta=(self.num1)-(self.num2)
        
    def multiplicacion(self):
        self.mult=(self.num1)*(self.num2)
        
    def division(self):
        self.div=(self.num1)/(self.num2)
        
    def mostrar(self):
        print(f"\nSuma: {self.suma}")
        print(f"Resta: {self.resta}")
        print(f"Multiplicación: {self.mult}")
        print(f"División: {self.div}")
        

numeros=Calculadora()
numeros.suma()
numeros.resta()
numeros.multiplicacion()
numeros.division()
numeros.mostrar()