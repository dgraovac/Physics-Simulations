from vpython import *

#Constants
dt = 0.01
g = 9.81
length = 0.3

#Initial conditions
theta_i = pi/6
angular_velocity_i = 0.0

#Pendulum setup
pendulum = cylinder(pos=vector(0,0.2,0), axis=vector(sin(theta_i), -cos(theta_i), 0) * length, radius = 0.001)
point = sphere(pos=pendulum.pos + pendulum.axis, radius=0.02)

#Variables
theta = theta_i
angular_v = angular_velocity_i

while True:
    rate(50)
    dw = -(g/length) * sin(theta) * dt
    angular_v = (angular_v + dw)
    d_theta = angular_v * dt
    theta = theta + d_theta

    pendulum.axis = vector(sin(theta), -cos(theta), 0) * length
    point.pos = pendulum.pos + pendulum.axis
