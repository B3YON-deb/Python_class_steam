import os
import re
import datetime

def eliminar(
    dic: dict
) -> str:
    """_summary_

    Args:
        a (str): _datos ingresados por usuario_
        dic (dict): _diccionario del cual se va eliminar dato_

    Returns:
        str: _usuario eliminado_
    """
    while True:
        os.system("cls")
        a=input("ingrese el usuario que desea eliminar\no ingresa 0 para regresar al menu anterior >")
        if a == "0":
            break
        if a not in dic:
            os.system("cls")
            k = input("no se encontro ese usuario en la base de datos, pulsa enter e intentalo de nuevo\n o ingresa 0 para regresar al menu anterior ") 
            if k == "0":
                break
        else: 
            os.system("cls")
            dic.pop(a)
            input(f"|se elimino usuario {a}|\ny todos sus articulos relacionados \n\n<pulsa enter para continual>")
            break