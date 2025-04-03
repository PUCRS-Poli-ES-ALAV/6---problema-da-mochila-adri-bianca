#Adrielle Dewes, Bianca Alves, Marcius Moraes, Conrado Crestani e Nicolas Ribeiro

import time

def fibo_rec(n):
    if n <= 1:
        return n
    return fibo_rec(n - 1) + fibo_rec(n - 2)

def fibo(n):
    f = [0] * (n + 1)
    f[0], f[1] = 0, 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

def memoized_fibo(n):
    f = [-1] * (n + 1)
    return lookup_fibo(f, n)

def lookup_fibo(f, n):
    if f[n] >= 0:
        return f[n]
    if n <= 1:
        f[n] = n
    else:
        f[n] = lookup_fibo(f, n - 1) + lookup_fibo(f, n - 2)
    return f[n]

def test_fibonacci():
    test_values = [4, 8, 16, 32]
    extended_test_values = [128, 1000, 10000]
    
    print("Testing FIBO-REC:")
    for n in test_values:
        start_time = time.time()
        result = fibo_rec(n)
        print(f"FIBO-REC({n}) = {result}, Time: {time.time() - start_time:.6f} sec")
    
    print("\nTesting FIBO:")
    for n in test_values:
        start_time = time.time()
        result = fibo(n)
        print(f"FIBO({n}) = {result}, Time: {time.time() - start_time:.6f} sec")
    
    print("\nTesting MEMOIZED-FIBO:")
    for n in test_values + extended_test_values:
        start_time = time.time()
        result = memoized_fibo(n)
        print(f"MEMOIZED-FIBO({n}) = {result}, Time: {time.time() - start_time:.6f} sec")

# Run the tests
test_fibonacci()
