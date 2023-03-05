def Convertion(W):
    PI=3.14
    secondes = float(180 * W / PI * 3600)

    s = secondes % 60
    m = secondes // 60
    d = m // 60
    m = m % 60
    return (d,m,s)

#W=float(input("entrer la valeur:"))
#print(Conv(W))


