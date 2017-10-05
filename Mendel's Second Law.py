import scipy
from scipy.stats import binom

instring = "7 30"

k, N = (int(elem) for elem in instring.split(" "))

k_big = 2**k

print(1 - binom.cdf(N - 1, k_big, 0.25))