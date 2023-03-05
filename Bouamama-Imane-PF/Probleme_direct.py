from math import *
import main
import Conversion


def Direct(phi1_d,phi1_m,phi1_s,A12d,A12m,A12s,s,lambda1_d,lambda1_m,lambda1_s):
    phi1=Conversion.dms2rad(phi1_d,phi1_m,phi1_s)
    lambda_1=Conversion.dms2rad(lambda1_d,lambda1_m,lambda1_s)
    A12=Conversion.dms2rad(A12d,A12m,A12s)



    sigma12= s/main.calcul_rayon_Gauss(6378249.145,6356515)
    print(sigma12)


print(Direct(35,0,0,30,0,0,10000,-6.8,0,0))

