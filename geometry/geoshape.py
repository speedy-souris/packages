#coding:utf-8
"""
    Geometric calculation module

> 4 computational functions on a perimeter :
        - square    -> square_perimeter(length)
        - circle    -> circle_perimeter(radius)
        - rectangle -> rectangle_perimeter(lenght, width)
        - triangle  -> triangle_perimeter(triangle_base, triangle_side1, triangle_side2)

> 4 computational functions on an area :
        - square    -> square_area(length)
        - circle    -> circle_area(radius, pi)
        - rectangle -> rectangle_perimeter(lenght, width)
        - triangle  -> triangle_area(triangle_base, triangle_side1, triangle_side2)

> 2 computational functions on a volume :
        - cube      -> cube_volume(length, pi)
        - sphere    -> sphere_volume(radius, pi)
"""

                    #----------
                    # Perimeter
                    #----------

pi = 3.14

# Square
def square_perimeter(length):
    return length * 4

# Circle
def circle_perimeter(radius):
    return 2 * pi * radius

# Rectangle
def rectangle_perimeter(lenght, width):
    return (lenght + width) * 2

# Triangle
def triangle_perimeter(triangle_base, triangle_side1, triangle_side2):
    return triangle_base + triangle_side1 + triangle_side2

                    #-----
                    # Area
                    #-----

# Square
def square_area(length):
    return length**2

# Cercle
def circle_area(radius):
    return  pi * radius**2

# Rectangle
def rectangle_area(length, width):
    return length * width

# Triangle
def triangle_area(triangle_base, triangle_side1, triangle_side2):
    s = triangle_perimeter(triangle_base, triangle_side1, triangle_side2)/2
    base = s - triangle_base
    side1 = s - triangle_side1
    side2 = s - triangle_side2
    t = s * base * side1 * side2
    return t**0.5

                    #-------
                    # Volume
                    #-------

# Cube
def cube_volume(length):
    return length**3

# Sphere
def sphere_volume(radius):
    return 4 * pi * radius**3 / 3

if __name__ == '__main__':
    print("Zone de test\n")
    print(f"Périmètre du carré : {square_perimeter(2)}\n")
    print("Périmètre du cercle : %.2f\n" % circle_perimeter(5))
    print(f"Périmètre du rectangle : {rectangle_perimeter(6, 2)}\n")
    print("Périmètre du triangle : %.2f\n" % triangle_perimeter(17, 24, 9))
    print(f"Aire du carré : {square_area(2)}\n")
    print("Aire du cercle : %.2f\n" % circle_area(5))
    print(f"Aire du rectangle : {rectangle_area(6, 2)}\n")
    print("Aire du triangle : %.2f\n" % triangle_area(17, 24, 9))
    print(f"Volume du cube : {cube_volume(2)}\n")
    print("Volume de la sphère : %.2f\n" % sphere_volume(5))
