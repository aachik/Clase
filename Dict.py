persona = {'nombre':'Abdul', 'edad': 21,'carrera': 'Itic',"vivo": True}

diccionario = {'hola': 'saludo generalente usado ',
                'morsa':'animal mamifero que es bigoton con cola'
               }

    
class Orden(Envio, Pedido):
            
    def __init__(self,nombre,icono):
        self.nombre = nombre
        self.icono = icono

      
        b = 0
        print("ejercicio de programacion ")
        
       

    def crearletra(self):
            nombre = 'nombre programa'
            global nombre
    def Pagar(self):
        print(nombre)


class Pedido(Orden):

    def __init__(self, a,b):
        self.a = a
        self.b = b


    def printNombre(self):
        print(nombre)

class Envio(Orden):

    def __init__(self):
        print("se creo el programa tres")

        self.crearletra()
        self.printNombre()
    
