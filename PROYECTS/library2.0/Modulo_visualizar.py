import os
import re
import datetime

def visualizar (
    dic: dict
)-> str:
    """_summary_

    Args:
        dic (dict): _diccionario del cual se va a visualizar los datos_

    Returns:
        none
    """
    os.system("cls")
    while True:
        os.system("cls")
        a = input("¡Ingrese el usuario que desea visualizar¡\n [pulse 0 para volver a menu anterior]\n\t> ")
        if a == "0":
            break
        if a not in dic:
            os.system("cls")
            y = input("¡Usuario no se encuentra en sistema!\n   [pulsa enter para re-intentar]")
            if y == "0":
                break
        else:
            print(f"los articulos de >{a}< son:\n |{dic[a]} \n")
            input("[Pulsa enter para continuar]")
            break