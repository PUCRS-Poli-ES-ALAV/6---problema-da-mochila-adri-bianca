from itertools import combinations
from tabulate import tabulate
import time

def knapsack_brute_force(items, capacity):
    n = len(items)
    best_value = 0
    best_combination = []
    iterations = 0
    instructions = 0
    
    start_time = time.time()
    for r in range(n + 1):
        for subset in combinations(items, r):
            iterations += 1
            instructions += 2  # somas
            total_weight = sum(item[0] for item in subset)
            total_value = sum(item[1] for item in subset)
            instructions += len(subset) * 2  # cada acesso de item[0] e item[1]
            
            if total_weight <= capacity and total_value > best_value:
                instructions += 2  # comparação e atribuição
                best_value = total_value
                best_combination = subset
    end_time = time.time()
    return best_value, best_combination, iterations, instructions, end_time - start_time

def knapsack_divide_and_conquer(items, capacity, n, iterations=[0], instructions=[0]):
    if n == 0 or capacity == 0:
        instructions[0] += 1
        return 0, iterations[0], instructions[0]
    
    iterations[0] += 1
    instructions[0] += 2  # acesso e atribuição
    weight, value = items[n-1]
    
    if weight > capacity:
        instructions[0] += 1
        return knapsack_divide_and_conquer(items, capacity, n-1, iterations, instructions)
    
    without_item, _, _ = knapsack_divide_and_conquer(items, capacity, n-1, iterations, instructions)
    with_item, _, _ = knapsack_divide_and_conquer(items, capacity - weight, n-1, iterations, instructions)
    
    instructions[0] += 3  # soma, max e retorno
    return max(with_item + value, without_item), iterations[0], instructions[0]

def knapsack_dynamic_programming(N, C, items):
    maxTab = [[0] * (C + 1) for _ in range(N + 1)]
    iterations = 0
    instructions = 0
    start_time = time.time()
    
    for i in range(1, N + 1):
        weight, value = items[i-1]
        instructions += 2
        for j in range(1, C + 1):
            iterations += 1
            if weight <= j:
                maxTab[i][j] = max(maxTab[i-1][j], value + maxTab[i-1][j - weight])
                instructions += 4  # comparação + max + soma + atribuição
            else:
                maxTab[i][j] = maxTab[i-1][j]
                instructions += 2  # comparação + atribuição
    end_time = time.time()
    return maxTab[N][C], iterations, instructions, end_time - start_time

# Casos de teste
test_cases = [
    (165, [(23, 92), (31, 57), (29, 49), (44, 68), (53, 60), (38, 43), (63, 67), (85, 84), (89, 87), (82, 72)]),
    (190, [(56, 50), (59, 50), (80, 64), (64, 46), (75, 50), (17, 5)])
]

data = []

for capacity, items in test_cases:
    # Brute Force
    best_value_brute, best_combination_brute, iterations_brute, instr_brute, time_brute = knapsack_brute_force(items, capacity)

    # Divide & Conquer
    best_value_dc, iterations_dc, instr_dc = knapsack_divide_and_conquer(items, capacity, len(items))
    time_dc = 0  # não medido com precisão aqui, poderia ser incluído se necessário

    # Dynamic Programming
    best_value_dp, iterations_dp, instr_dp, time_dp = knapsack_dynamic_programming(len(items), capacity, items)
    
    # Preenche a tabela
    data.append([capacity, "Brute Force", best_value_brute, iterations_brute, instr_brute, f"{time_brute:.6f}s"])
    data.append([capacity, "Divide & Conquer", best_value_dc, iterations_dc, instr_dc, f"{time_dc:.6f}s"])
    data.append([capacity, "Dynamic Programming", best_value_dp, iterations_dp, instr_dp, f"{time_dp:.6f}s"])

# Exibir os resultados em formato de tabela
headers = ["Capacidade", "Método", "Melhor Valor", "Iterações", "Instruções", "Tempo"]
print(tabulate(data, headers=headers, tablefmt="grid"))