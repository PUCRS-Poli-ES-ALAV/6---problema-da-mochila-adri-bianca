def edit_distance_recursive(s1, s2, m, n, iterations=[0]):
    iterations[0] += 1
    if m == 0:
        return n, iterations[0]
    if n == 0:
        return m, iterations[0]
    
    if s1[m-1] == s2[n-1]:
        return edit_distance_recursive(s1, s2, m-1, n-1, iterations)
    
    insert_op, _ = edit_distance_recursive(s1, s2, m, n-1, iterations)
    remove_op, _ = edit_distance_recursive(s1, s2, m-1, n, iterations)
    replace_op, _ = edit_distance_recursive(s1, s2, m-1, n-1, iterations)
    
    return 1 + min(insert_op, remove_op, replace_op), iterations[0]


def edit_distance_dynamic(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    iterations = 0
    
    for i in range(m + 1):
        for j in range(n + 1):
            iterations += 1
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
    
    return dp[m][n], iterations


# Testando os métodos da distância de edição
s1 = "Casablanca"
s2 = "Portentoso"
distance_recursive, iterations_recursive = edit_distance_recursive(s1, s2, len(s1), len(s2))
print("\nEdit Distance (Recursive):")
print("Distância de edição:", distance_recursive)
print("Número de iterações:", iterations_recursive)

distance_dp, iterations_dp = edit_distance_dynamic(s1, s2)
print("\nEdit Distance (Dynamic Programming):")
print("Distância de edição:", distance_dp)
print("Número de iterações:", iterations_dp)
