instring = "21 16 19"

k, m, n = (int(elem) for elem in instring.split(" "))

s = k + m + n
denom = s * (s - 1)
numer = k * (k - 1) + 2 * k * m + m * n + 0.75 * m * (m - 1) + 2 * k * n

print(1.0 * numer / denom)