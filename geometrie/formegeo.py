#coding:utf-8
"""
    Module de calcul géométrique

> 4 fonctions de calcul sur un périmètre :
        - carré     -> perimetre_carre(longueur)
        - cercle    -> perimetre_cercle(rayon)
        - rectangle -> perimetre_rectangle(longueur, largeur)
        - triangle  -> perimetre_triangle(base, cote1, cote2)

> 4 fonctions de calcul sur une aire :
        - carré     -> aire_carre(longueur)
        - cercle    -> aire_cercle(rayon)
        - rectangle -> aire_rectangle(longueur, largeur)
        - triangle  -> aire_triangle(base, cote1, cote2)

> 2 fonctions de calcul sur un volume :
        - cube      -> volume_cube(longueur)
        - sphère    -> aire_triangle(base, cote1, cote2)
"""

                    #----------
                    # Périmètre
                    #----------

pi = 3.14

# Carré
def perimetre_carre(longueur):
    return longueur * 4

# Cercle
def perimetre_cercle(rayon):
    return 2 * pi * rayon

# Rectangle
def perimetre_rectangle(longueur, largeur):
    return (longueur + largeur) * 2

# Triangle
def perimetre_triangle(base, cote1, cote2) :
    return base + cote1 + cote2

                    #-----
                    # Aire
                    #-----

# Carré
def aire_carre(longueur):
    return longueur**2

# Cercle
def aire_cercle(rayon):
    return  pi * rayon**2

# Rectangle
def aire_rectangle(longueur, largeur):
    return longueur * largeur

# Triangle
def aire_triangle(base, cote1, cote2):
    s = perimetre_triangle(base, cote1, cote2) / 2
    part = s - base
    part1 = s - cote1
    part2 = s - cote2
    t = s * part * part1 * part2
    return t**0.5

                    #-------
                    # Volume
                    #-------

# Cube
def volume_cube(longueur):
    return longueur**3

# Sphère
def volume_sphere(rayon):
    return 4 * pi * rayon**3 / 3

if __name__ == '__main__':
    print("\nZone de test\n")
    print(f"Périmètre du carré : {perimetre_carre(2)}\n")
    print("Périmètre du cercle : %.2f\n" % perimetre_cercle(5))
    print(f"Périmètre du rectangle : {perimetre_rectangle(6, 2)}\n")
    print("Périmètre du triangle : %.2f\n" % perimetre_triangle(17, 24, 9))
    print(f"Aire du carré : {aire_carre(2)}\n")
    print("Aire du cercle : %.2f\n" % aire_cercle(5))
    print(f"Aire du rectangle : {aire_rectangle(6, 2)}\n")
    print("Aire du triangle : %.2f\n" % aire_triangle(17, 24, 9))
    print(f"Volume du cube : {volume_cube(2)}\n")
    print("Volume de la sphère : %.2f\n" % volume_sphere(5))
