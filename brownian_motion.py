from vpython import *

#Constants
dt = 0.002
box_size = 10.0


#Setting up singular large particle
large_particle = sphere(pos=vector(0.0, 0.0, 0.0), radius=1.0, make_trail=True)
large_particle.mass = 10.0
large_particle.p = vector(0.0, 0.0, 0.0)


def create_particles(number, r):
    parts = []
    for i in range(0, number):
        x = (random()-0.5) * 20.0
        y = (random()-0.5) * 20.0

        #Check if random position collides with any existing particles OR with the large particle
        collision = True
        while collision == True:
            collision = False
            for other_particle in parts:
                if sqrt(mag2(other_particle.pos - vector(x,y,0.0))) < 2 * r:
                    collision = True
            if sqrt(mag2(vector(x,y,0.0))) + r < large_particle.radius:
                collision = True
            if collision == True:
                x = (random()-0.5) * 20.0
                y = (random()-0.5) * 20.0

        v_x = (random()-0.5) * 5.0
        v_y = (random()-0.5) * 5.0
        particle = sphere(pos=vector(x,y,0.0), radius=r, color=color.yellow)
        particle.mass = 1.0
        particle.p = vector(v_x, v_y, 0.0) * particle.mass
        parts.append(particle)
    return parts

particles = create_particles(100, 0.2)


#Adding large particle to particle list for collision detection
particles.append(large_particle)

while True:
    rate(50)

    for i in range(0, len(particles)):
        p1 = particles[i]
        for j in range(i+1, len(particles)):
            p2 = particles[j]

            #Check for collision
            if sqrt(mag2(p1.pos - p2.pos)) <= (p1.radius + p2.radius):
                m1 = p1.mass
                m2 = p2.mass
                u1 = p1.p/p1.mass
                u2 = p2.p/p2.mass

                p1.p = (u1 - (((2 * m2)/(m1+m2)) * (dot(u1 - u2, p1.pos - p2.pos)/(mag2(p1.pos - p2.pos)))) * (p1.pos - p2.pos) * p1.mass)
                p2.p = (u2 - (((2 * m1)/(m1+m2)) * (dot(u2 - u1, p2.pos - p1.pos)/(mag2(p2.pos - p1.pos)))) * (p2.pos - p1.pos) * p2.mass)
            #Update position after collision
            p1.pos = p1.pos + dt * (p1.p/p1.mass)
            p2.pos = p2.pos + dt * (p2.p/p2.mass)

        #Ensure particles stay in the confines of the box
        if abs(p1.pos.y) >= 10:
            p1.p.y = -p1.p.y
        if abs(p1.pos.x) >= 10:
            p1.p.x = -p1.p.x
