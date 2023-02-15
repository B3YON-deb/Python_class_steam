# import functions todo functions
# from functions import area_rectangulo especifico
# from functions import * absolutamente todo


#parametros por defecto siempre al final
#_______________________________________

# def funciones_ejemplo(a,b,c="andres"):
#     #logica
#     suma = a+b
#     #retorno
#     return print(suma,c)
# funciones_ejemplo(1,2)


#_______________________________________
# def funciones_ejemplo(a,b,c=5):
#     #logica
#     d = int(input("digita un numero : "))
#     suma = a+b+d
#     #retorno
#     return suma
    
# print(funciones_ejemplo(2,3))
#_______________________________________
# lista = []
# def agregar (
#     alummnos:list
# )-> list:
    
#     estudiante = input("ingrese estudiante: ")
#     alummnos.append(estudiante)
#     print(alummnos)

# def eliminar (
#     alum:list
# )-> list:
#     a = str(input("ingrese el estudiante que desea eliminar: "))
#     alum.remove(a)
#     print(f"se ha eliminado {a}")
    
# def visualizar(
#     alum:list
# )-> list:
#     a = str(input("ingrese el estudiante que desea visualizar: "))
#     b = alum.index(a)
#     print(alum[b])
    
    
    
# agregar(lista)
# eliminar(lista)
# agregar(lista)
# visualizar(lista)
#_______________________________________
# import math
# def area_rectangulo (
#     x:float,
#     y:float
# ) -> float:
#     """
#     funcion que calcula el area de un rectangulo

#     Args:
#         x (float): base de mi rectangulo
#         y (float): altura de mi rectangulo

#     Returns:
#         area (float): es el area de mi rectangulo
#     """
#     area = x*y
#     return area


# base:float = float(input("ingresa la base: "))
# altura:float = float(input("ingresa la altura: "))
# area = area_rectangulo(base,altura)
# area = print(f"el area de tu rectangulo es {area}")

# #__________________________________________________________________________________
# def distancia_dos_puntos(
#     x_1:float,
#     x_2:float,
#     y_1:float,
#     y_2:float
# ) -> float:
#     """_summary_

#     Args:
#         x_1 (float): _valor 1_
#         x_2 (float): _valor 2_
#         y_1 (float): _valor 3_
#         y_2 (float): _valor 4_

#     Returns:
#         float: _distancia entre dos puntos _
#     """
#     x = math.pow(x_2 - x_1,2)
#     y = math.pow(y_2 - y_1,2)
#     d = math.sqrt(x+y)
#     return d
# abc = distancia_dos_puntos(2,3,4,5,)
# print(abc)

