def dist_ed_prog_dina(A: str, B: str) -> tuple:
    m, n = len(A), len(B)
    matriz = [[0] * (n + 1) for _ in range(m + 1)]
    iterations = 0
    
    # Inicializa primeira coluna (remoções)
    for i in range(1, m + 1):
        matriz[i][0] = matriz[i - 1][0] + 1  # Custo de remoção
        iterations += 1
    
    # Inicializa primeira linha (inserções)
    for j in range(1, n + 1):
        matriz[0][j] = matriz[0][j - 1] + 1  # Custo de inserção
        iterations += 1
    
    # Preenchendo a matriz com os custos das operações
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            iterations += 1
            if A[i - 1] == B[j - 1]:
                custo_extra = 0  # Match
            else:
                custo_extra = 1  # Substituição
            
            matriz[i][j] = min(
                matriz[i - 1][j] + 1,      # Remoção
                matriz[i][j - 1] + 1,      # Inserção
                matriz[i - 1][j - 1] + custo_extra  # Substituição
            )
    
    return matriz[m][n], iterations

# Testes com exemplos
A = "Casablanca"
B = "Portentoso"
distancia, iteracoes = dist_ed_prog_dina(A, B)
print("Distância de edição:", distancia)
print("Número de iterações:", iteracoes)
