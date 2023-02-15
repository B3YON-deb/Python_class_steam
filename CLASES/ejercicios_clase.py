
# ejercicio 2 (5)
# Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.

# def worst (
#     p:str
# )-> dict:
#     p = p.split(" ")
#     dicto = {}
#     long = len(p)
#     for letra in p:
#         dicto[letra] = {
#             "longitud": [long]
#             }
#     print(dicto)
# worst("razer blade")
# #_________________________________________________________________________________




# ejercicio 1
# https://www.mclibre.org/consultar/python/ejercicios/ej-funciones-2.html
# Escriba un programa que permita crear dos listas de palabras y que, a continuación,0 
# elimine de la primera lista los nombres de la segunda lista.
# El programa debe preguntar por la cantidad de elementos en cada lista



# def operacion_listas(

# ):
    
#     numerito= int(input("Dijita el numero de palabras de la lista "))
#     lista = []
#     for i in range(numerito):
#         palabra=input(f"Dijita palabra {i+1} : ")
#         lista.append(palabra)
    
    
#     numerito2= int(input("Dijita el numero de palabras de la lista "))
#     lista2 = []
#     for j in range(numerito2):
#         palabra=input(f"Dijita palabra que deseas remove {j+1} : ")
#         lista2.append(palabra)
    
#     print(lista)
#     print(lista2)
    
#     for k in lista2:
#         if k in lista:
#             lista.remove(k)
    
#     print("lista final: ",lista)

# operacion_listas()

#_____________________________________________________________________________________________
#_____________________________________________________________________________________________

# numero = int(input("Dígame cuántas palabras tiene la lista: "))

# if numero < 1:
#     print("¡Imposible!")
# else:
#     lista = []
#     for i in range(numero):
#         print("Dígame la palabra", str(i + 1) + ": ", end="")
#         palabra = input()
#         lista += [palabra]
#     print("La lista creada es:", lista)

#     numero2 = int(input("Dígame cuántas palabras tiene la lista de palabras a eliminar: "))

#     if numero2 < 1:
#         print("¡Imposible!")
#     else:
#         eliminar = []
#         for i in range(numero2):
#             print("Dígame la palabra", str(i + 1) + ": ", end="")
#             palabra = input()
#             eliminar += [palabra]
#         print("La lista de palabras a eliminar es:", eliminar)

#         for i in eliminar:
#             for j in range(len(lista)-1, -1, -1):
#                 if lista[j] == i:
#                     del(lista[j])
#         print("La lista es ahora:", lista)