from random import random
from random import uniform
from random import randint

class Particle:
    def __init__(self, bounds):
        self.position_i = []  # particle position
        self.velocity_i = []  # particle velocity
        self.pos_best_i = []  # best position individual
        self.err_best_i = -1  # best error individual
        self.err_i = -1  # error individual

        for i in range(0, num_dimensions):
            self.velocity_i.append(uniform(-1, 1))
            self.position_i.append(randint(bounds[i][0], bounds[i][1]))

    # evaluate current fitness
    def evaluate(self, costFunc):
        self.err_i = costFunc(self.position_i)

        # check to see if the current position is an individual best
        if self.err_i < self.err_best_i or self.err_best_i == -1:
            self.pos_best_i = self.position_i.copy()
            self.err_best_i = self.err_i

    # update new particle velocity
    def update_velocity(self, pos_best_g, i):
        # w = 0.5 #  * i/(i+1)  # inertia weight (how much to weigh the previous velocity)
        # print("W: ", w)
        c1 = 2  # cognative constant
        c2 = 1  # social constant

        for i in range(0, num_dimensions):
            r1 = random()
            r2 = random()

            vel_cognitive = c1 * r1 * (self.pos_best_i[i] - self.position_i[i])
            vel_social = c2 * r2 * (pos_best_g[i] - self.position_i[i])
            self.velocity_i[i] = comp_factor * (w * self.velocity_i[i] + vel_cognitive + vel_social)  # compression factor added

    # update the particle position based off new velocity updates
    def update_position(self, bounds):
        for i in range(0, num_dimensions):
            self.position_i[i] = self.position_i[i] + self.velocity_i[i]

            # adjust maximum position if necessary
            if self.position_i[i] > bounds[i][1]:
                self.position_i[i] = bounds[i][1]

            # adjust minimum position if neseccary
            if self.position_i[i] < bounds[i][0]:  # if it goes outside the field, set it on the field border
                self.position_i[i] = bounds[i][0]


def minimize(costFunc, nd, bounds, num_particles, maxiter, comp_fac, verbose=False):

    global num_dimensions, comp_factor, minuser, w
    num_dimensions = nd
    comp_factor = comp_fac
    minuser = 0.5/maxiter # w decreases linearly  from 0.9 to 0.4
    w = 0.9 # 0.7298

    err_best_g = -1  # best error for group
    pos_best_g = []  # best position for group

    # establish the swarm
    swarm = []
    for i in range(0, num_particles):
        swarm.append(Particle(bounds)) # adds a new particle to the swarm

    # begin optimization loop
    i = 0
    while i < maxiter:
        if verbose: print(f'iter: {i:>4d}, best solution: {err_best_g:10.6f}')

        # cycle through particles in swarm and evaluate fitness
        for j in range(0, num_particles):
            swarm[j].evaluate(costFunc)

            # determine if current particle is the best (globally)
            if swarm[j].err_i < err_best_g or err_best_g == -1:
                pos_best_g = list(swarm[j].position_i)
                err_best_g = float(swarm[j].err_i)

        # cycle through swarm and update velocities and position
        for j in range(0, num_particles):
            swarm[j].update_velocity(pos_best_g, i)
            swarm[j].update_position(bounds)
        w -= minuser
        i += 1


    # print final results
    pos_best_g_formated = ['%.4f' % elem for elem in pos_best_g]
    print('\nFINAL SOLUTION:')
    print(f'   Position: {pos_best_g_formated}')
    print(f'   Global optimum: {err_best_g:10.6f}\n')

    pass

