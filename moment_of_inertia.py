import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy import interpolate , integrate

#airfoil = np.genfromtxt('airfoil_upper.dat')
#fig, ax = plt.subplots()
#ax.plot(airfoil[:,0], airfoil[:,1], color='black')
#ax.set_xlabel('X position')
#ax.set_ylabel('Y position')
#plt.show()

lam = 0.28
b = 68.85
cr = 9.78
dihedral = 1.56
width = 0.45
height = 0.12
t = 0.005
a = 0.001

def chord_length(y):
    c = cr - (cr*(1-lam)/(b/2))*y
    return c

def moment_inertia(y):
    w = width * chord_length(y)
    h = height * chord_length(y)
    M_outer = 1/12 * (w+t/2) * (h+t/2)**3
    M_inner = 1/12 * (w-t/2) * (h-t/2)**3
    M_stringer = a * (h/2)**2
    return  M_outer - M_inner + M_stringer

y_list = []
I_list = []
dv_dy_list = []
y = b/2
n = 1000

for i in range(n+1):
    y -= ((b/2)/n)
    y_list.append(y)
    i = moment_inertia(y)
    I_list.append(i)

I_cont = sp.interpolate.interp1d(y_list,I_list,kind="previous",fill_value="extrapolate")

M_cont = 10e6
E = 72e9

Integ1 = sp.integrate.quad(lambda x: (M_cont/(E*I_cont(x))),0,b/2)
print(Integ1)



#plt.plot(y_list,Integ1(y_list))
#plt.show()
    




