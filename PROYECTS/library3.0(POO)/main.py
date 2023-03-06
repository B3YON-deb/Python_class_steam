from objetos import Biblioteca
datos ={}
x = Biblioteca()

while True:
    menu = int(input('''
                    Qué deseas realizar?:
                1. Agregar nuevo usuario
                2. Editar usuario
                3. Visualizar usuario
                4. Eliminar usuario
                5. Finalizar 
                '''))
    match menu:
        case 1:
            x.agregar(datos)
        case 2:
            x.editar()
        case 3:
            x.visualizar()
    