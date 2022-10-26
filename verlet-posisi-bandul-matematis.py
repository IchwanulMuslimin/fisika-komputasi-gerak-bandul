#import module
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

#Notasi that used for this program :
"""
xn = for position at n indeks
xnp1 = for position at n plus 1 indeks (n+1)
xnm1 = for position an n minus 1 indeks (n-1)
"""

#initial variabel
x0 = 1.0 
vx0 = 0.0
dt = 0.05

#gravitation acceleration
g = 9.8
l =10.0

#initial acceleration
a0 = (-g/l)*x0

x1 = x0 + vx0*dt + 0.5*ax0*dt**2

xnm1 = x0
xn = x1

#array for collect the value of position and time
x = [x0,x1]
t = [0.0, dt]
tn = dt

#iteration using verlet position method 
for i in range(400):
  #update value of acceleration 
  axn = (-g/l)*xn
  
  #verlet posisition method
  xnp1 = 2*xn-xnm1+axn*dt**2
  
  #save the value for the next iteration
  xn = xnp1
  xnm1 = xn 
  tn+=dt
  
  #append into array 
  x.append(xnp1)
  t.append(tn)
 
#plot 
plt.plot(t,x,"ob")
plt.show()
  
