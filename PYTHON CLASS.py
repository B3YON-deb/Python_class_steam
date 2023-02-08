def area_rectangulo (
    x:float,
    y:float
) -> float:
    """
    funcion que calcula el area de un rectangulo

    Args:
        x (float): base de mi rectangulo
        y (float): altura de mi rectangulo

    Returns:
        area (float): es el area de mi rectangulo
    """
    area = x*y
    return area


base:float = float(input("ingresa la base: "))
altura:float = float(input("ingresa la altura: "))
area = area_rectangulo(base,altura)
area = print(f"el area de tu rectangulo es {area}")