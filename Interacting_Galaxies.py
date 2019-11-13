from vpython import *

# Constants
G = 1.0 #Gravitational constant
dt = 0.08

#Central mass setup
central = sphere(pos=vector(0,0,0), radius=1.0, color=color.red)
central.mass = 3.0
central.p = vector(0,0,0)


#Interacting galaxy
interacting = sphere(pos=vector(2,-15,0), radius=1.0, color=color.orange)
interacting.mass = 3.0
interacting.p = vector(0.65,0.65,0) * interacting.mass


#Layer Setup
def create_layer(r, n_particles, col, centre, initial_velocity, big_mass):
    particles = []
    for x in range(0, n_particles):
        angle = random() * 2 * pi
        part = sphere(pos=vector(r * cos(angle), r * sin(angle), 0) + centre, radius = 0.2, color=col)
        part.mass = 0.001
        part.p = (vector(-r * sin(angle), r * cos(angle), 0).hat) * part.mass * sqrt((big_mass * G) / r) + initial_velocity * part.mass
        particles.append(part)
    return particles


#Initial galaxy
layer1 = create_layer(2, 48, color.white, vector(0,0,0), vector(0,0,0), central.mass)
layer2 = create_layer(3, 72, color.magenta, vector(0,0,0), vector(0,0,0), central.mass)
layer3 = create_layer(4, 96, color.yellow, vector(0,0,0), vector(0,0,0), central.mass)
layer4 = create_layer(5, 120, color.blue, vector(0,0,0), vector(0,0,0), central.mass)
layer5 = create_layer(6, 144, color.green, vector(0,0,0), vector(0,0,0), central.mass)

#Interacting galaxy
layer6 = create_layer(2, 48, color.white, interacting.pos, interacting.p/interacting.mass, interacting.mass)
layer7 = create_layer(3, 72, color.magenta, interacting.pos, interacting.p/interacting.mass, interacting.mass)
layer8 = create_layer(4, 96, color.yellow, interacting.pos, interacting.p/interacting.mass, interacting.mass)
layer9 = create_layer(5, 120, color.blue, interacting.pos, interacting.p/interacting.mass, interacting.mass)
layer10 = create_layer(6, 144, color.green, interacting.pos, interacting.p/interacting.mass, interacting.mass)

layers = [layer1, layer2, layer3, layer4, layer5, layer6, layer7, layer8, layer9, layer10]


while True:
    rate(50)
    #Update position of galaxy centres
    dr = central.pos - interacting.pos
    F = G * central.mass * interacting.mass * dr.hat / mag2(dr)
    interacting.p = interacting.p + F * dt
    interacting.pos = interacting.pos + dt * (interacting.p/interacting.mass)
    central.p = central.p -F*dt
    central.pos = central.pos + dt * (central.p/central.mass)


    #Update positon of test masses
    for layer in layers:
        for part in layer:
            dr1 = central.pos - part.pos
            dr2 = interacting.pos - part.pos
            F = G * central.mass * part.mass * dr1.hat / mag2(dr1) + G * interacting.mass * part.mass * dr2.hat / mag2(dr2)
            part.p = part.p + F*dt
            part.pos = part.pos + dt * (part.p/part.mass)

            if mag2(part.p/part.mass) > 10:
                part.visible = False
