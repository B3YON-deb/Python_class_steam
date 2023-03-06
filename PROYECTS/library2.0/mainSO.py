import os
from Modulo_ingresar import ingresar
from Modulo_visualizar import visualizar
from Modulo_eliminar import eliminar
from Modulo_editar import editar
def run():
    datos = {}
    DEX = "_"
    while True:
        os.system("cls")
        while True:
            os.system("cls")
            try:
                menu = int(input("""
                                >sistema de registro de usuaios SDDU<
                                
                                [1] ingresar usuario
                                [2] eliminar usuario
                                [3] visualizar usuario
                                [4] editar usuario
                                [5] cerrar
                                
                                ingresa una opcion: 
                                
                                """))
            except ValueError:
                os.system("cls")
                input("¡No has ingresado una opcion valida!\n   [Pulsa enter para re-intentar]")
            else:
                break
                
        if menu == 1:
            os.system("cls")
            ingresar(datos)
        elif menu == 2:
            os.system("cls")
            while True:
                os.system("cls")
                try:
                    options = int(input("""
                                [1] eliminar usuario especifico
                                    [2] eliminar todos los usuarios
                                        [0] para cancelar > """))
                    
                    if options == 0:
                        break
                    elif options == 1:
                        if  datos:
                            eliminar(datos)
                        else:
                            os.system("cls")
                            input(" No hay usuarios registrados en sistema\n[Pulsa enter para volver al menu anterior]")
                        
                    elif options == 2:
                        if  datos:
                            datos.clear()
                            os.system("cls")
                            input("¡Se han eliminado todos los usuarios exitosamente!\n   [Pulsa enter para regresar al menu principal]")
                        else:
                            os.system("cls")
                            input(" No hay usuarios registrados en sistema\n[Pulsa enter para volver al menu anterior]")
                        
                except ValueError:
                    os.system("cls")
                    input("¡No has ingresado una opcion valida!\n   [Pulsa enter para re-intentar]")
        elif menu == 3:
            os.system("cls")
            while True:
                try:
                    os.system("cls")
                    options = int(input("""
                        [1] para usuario especifico
                            [2] para visualizar todos los usuarios :
                                [0] para cancelar > """))
                    if options == 0:
                        break
                    if options == 1:
                        os.system("cls")
                        visualizar(datos)
                    elif options == 2:
                        os.system("cls")
                        if len(datos) == 0:
                            input("No hay datos para consultar \n[pulsa enter para continuar]")
                        else:
                            print(" \n".join(" usuario: {} \n datos: {} \n_______________ ".format(k,v) for k,v in datos.items()))
                            input(" \n[Pulsa enter para continuar]")
                            break
                except ValueError:
                    os.system("cls")
                    war =input("     ¡Ingresa un valor valido!\n   [pulsa enter para re-intentar]\npulsa '0' para regresar al menu inicial >")
                    if war == "0":
                        break
        elif menu == 4:
            os.system("cls")
            editar(datos)
        elif menu == 5:
            break
        else:
            os.system("cls")
            input("¡No has ingresado una opcion valida!\n   [Pulsa enter para re-intentar]")
if __name__ == "__main__":
    run()