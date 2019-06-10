import matplotlib.pyplot as plt
from random import randrange
from math import exp,sqrt,log


def f(n,a,b,c):
    return 1/(a+(n/b)**(c))


def C(n,r,a,b,c):
    k=0
    S=n
    while S>1:
        S*=(1-f(S,a,b,c))
        k+=1
    ni=n
    s1=0
    s2=0
    for i in range(k):
        s1+=ni
        s2+=(ni*ni)
        ni*=(1-f(ni,a,b,c))
    return (999*n+498501/(16*r*r)+12*n+4*k+244708*s1+2*s2)/(2*10**8)


def excel(n):
    return 0.4671*exp(n*0.0205)

n_max=250
rayon=20
#a modifie la pente a l'origine
#b modifie la vitesse de croissance
#c modifie l'asymptote

a4,b4,c4=11,47,4.3

C0=[excel(n) for n in range(n_max)]
C4=[C(n,rayon,a4,b4,c4) for n in range(n_max)]    
X=[i for i in range(n_max)]
plt.plot(X,C0,"black",label="Simulation")
plt.plot(X,C4,"red",label="Modèle")
plt.legend()
plt.xlabel("Nombre de disques à l'instant initial")
plt.ylabel("Temps de calcul (s)")
plt.show()