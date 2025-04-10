from tabulate import tabulate
import time
import sys

# Aumenta o limite de recursão para casos razoavelmente grandes
sys.setrecursionlimit(10000)

# Contadores globais
instr_recursive = [0]
instr_dynamic = [0]

def edit_distance_recursive(s1, s2, i, j, iterations=[0]):
    iterations[0] += 1
    instr_recursive[0] += 1

    if i == 0:
        instr_recursive[0] += 1
        return j, iterations[0]
    if j == 0:
        instr_recursive[0] += 1
        return i, iterations[0]

    if s1[i-1] == s2[j-1]:
        instr_recursive[0] += 1
        return edit_distance_recursive(s1, s2, i-1, j-1, iterations)

    # Três operações possíveis
    instr_recursive[0] += 1
    sub_op, _ = edit_distance_recursive(s1, s2, i-1, j-1, iterations)  # Substituição
    instr_recursive[0] += 1
    ins_op, _ = edit_distance_recursive(s1, s2, i, j-1, iterations)    # Inserção
    instr_recursive[0] += 1
    rem_op, _ = edit_distance_recursive(s1, s2, i-1, j, iterations)    # Remoção

    instr_recursive[0] += 1
    return 1 + min(sub_op, ins_op, rem_op), iterations[0]


def edit_distance_dynamic(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    iterations = 0

    for i in range(m + 1):
        for j in range(n + 1):
            iterations += 1
            instr_dynamic[0] += 1

            if i == 0:
                dp[i][j] = j
                instr_dynamic[0] += 1
            elif j == 0:
                dp[i][j] = i
                instr_dynamic[0] += 1
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
                instr_dynamic[0] += 2
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
                instr_dynamic[0] += 3

    return dp[m][n], iterations

# Strings de teste
s1_1 = "Casablanca"
s2_1 = "Portentoso"

s1_2 = ("Maven, a Yiddish word meaning accumulator of knowledge, began as an attempt to " +
        "simplify the build processes in the Jakarta Turbine project. There were several" +
        " projects, each with their own Ant build files, that were all slightly different." +
        "JARs were checked into CVS. We wanted a standard way to build the projects, a clear " +
        "definition of what the project consisted of, an easy way to publish project information" +
        "and a way to share JARs across several projects. The result is a tool that can now be" +
        "used for building and managing any Java-based project. We hope that we have created " +
        "something that will make the day-to-day work of Java developers easier and generally help " +
        "with the comprehension of any Java-based project.")

s2_2 = ("This post is not about deep learning. But it could be might as well. This is the power of " +
        "kernels. They are universally applicable in any machine learning algorithm. Why you might" +
        "ask? I am going to try to answer this question in this article." +
        "Go to the profile of Marin Vlastelica Pogančić" +
        "Marin Vlastelica Pogančić Jun")

# Execução para os casos
tabela = []

# Caso curto: Casablanca x Portentoso (Recursivo e Dinâmico)
instr_recursive[0] = 0
start = time.time()
dist_rec, it_rec = edit_distance_recursive(s1_1, s2_1, len(s1_1), len(s2_1))
end = time.time()
tempo_rec = end - start
tabela.append(["Recursivo", "Casablanca x Portentoso", it_rec, instr_recursive[0], f"{tempo_rec:.6f} s"])

instr_dynamic[0] = 0
start = time.time()
dist_dyn, it_dyn = edit_distance_dynamic(s1_1, s2_1)
end = time.time()
tempo_dyn = end - start
tabela.append(["Dinâmico", "Casablanca x Portentoso", it_dyn, instr_dynamic[0], f"{tempo_dyn:.6f} s"])

# Caso longo: texto 1 x texto 2 (somente Dinâmico)
instr_dynamic[0] = 0
start = time.time()
dist_dyn2, it_dyn2 = edit_distance_dynamic(s1_2, s2_2)
end = time.time()
tempo_dyn2 = end - start
tabela.append(["Dinâmico", "Texto Longo x Texto Longo", it_dyn2, instr_dynamic[0], f"{tempo_dyn2:.6f} s"])

# Imprimir tabela final
print("\nComparação das implementações:")
print(tabulate(tabela, headers=["Implementação", "Caso", "Iterações", "Instruções", "Tempo"]))