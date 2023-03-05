from math import *
import Conversion
import main
from main import calcul_rayon_Gauss as Rg
import mpmath as mp
def probleme_inverse (phi1d,phi1m,phi1s, phi2d,phi2m,phi2s,lambda1d,lambda1m,lambda1s,lambda2d,lambda2m,lambda2s) :

    phi1 = Conversion.dmstorad(phi1d, phi1m, phi1s)
    phi2 = Conversion.dmstorad(phi2d, phi2m, phi2s)
    lambda1 = Conversion.dmstorad(lambda1d, lambda1m, lambda1s)
    lambda2 = Conversion.dmstorad(lambda2d, lambda2m, lambda2s)
    delta_lambda=lambda1-lambda2
    #DETERMINATION DE SIGMA12
    #sigma12=acos(sin(phi1)*sin(phi2)+cos(phi1)*cos(phi2)*cos(delta_lambda))*(180/pi)
    sigma12 = acos((sin(phi1) * sin(phi2) + cos(phi1) * cos(phi2) * cos(delta_lambda)))
    dis_ang_metre = sigma12 *Rg(6378249.20,6356515.0)
    print(dis_ang_metre)
    #DETRMINATION DE A12
    cot1= (tan(phi2)*cos(phi1)/sin(delta_lambda)) - (sin(phi1)*mp.cot(delta_lambda))
    A12=mp.acot(cot1)
    (A12_d, A12_m, A12_s) = Conversion.radtodms(A12)
    #DETERMINATION D'AZIMUT DE RETOUR
    A21=(mp.acot(-((tan(phi1)*cos(phi2)/sin(delta_lambda))-sin(phi2)*mp.cot(delta_lambda))))
    (A21_d, A21_m, A21_s) = Conversion.radtodms(A21)
    a = 6378249.20
    b = 6356515.0
    #print(sigma12*main.calcul_rayon_Gauss(a,b))
    print(Conversion.radtodms(A12))
    print(Conversion.radtodms(A21))


probleme_inverse(35,3,0,35,7,40.34,-6,48,0,-6,44,42.07)

