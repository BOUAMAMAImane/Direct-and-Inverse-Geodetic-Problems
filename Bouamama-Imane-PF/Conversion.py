from math import *
def dmstorad(d, m, s):
    Degree=d+(m+s/60)/60
    Rad=Degree*pi/180
    return Rad


def radtodms(S):

    seconde = float(180 * S / pi * 3600)

    s = seconde % 60
    m = seconde // 60
    d = m // 60
    m = m % 60
    return (d,m,s)