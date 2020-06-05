import pso
import functions

bounds_ackley = [(-32,32),(-32,32)]
bounds_schwefel = [(-500,500),(-500,500),(-500,500)]
numParticles = [15, 30, 50]
maxIter = [30, 50, 100]
verbose = False
compression_factor = 0.7842

for i in range(0, 3):
    print("Variant: ", i)
    print("Ackley: ")
    pso.minimize(functions.ackley, 2, bounds_ackley, numParticles[i], maxIter[i], compression_factor, verbose)
    print("Schwefel: ")
    pso.minimize(functions.schwefel, 3, bounds_schwefel, numParticles[i], maxIter[i], compression_factor, verbose)
