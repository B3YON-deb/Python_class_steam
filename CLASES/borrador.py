# import datetime
# personas = {}


# def agregar_persona (
#     diccionario:dict
# )-> dict:
#     nombre = input("cual es el nombre de la persona ")
#     libro = input("cual es el libro que presto ")
#     fecha = datetime.datetime.now()
#     fecha_de_prestamo = input("cuando presto el libro: ")
#     diccionario_interno = {
#         "libro":libro,
#         "fecha": fecha_de_prestamo
#     }
#     print(diccionario_interno)
#     if diccionario.get(nombre) != None:
#         diccionario[nombre].append(diccionario_interno)
#     else:
#         diccionario[nombre] = [diccionario_interno]
#     print(diccionario)
    
# agregar_persona(personas)

# import datetime

# dicot = {
#     'andres': [{'nombre': 'andres', 'apellido': 'vidal'}]
#     }

# while True:
#     nombre = str(input("agrega un nombre: "))
#     apellido = input("agrega un apellido: ")

#     docta = {
#         "nombre":nombre,
#         "apellido": apellido 
#     }
#     if dicot.get(nombre) != None:
#         dicot[nombre].append(docta)
#     else:
#         dicot[nombre] = [docta]
#     print(dicot)





# diccionario = {"nombre":"Felipe"}
# diccionario["apellido"] = "gonzalez"
# temp = {"edad":23,
#         "sexo":"M",
#         "nombre":"gabriela",
#         "Profesion":"ing sistemas"}
# diccionario.update(temp)
# print(diccionario)

# diccionario["extra"] = temp
# diccionario["extra"].pop("sexo")
# diccionario["extra"]["Profesion"] = ["Profesor","ing","bailarin","modelo","batman"]

# diccionario["extra"]["Profesion"].append("astronauta")
# print(diccionario["extra"]["Profesion"])
# print(diccionario["extra"]["Profesion"])




intern_dict = {"andres":{
            "libro":{"Estado":"Prestado"},
            "Fecha >": "formatF",
            "Hora >": "4:00"}
            }



for i,x in intern_dict.items():
    for i,x in x.items():
        print(f"Libro > {i}")
        break
    for i,x in x.items():
        print(f"Estado > {x}")
        break
print(f"Fecha >", intern_dict["andres"]["Fecha >"])
print(f"Hora >", intern_dict["andres"]["Hora >"])
        


# print(f""" 
#       Usuario : Andres
#       Libro : {"\n".join("{} {}".format(a,s) for a,s in intern_dict.items())}
#       Estado : {intern_dict['andres']["libro"]["Estado"]}
#       Fecha : {intern_dict['andres']["Fecha >"]}
#       Hora : {intern_dict['andres']["Hora >"]}
#       """)
    



# dic = {}

# nombre = input("ingresa tu nombre: ")
# libro = input("ingresa tu libro: ")
# hora = datetime.datetime.now()
# formatt = hora.strftime("%d %b %Y %H: %M: %S")

# intern_dict = {
#     "nombre":nombre,
#     "libro":libro,
#     "hora": formatt
# }

# if dic.get(nombre) != None:
#     dic[nombre].append(intern_dict)
# else:
#     dic[nombre] = [intern_dict]
#     input("\n".join("{} {}".format(x,z) for x,z in intern_dict.items()))

#PREGUNTAS
# var1,var2 = main,main2



# diccionario = {
#     "nombre":"andres"}
# }
    
    


# main = list(range(50))
# print(main)