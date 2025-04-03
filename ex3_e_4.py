from itertools import combinations

def knapsack_brute_force(items, capacity):
    n = len(items)
    best_value = 0
    best_combination = []
    iterations = 0
    
    for r in range(n + 1):
        for subset in combinations(items, r):
            iterations += 1
            total_weight = sum(item[0] for item in subset)
            total_value = sum(item[1] for item in subset)
            
            if total_weight <= capacity and total_value > best_value:
                best_value = total_value
                best_combination = subset
    
    return best_value, best_combination, iterations

def knapsack_divide_and_conquer(items, capacity, n, iterations=[0]):
    if n == 0 or capacity == 0:
        return 0, iterations[0]
    
    iterations[0] += 1
    weight, value = items[n-1]
    
    if weight > capacity:
        return knapsack_divide_and_conquer(items, capacity, n-1, iterations)
    
    without_item, _ = knapsack_divide_and_conquer(items, capacity, n-1, iterations)
    with_item, _ = knapsack_divide_and_conquer(items, capacity - weight, n-1, iterations)
    
    return max(with_item + value, without_item), iterations[0]

def knapsack_dynamic_programming(N, C, items):
    maxTab = [[0] * (C + 1) for _ in range(N + 1)]
    iterations = 0
    
    for i in range(1, N + 1):
        weight, value = items[i-1]  # items are zero-indexed
        for j in range(1, C + 1):
            iterations += 1
            if weight <= j:
                maxTab[i][j] = max(maxTab[i-1][j], value + maxTab[i-1][j-weight])
            else:
                maxTab[i][j] = maxTab[i-1][j]
    
    return maxTab[N][C], iterations

# Testando os três métodos
items = [(2, 3), (3, 4), (4, 5), (5, 8)]  # (peso, valor)
capacity = 5

# Teste com força bruta
best_value_brute, best_combination_brute, iterations_brute = knapsack_brute_force(items, capacity)
print("Brute Force:")
print("Melhor valor:", best_value_brute)
print("Melhor combinação:", best_combination_brute)
print("Número de iterações:", iterations_brute)

# Teste com divisão e conquista
best_value_dc, iterations_dc = knapsack_divide_and_conquer(items, capacity, len(items))
print("\nDivide and Conquer:")
print("Melhor valor:", best_value_dc)
print("Número de iterações:", iterations_dc)

# Teste com programação dinâmica
best_value_dp, iterations_dp = knapsack_dynamic_programming(len(items), capacity, items)
print("\nDynamic Programming:")
print("Melhor valor:", best_value_dp)
print("Número de iterações:", iterations_dp)
