import re
import os
# def error(
#     text:str
#     )-> bool :
#     """_summary_

#     Args:
#         text (str): _parametro que captura variable a comparar con validation_

#     Returns:
#         bool: _True o False_
#     """
#     validation = "^[A-Za-z0-9 ]+$"
#     return bool(re.search(validation,text))

def error(
    text:str
    )-> bool :
    """_summary_

    Args:
        text (str): _parametro que captura variable a comparar con validation_

    Returns:
        bool: _True o False_
    """
    validation = "^[A-Za-z0-9 ]+$"
    main = bool(re.search(validation,text))
    os.system("cls")
    if main == True:
        return True
    else:
        return False
            
        
    
    
    # while True:
    #     while True:
    #         os.system("cls")
    #         nombre = input("ingresa tu nombre: ")
    #         validation = error(nombre)
    #         if validation == True:
    #             pass
    #         else:
    #             os.system("cls")
    #             input("¡ingresa un valor valido!\n(Solo letras y numeros)")
    #             break