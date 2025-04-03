#Adrielle Dewes, Bianca Alves, Marcius Moraes, Conrado Crestani e Nicolas Ribeiro

import time
from functools import lru_cache
from tabulate import tabulate

def fibo_rec(n, counter):
    counter["iterations"] += 1
    counter["instructions"] += 2  # Uma comparação e uma soma/retorno
    if n <= 1:
        return n
    return fibo_rec(n - 1, counter) + fibo_rec(n - 2, counter)

def fibo(n, counter):
    f = [0] * (n + 1)
    f[0], f[1] = 0, 1
    counter["instructions"] += 2  # Atribuições iniciais
    for i in range(2, n + 1):
        counter["iterations"] += 1
        counter["instructions"] += 3  # Atribuição, acesso ao array e soma
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

@lru_cache(None)
def memoized_fibo(n):
    if n <= 1:
        return n
    return memoized_fibo(n - 1) + memoized_fibo(n - 2)

def test_fibonacci():
    test_values = [4, 8, 16, 32]
    algorithms = [
        ("FIBO-REC", fibo_rec),
        ("FIBO", fibo),
        ("MEMOIZED-FIBO", memoized_fibo)
    ]
    
    results = []
    for name, func in algorithms:
        row = [name]
        for n in test_values:
            counter = {"iterations": 0, "instructions": 0}
            start_time = time.time()
            result = func(n, counter) if name != "MEMOIZED-FIBO" else func(n)
            exec_time = time.time() - start_time
            
            row.append(f"{result} ({exec_time:.6f}s, {counter['iterations']} it, {counter['instructions']} instr)")
        results.append(row)
    
    print(tabulate(results, headers=["Algorithm"] + test_values, tablefmt="grid"))

# Run the tests
test_fibonacci()