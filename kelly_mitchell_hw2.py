from math import pi

T = float(input("Enter time of orbit (s): "))
R = 6371*10**3   #km to m conversion
G = 6.67*10**-11
M = 5.97*10**24

h = ((G*M*(T**2)/(4*pi**2))**(1/3)) - R      #altitude formula from part a

h1440 = ((G*M*(86400**2)/(4*pi**2))**(1/3)) - R   #T = 1 Day (1440 Minutes)
h90 = ((G*M*(5400**2)/(4*pi**2))**(1/3)) - R      #T = 90 Minutes
h45 = ((G*M*(3600**2)/(4*pi**2))**(1/3)) - R      #T = 45 Minutes

# Orbital Periods less than 5063 seconds produce an unphysical altitude which would be inside the radius of the Earth

if T<=5063.38783:  
   print("This orbital period is too small")

else:
    print("The altitude of the satellite is",h,"meters")
    print("The altitude of a satellite that orbits in a day is",h1440,"meters")
    print("The altitude of a satellite that orbits in 90 minutes is",h90,"meters")
    print("The altitude of a satellite that orbits in 45 minutes is",h45,"meters")


# We can conclude that satellites cannot have an orbital period of 45 minutes, and orbital periods of around 90 minutes are typical of low earth orbiting satelites 


