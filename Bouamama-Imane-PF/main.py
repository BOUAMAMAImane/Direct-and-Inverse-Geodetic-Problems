from math import *

def calcul_rayon_moyen (a,b) :
    Rm=(2*a+b)/3

    return Rm

def calcul_rayon_a (E):
    Ra= sqrt(E/(4*pi))

    return Ra

def calcul_rayon_v (a,b):
    Rv=(a*a*b)**(1/3)

    return Rv

def calcul_rayon_Gauss (a,b) :
    e = sqrt(a*a-b*b)/a
    phi = pi/4
    M = a*(1-e*e)/(1-e*e*(sin(phi)**2))**(3/2)
    N = a/sqrt(1-e*e*(sin(phi)**2))
    Rg= sqrt(M*N)

    return Rg


a=6378249.20
b=6356515.0
#a = 6378249.145
#b = 6356515.0
E = 4 * ((b * b) *pi* 1.00456)
#print(calcul_rayon_Gauss(a,b))
#print(calcul_rayon_moyen(a,b))
print(calcul_rayon_a(E))