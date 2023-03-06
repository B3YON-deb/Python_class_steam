#Control bibliotecario: el bibliotecario lleva el control de prestar y devolucion libros
#Asignar, visualizar quien prestó, devolver el libro

#agregamos
from datetime import datetime

class Biblioteca:
    def __init__(self) -> None:
        pass
    
    def agregar(self, datos): 
        self.datos = datos
        self.id = int(input('Ingresa tu cédula: '))
        self.nombre = input('Ingresa tu nombre: ')
        self.datos[self.id] = self.nombre
        #print(self.datos)
                
    def editar (self):
        self.libro = input('Ingrese nombre de libro: ')
        date = datetime.now()
        self.fecha = date.strftime('%d %b %Y')
        self.hora = date.strftime("%H:%M:%S")
        diccionario_interno = {
            self.nombre: {
                'libro': self.libro,
                'fecha': self.fecha,
                'hora': self.hora,
            'estado': 'prestado'
            }
        }
        self.datos[self.id] = diccionario_interno
                
    def visualizar(self):
        print(self.datos)
        
        
   