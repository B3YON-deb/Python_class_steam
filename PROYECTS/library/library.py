import os
from functions import ingresar
from functions import visualizar
from functions import eliminar
from functions import editar
datos = {}
def run():
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
            if menu == 1:
                os.system("cls")
                ingresar(datos)
            elif menu == 2:
                os.system("cls")
                eliminar(datos)
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
                                input("no hay datos para consultar \n>pulsa enter para continuar<")
                            else:
                                print(" \n".join(" usuario: {} \n datos: {} \n_______________ ".format(k,v) for k,v in datos.items()))
                                input(" \n>pulsa enter para continuar<")
                                break
                    except ValueError:
                        os.system("cls")
                        war =input("valor no valido, pulsa enter e intentalo de nuevo\n\to ingresa 0 para cancelar ")
                        if war == "0":
                            break
            elif menu == 4:
                os.system("cls")
                editar(datos)
            elif menu == 5:
                break
        except ValueError:
            os.system("cls")
            input("no has ingresado una opcion valida, pulsa enter para re-intentar")
if __name__ == "__main__":
    run()
            
            

