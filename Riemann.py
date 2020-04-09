import numpy as np
from matplotlib.pyplot import *
#number 1
h = 0.01
t = np.arange(0, 10, h)
v = np.empty(len(t))
for i in range(len(t)):
    v[i] = t[i] * np.sin(t[i])
x = np.empty(len(t))
for i in range(len(t)):
    x[i] = t[i] * np.cos(t[i]) + np.sin(t[i])
print('Position at ten seconds = ', x[-1])
#Right Riemann sum
def RiemannR(f, inc):
    sumr = np.zeros(len(t))
    for i in range(len(t)-1):
        sumr[i+1] = sumr[i] + f[i+1]*inc
    return sumr

#Trapezoid Rule
def RiemannT(f, inc):
    sumt = np.zeros(len(t))
    for i in range(len(t)-1):
        sumt[i+1] = sumt[i] + inc*(f[i]+f[i+1])/2
    return sumt

a = np.empty(len(t))
for i in range(len(t)):
    a[i] = np.sin(t[i]) - t[i]*np.cos(t[i])

RlargeErr = a - (RiemannR(v, 0.1))
RsmallErr = a - (RiemannR(v, 0.01))
RsmallerErr = a - (RiemannR(v, 0.001))
RsmallestErr = a - (RiemannR(v, 0.0001))
TlargeErr = a - (RiemannT(v, 0.1))
TsmallErr = a - (RiemannT(v, 0.01))
TsmallerErr = a - (RiemannT(v, 0.001))
TsmallestErr = a - (RiemannT(v, 0.0001))
figure(1)
plot(t, RlargeErr, label = 'Riemann with 0.1')
plot(t, RsmallErr, label = 'Riemann with 0.01')
plot(t, RsmallerErr, label = 'Riemann with 0.001')
plot(t, RsmallestErr, label = 'Riemann with 0.0001')
legend()
figure(2)
plot(t, TlargeErr, label = 'Trapezoid with 0.1')
plot(t, TsmallErr, label = 'Trapezoid with 0.01')
plot(t, TsmallerErr, label = 'Trapezoid with 0.001')
plot(t, TsmallestErr, label = 'Trapezoid with 0.0001')
legend()
show()