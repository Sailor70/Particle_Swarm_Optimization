import numpy as np
from numpy import abs, cos, exp, pi, sin, sqrt, sum

# Minimum globalne f(x*) = 0 dla x*=(0,...,0), zazwyczaj xi ∈ [-32.768, 32.768], dla wszystkich i = 1,...,d
def ackley( x, a=20, b=0.2, c=2*pi ):
    x = np.asarray_chkfinite(x)  # ValueError if any NaN or Inf
    n = len(x)
    s1 = sum( x**2 )
    s2 = sum( cos( c * x ))
    return -a*exp( -b*sqrt( s1 / n )) - exp( s2 / n ) + a + exp(1)

# Minimum globalne f(x*) = 0 dla x*=(420.9687,...,420.9687), zazwyczaj xi ∈ [-500, 500], dla wszystkich i = 1,...,d
def schwefel( x ):
    x = np.asarray_chkfinite(x)
    n = len(x)
    return 418.9829*n - sum( x * sin( sqrt( abs( x ))))
