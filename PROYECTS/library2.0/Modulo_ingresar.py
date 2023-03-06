import os
import re
import datetime
from Modulo_error import error

def ingresar(
    dic: dict
    
)-> str:
    """_summary_

    Args:
        dic (dict): _diccionario donde se almacenaran los datos_

    Returns:
        dict: _usuario y articulo ingresado en diccionario_
    """
    while True:
        while True:
            DEX = "_"
            os.system("cls")
            nombre = input("ingresa tu nombre: ")
            validation = error(nombre)
            if validation == True and nombre.isspace() == False:
                break
            else:
                os.system("cls")
                input("¡Ingresa un valor valido!\n(Solo letras y numeros)")
        while True:
            libro = input("ingresa tu libro: ")
            validation = error(libro)
            if validation == True and nombre.isspace() == False:
                break
            else:
                os.system("cls")
                input("¡Ingresa un valor valido!\n(Solo letras y numeros)")
        hora = datetime.datetime.now()
        formatH = hora.strftime("%I: %M: %S: %p")
        fecha = datetime.datetime.now()
        formatF = fecha.strftime("%d/%B/%Y")
    
    
        intern_dict = {
            libro:{"Estado >":"Prestado"},
            "Fecha >": formatF,
            "Hora >": formatH
            }
        
        if dic.get(nombre) != None:
            os.system("cls")
            input("¡Usuario ya se encuentra registrado¡\nIngrese a la opcion [4] Editar usuario (del menu principal) si desea actualizar datos.\nPulse enter para regresar al menu principal.")
            break       
        else:
            dic[nombre] = intern_dict
            os.system("cls")
            input(  f"¡Se agrego con exito! \nusuario> {nombre}\n{DEX*16}\n"+"\n".join(" {} {}".format(x,z) for x,z in intern_dict.items()))
            break
        
            
            
            
            
            
            
            
            
            
            
            
            
            #################3
            
            
            
            
            
#             import os
# import re
# import datetime
# from Modulo_error import error

# def ingresar(
#     dic: dict
    
# )-> str:
#     """_summary_

#     Args:
#         dic (dict): _diccionario donde se almacenaran los datos_

#     Returns:
#         dict: _usuario y articulo ingresado en diccionario_
#     """
#     while True:
#         while True:
#             DEX = "_"
#             os.system("cls")
#             nombre = input("ingresa tu nombre: ")
#             validation = error(nombre)
#             if validation == True and nombre.isspace() == False:
#                 break
#             else:
#                 os.system("cls")
#                 input("¡Ingresa un valor valido!\n(Solo letras y numeros)")
#         while True:
#             libro = input("ingresa tu libro: ")
#             validation = error(libro)
#             if validation == True and nombre.isspace() == False:
#                 break
#             else:
#                 os.system("cls")
#                 input("¡Ingresa un valor valido!\n(Solo letras y numeros)")
#         hora = datetime.datetime.now()
#         formatH = hora.strftime("%I: %M: %S: %p")
#         fecha = datetime.datetime.now()
#         formatF = fecha.strftime("%d/%B/%Y")
    
    
#         intern_dict = {    
#             "Libro >":libro,
#             "Fecha >": formatF,
#             "Hora >": formatH,
#             "Estado >": "Prestado"
#             }
        
#         if dic.get(nombre) != None:
#             os.system("cls")
#             input("¡Usuario ya se encuentra registrado¡\nIngrese a la opcion [4] Editar usuario (del menu principal) si desea actualizar datos.\nPulse enter para regresar al menu principal.")
#             break       
#         else:
#             dic[nombre] = [intern_dict]
#             os.system("cls")
#             input(  f"¡Se agrego con exito! \nusuario> {nombre}\n{DEX*16}\n"+"\n".join(" {} {}".format(x,z) for x,z in intern_dict.items()))
#             input(dic)
#             break
            