contactos=[]

class Persona():
    def __init__(self):
        self.nombre=input("Nombre: ")
        self.telefono=int(input("Teléfono: "))
        self.email=input("Email: ")
        

class Agenda(Persona):
    def __init__(self):
        pass 
    def Agregar(self):
        super().__init__()  # pide datos
        contactos.append({
            "Nombre": self.nombre,
            "Teléfono": self.telefono,
            "Email": self.email
        })

    def Lista(self):
        if len(contactos)!=0:
            print(f"\nLISTA DE CONTACTOS: ")
            for i in range(len(contactos)):
                print(f"\nContacto {i+1}: ")
                print(f"-Nombre: {contactos[i]['Nombre']}")
                print(f"-Teléfono: {contactos[i]['Teléfono']}")
                print(f"-Email: {contactos[i]['Email']}")
        else:
            print("No hay ningun contacto cargado")
            
    def Buscar(self):
        if len(contactos)!=0:
            self.buscar=input("Ingrese el nombre de la persona: ")
            for l in range(len(contactos)):
                if contactos[l]['Nombre']==self.buscar:
                    print(f"\nNombre: {contactos[l]['Nombre']}")
                    print(f"Teléfono: {contactos[l]['Teléfono']}")
                    print(f"Email: {contactos[l]['Email']}")

        else:
            print("No hay ningun contacto cargado")
    
    def Editar(self):
        global contactos
        if len(contactos)!=0:
            self.editar=int(input("Ingrese el contacto que desea editar: "))-1
            while self.editar>len(contactos):
                self.editar=int(input("Ingrese un contacto válido: "))-1
        
            super().__init__()
            contactos[self.editar]["Nombre"] = self.nombre
            contactos[self.editar]["Teléfono"] = self.telefono
            contactos[self.editar]["Email"] = self.email
        else:
            print("No hay ningun contacto cargado")




contacto1=Agenda()

print("\nMENÚ:")
print("1- Añadir contacto")
print("2- Lista de contactos")
print("3- Buscar contactos")
print("4- Editar contacto")
print("5- Cerrar agenda")
op=int(input("Ingrese la opcion que desea: "))
while op!=5:
    if op==1:
        contacto1.Agregar()
        
    if op==2:
        contacto1.Lista()
        
    if op==3:
        contacto1.Buscar()
    if op==4:
        contacto1.Editar()
    
    print("MENÚ:")
    print("1- Añadir contacto")
    print("2- Lista de contactos")
    print("3- Buscar contactos")
    print("4- Editar contacto")
    print("5- Cerrar agenda")

    op=int(input("Ingrese la opcion que desea: "))
    
