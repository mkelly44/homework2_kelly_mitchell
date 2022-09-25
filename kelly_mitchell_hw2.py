from math import pi

T = float(input("Enter time (s): "))
R = 6371*10**3   #km to m conversion
G = 6.67*10**-11
M = 5.97*10**24

h = ((G*M*(T**2)/(4*pi**2))**(1/3)) - R
print(h)
