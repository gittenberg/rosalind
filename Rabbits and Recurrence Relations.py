def LinearFibonacci(n, k):
    fn = f1 = f2 = 1
    for x in range(2, n):
        fn = f1 + k * f2
        f2, f1 = f1, fn
    return fn

n = 31
k = 4
print(LinearFibonacci(n, k))