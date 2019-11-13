from vpython import *

#Analysis of use of gravitational slingshot

#Constants
G = 1.0
dt = 0.04

#Big mass
star = sphere(pos=vector(6.7,0.0,0.0), radius = 1.0, color=color.red)
star.mass = 10.0
star.p = vector(-1.0,0.0,0.0) * star.mass

#Satelite
satelite = sphere(pos=vector(-8.0,-8.0, 0.0), radius = 0.4, color=color.blue)
satelite.mass = 0.000000000000001
satelite.p = vector(0.8, 0.6, 0.0) * satelite.mass

while True:
    rate(50)
    print("Velocity = " + str(sqrt(mag2(satelite.p/satelite.mass))))
    dr = star.pos - satelite.pos
    F = G * star.mass * satelite.mass * dr.hat / mag2(dr)
    star.p = star.p - F * dt
    star.pos = star.pos + dt * (star.p/star.mass)
    satelite.p = satelite.p + F * dt
    satelite.pos = satelite.pos + dt * (satelite.p/satelite.mass)
