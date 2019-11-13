from vpython import *

#Constants
dt = 0.01
g = 9.81
length = 0.3

m1 = 1.0
m2 = 1.0

#Initial conditions
theta_1_i = pi/2
angular_v_1_i = 0.0
theta_2_i = pi/1.5
angular_v_2_i = 0.0

pendulum_1 = cylinder(pos=vector(0,0.2,0), axis=vector(sin(theta_1_i), -cos(theta_1_i), 0) * length, radius = 0.001)
point_1 = sphere(pos=pendulum_1.pos + pendulum_1.axis, radius=0.02)
pendulum_2 = cylinder(pos=pendulum_1.pos + pendulum_1.axis, axis=vector(sin(theta_2_i), -cos(theta_2_i), 0) * length, radius = 0.001)
point_2 = sphere(pos=pendulum_2.pos + pendulum_2.axis, radius = 0.02, make_trail=True)


theta_1 = theta_1_i
theta_2 = theta_2_i
angular_v_1 = angular_v_1_i
angular_v_2 = angular_v_2_i

momenta_1 = (m1 + m2) * angular_v_1 + m2 * angular_v_2 * cos(theta_1 - theta_2)
momenta_2 = m2 * angular_v_2 + m2 * angular_v_1 * cos(theta_1 - theta_2)


while True:
    rate(50)

    angular_v_1 = (momenta_1 - momenta_2 * cos(theta_1 - theta_2))/(m1 + m2 * (sin(theta_1 - theta_2)) ** 2)
    angular_v_2 = ((m1+m2) * momenta_2 - m2 * momenta_1 * cos(theta_1 - theta_2))/(m2 * (m1 + m2 * ((sin(theta_1-theta_2))**2)))

    C1 = (momenta_1 * momenta_2 * sin(theta_1 - theta_2))/(m1 + m2 * ((sin(theta_1 - theta_2)) ** 2))
    C2 = sin(2*(theta_1 - theta_2)) * ((m2 * (momenta_1 ** 2) + (m1 + m2)*(momenta_2 ** 2) - m2 * momenta_1 * momenta_2 * cos(theta_1 - theta_2)  )/(2 * (m1 + m2 * (sin(theta_1 - theta_2) ** 2)) ** 2))

    dp1_dt = -(m1 + m2) * g * sin(theta_1)  - C1 + C2
    dp2_dt = -m2 * g * sin(theta_2) + C1 - C2

    theta_1 = theta_1 + angular_v_1 * dt
    theta_2 = theta_2 + angular_v_2 * dt

    momenta_1 = momenta_1 + dp1_dt * dt
    momenta_2 = momenta_2 + dp2_dt * dt

    pendulum_1.axis = vector(sin(theta_1), -cos(theta_1), 0) * length
    point_1.pos = pendulum_1.pos + pendulum_1.axis

    pendulum_2.pos = pendulum_1.pos + pendulum_1.axis
    pendulum_2.axis = vector(sin(theta_2), -cos(theta_2), 0) * length
    point_2.pos = pendulum_2.pos + pendulum_2.axis
