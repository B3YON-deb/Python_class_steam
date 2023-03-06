import os
import re
#________________________________________________________________________________ validacion de errores
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
    return bool(re.search(validation,text)) 
#________________________________________________________________________________
def userin (
    main: str,
    dicto: dict
)-> str:
    if main in dicto:
        return False
        
    else:
        return True
    

#________________________________________________________________________________


def ingresar(
    dic: dict
    
)-> str:
    """_summary_

    Args:
        dic (dict): _diccionario donde se almacenaran los datos_

    Returns:
        str: _usuario y articulo ingresado en diccionario_
    """
    x=True
    while x == True:
        y = True
        while True:
            os.system("cls")
            a= input("ingrese el nombre del usuario \no ingresa 0 para cancelar : ")
            validation = error(a)
            if a.isspace() == True:
                os.system("cls")
                input(">para continuar debes ingresar un dato<\n    !pulsa enter para re-intentar¡")
            else:
                break
        if a == "0":
            break
        if validation == True:
            while True:
                while True:
                    os.system("cls")
                    b= input("ingresa el articulo\no ingresa 0 para cancelar : ")
                    os.system("cls")
                    validation = error(b)
                    if b.isspace() == True:
                        os.system("cls")
                        input(">para continuar debes ingresar un dato<\n    !pulsa enter para re-intentar¡")
                    else:
                        break
                if b == "0":
                    x = False
                    break
                if validation == True:
                    dic[a] = b
                    os.system("cls")
                    input(f"\n\t|usuario: {a}\n\t|articulo: {b} \n  ¡se a creado exitosamente¡ \n __________________________ \n >pulsa enter para continuar< ")
                    x = False
                    break
                else: input(">ingresa un valor valido< \n!pulsa enter para re-intentar¡")
                os.system("cls")
        else:
            os.system("cls")
            input(">ingresa un valor valido< \n!pulsa enter para re-intentar¡")
            
        

                
        # else:
        #     os.system("cls")
        #     input("ingresa un valor valido ")
        #     os.system("cls")
            
            
            
            
            
#___________________________________________________________________________________
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
        a=input("ingrese el usuario que desea eliminar\n o ingresa 0 para cancelar ")
        if a == "0":
            break
        if a not in dic:
            os.system("cls")
            k = input("no se encontro ese usuario en la base de datos, pulsa enter e intentalo de nuevo\n o ingresa 0 para cancelar ") 
            if k == "0":
                break
        else: 
            os.system("cls")
            dic.pop(a)
            input(f"|se elimino usuario {a}|\ny todos sus articulos relacionados \n\n<pulsa enter para continual>")
            break
            

#___________________________________________________________________________________
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
        a = input("|*ingrese el usuario que desea visualizar*|\no pulse 0 para volver a menu anterior > ")
        if a == "0":
            break
        if a not in dic:
            os.system("cls")
            y = input("usuario no se encuentra en sistema, pulsa enter para re-intentar")
            if y == "0":
                break
        else:
            print(f"los articulos de >{a}< son:\n |{dic[a]} \n")
            input("pulsa enter para continuar")
            break

#___________________________________________________________________________________
def editar(
    dic: dict
)-> str:
    g = True
    os.system("cls")
    while g == True:
        print(" \n".join(" {} {} {} {}".format("usuario >",k,"| articulos >",v) for k,v in dic.items()))
        a:str = input(" ingresa el nombre del usuario que deseas editar \n o pulsa 0 para cancelar >")
        if a == "0":
            break
        while True:
            if a not in dic:
                os.system("cls")
                entrance : str = input("usuario no se encuentra en sistema pulsa enter para re-intentar\n    o pulsa 0 para regresar al menu inicial ")
                if entrance == "0":
                    g = False
                    break
                else:
                    pass
                os.system("cls")
                break
            else:
                while True:
                    b:str = input("ingresa el nuevo articulo: ")
                    validation = error(b)
                    if b.isspace() == True:
                        os.system("cls")
                        input(">para continuar debes ingresar un dato<\n    !pulsa enter para re-intentar¡")
                    else:
                        break
        
                if validation == True:
                    os.system("cls")
                    input(f"se a agregado el articulo {b} !exitosamente¡\n pulsa enter para continuar ") 
                    os.system("cls")
                    dic[a] = b
                    g = False
                    break
                else:
                    k = input("no se encontro ese usuario en la base de datos, pulsa enter e intentalo de nuevo\n o ingresa 0 para cancelar ")
                    if k == "0":
                        g = False
                        break
                    else:
                        pass
                
                