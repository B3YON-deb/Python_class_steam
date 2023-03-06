import os
import datetime
from Modulo_error import error

def editar(
    dic: dict
)-> str:
    os.system("cls")
    x = True
    DEX = "_"
    while x == True:
        os.system("cls")
        print( f"-LISTA DE USUARIOS- > \n{DEX*11}\n"+"\n".join("{}\n{}".format(c,DEX*11) for c in dic))
        a:str = input("-ingresa el nombre del usuario que deseas editar- \n\t[Pulsa 0 para cancelar]\n\t  >")
        if a == "0":
            break

        while True:
            if a not in dic:
                os.system("cls")
                entrance : str = input("¡Usuario no se encuentra en sistema!\n   [pulsa enter para re-intentar]\npulsa '0' para regresar al menu inicial > ")
                if entrance == "0":
                    x = False
                    break
                else:   
                    os.system("cls")
                    break
            os.system("cls")
            while True:
                os.system("cls")
                try:
                    entrance = int(input("""
                                [1] Agregar [Libro]
                                    [2] Cambiar nombre de [Usuario]
                                        [3] Cambiar estado del [Libro]
                                            [0] Regresar al menu anterior > """))
                except:
                    os.system("cls")
                    input("     ¡Ingresa un valor valido!\n   [pulsa enter para re-intentar]\nPulsa '0' para regresar al menu inicial >")
                else:
                    break   
            if entrance == 0:
                    break
            if entrance == 1:
                on = True
                while on == True:
                    while True:
                        os.system("cls")
                        libro = input("Ingresa el libro que deseas agregar\n [Pulsa '0' para regresar al menu anterior]\n\t >")
                        if libro == "0":
                            on = False
                            break
                        validation = error(libro)
                        if validation == True and libro.isspace() == False:
                            pass
                        else:
                            os.system("cls")
                            input("  ¡Ingresa un valor valido!\n[Pulsa enter para re-intertar]")
                            break
                        fecha = datetime.datetime.now()
                        formatF= fecha.strftime("%d/%B/%Y")
                        hora = datetime.datetime.now() 
                        formatH = hora.strftime("%I: %M: %S: %p")
                        
                        intern_dict = {    
                        libro:{"Estado >":"Prestado"},
                        "Fecha >": formatF,
                        "Hora >": formatH
                        }
                        
                        dic[a].append(intern_dict)
                        print(f"USUARIO > {a}")
                        for key,value in dic.items():
                            for i in value:
                                print(f"{DEX*11}")
                                for n,m in i.items():
                                    print(f" {n}{m}" )
                        
                        select = input(f"\n¡Se agrego el libro [{libro}] al usuario [{a}]!\n{DEX*40}\n[Pulsa enter para volver a ingresar otro libro]\n [Pulsa '0' para volver al menu de seleccion] \n\t >  ")
                        if select == "0":
                            on = False
                            break
                        else:
                            pass
            if  entrance == 2:
                os.system("cls")
                while True:
                    main = input(f"Actualmente tu nombre de usuario es [{a}]\n  ¡Ingresa el nuevo nombre de usuario!\n [Pulsa '0' para volver al menu anterior] \n\t> ")
                    if main == "0":
                        break
                    else:
                        dic[main] = dic[a] 
                        del dic[a]
                        os.system("cls")
                        print(f"USUARIO > {main}")
                        for key,value in dic.items():
                            for i in value:
                                print(f"{DEX*8}")
                                for n,m in i.items():
                                    print(f" {n}{m}" )
                        print(f"{DEX*40}")
                        print(dic)
                        input(f"\nSe cambio usuario -> [{a}] \nPor usuario -> [{main}]\n{DEX*40}\n ¡No se afecto ningun dato en el proceso!\n[Pulsa enter para regresar al menu anterior]")
                        
                        break
            if entrance == 3:
                print(f"Usuario > {a}")
                for i,x in dic.items():
                    for i,x in x.items():
                        print(f"Libro > {i}")
                        break
                    for i,x in x.items():
                        print(f"Estado > {x}")
                print(f"Fecha >", dic[a]["Fecha >"])
                print(f"Hora >", dic[a]["Hora >"])
                    
                print(f"{DEX*40}")
                user = input("¡Ingresa el libro al cual deseas cambiar el estado! > ")             
                os.system("cls")
                estado = int(input("Ingresa [1] para Estado 'DEVUELTO'\n [2] para Estado 'PRESTADO' "))
                if estado == 1:
                    estado = "Devuelto"
                    dic[a][user]["Estado >"] = estado
                    input("")
                elif estado ==2:
                    estado = "Prestado"
                    dic[a][user]["Estado >"] = estado
        
if __name__ == "__main__":
    editar()
                
                
# intern_dict = {    
#             "Libro >":libro,
#             "Fecha >": formatF,
#             "Hora >": formatH,
#             "Estado >": "Prestado"
#             }


# def editar(
#     dic: dict
# )-> str:
#     g = True
#     os.system("cls")
#     while g == True:
#         print(" \n".join(" {} {} {} {}".format("usuario >",k,"| articulos >",v) for k,v in dic.items()))
#         a:str = input(" ingresa el nombre del usuario que deseas editar \n o pulsa 0 para cancelar >")
#         if a == "0":
#             break
#         while True:
#             if a not in dic:
#                 os.system("cls")
#                 entrance : str = input("usuario no se encuentra en sistema pulsa enter para re-intentar\n    o pulsa 0 para regresar al menu inicial ")
#                 if entrance == "0":
#                     g = False
#                     break
#                 else:
#                     pass
#                 os.system("cls")
#                 break
#             else:
#                 while True:
#                     b:str = input("ingresa el nuevo articulo: ")
#                     validation = error(b)
#                     if b.isspace() == True:
#                         os.system("cls")
#                         input(">para continuar debes ingresar un dato<\n    !pulsa enter para re-intentar¡")
#                     else:
#                         break
        
#                 if validation == True:
#                     os.system("cls")
#                     input(f"se a agregado el articulo {b} !exitosamente¡\n pulsa enter para continuar ") 
#                     os.system("cls")
#                     dic[a] = b
#                     g = False
#                     break
#                 else:
#                     k = input("no se encontro ese usuario en la base de datos, pulsa enter e intentalo de nuevo\n o ingresa 0 para cancelar ")
#                     if k == "0":
#                         g = False
#                         break
#                     else:
#                         pass