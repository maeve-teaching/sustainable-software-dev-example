import numpy as np
import matplotlib.pyplot as plt
# A module to calculate the hypotenuse of a
# right angled triangle

# a^2 = b^2 + c^2
# a = sqrt(a^2 + b^2)

# function to calculate the squ

# maybe analytical model?

def Temp_rt(a, T_i, T_s, r, t, k):
    """
    A function to calculate the T at a specific r, t, analytical solution provided by Sterenborg and Crowley, 2013
    """
    factor = (2 * a * T_i)/(np.pi * r)
    sum_list = []
    for n in range(1,500,1):
        sum_coef = (((-1)**n + 1)/n) * np.sin((n * np.pi *r)/a)*np.e**(-k*(n**2) * (np.pi**2) * (t/a**2))
        sum_list.append(sum_coef)
    T_rt = factor * sum(sum_list)
    return(T_rt)


a = 700
T_i = 1200
T_s = 0
r = 70
t = 25
k = 5

r0 = 1
R = 300

t0 = 1
tf = 10000 #myr

temp = Temp_rt(a, T_i, T_s, r, t, k)
print(temp)

t = np.arange(10, 1000, 10)
# temps = np.zeroslike(t)
temp = Temp_rt(a, T_i, T_s, r, t, k)
temp

plt.scatter(t, temp)
plt.savefig("testing.png")