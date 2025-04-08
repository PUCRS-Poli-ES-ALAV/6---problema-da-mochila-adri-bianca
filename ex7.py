from tabulate import tabulate
import time

def dist_ed_prog_dina(A: str, B: str) -> tuple:
    m, n = len(A), len(B)
    matriz = [[0] * (n + 1) for _ in range(m + 1)]
    iterations = 0
    instructions = 0

    start_time = time.time()

    # Inicializa primeira coluna (remoções)
    for i in range(1, m + 1):
        matriz[i][0] = matriz[i - 1][0] + 1
        iterations += 1
        instructions += 2  # atribuição + soma

    # Inicializa primeira linha (inserções)
    for j in range(1, n + 1):
        matriz[0][j] = matriz[0][j - 1] + 1
        iterations += 1
        instructions += 2  # atribuição + soma

    # Preenchendo a matriz com os custos das operações
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            iterations += 1
            instructions += 1  # comparação
            if A[i - 1] == B[j - 1]:
                custo_extra = 0
            else:
                custo_extra = 1
            instructions += 4  # atribuição de custo_extra + 3 opções de min
            matriz[i][j] = min(
                matriz[i - 1][j] + 1,
                matriz[i][j - 1] + 1,
                matriz[i - 1][j - 1] + custo_extra
            )
            instructions += 4  # 3 somas + atribuição de min

    end_time = time.time()
    return matriz[m][n], iterations, instructions, end_time - start_time

# Casos de teste
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

# Executando os testes
dados = []
for A, B in [(s1_1, s2_1), (s1_2, s2_2)]:
    distancia, iteracoes, instrucoes, tempo = dist_ed_prog_dina(A, B)
    dados.append([
        A[:30] + ("..." if len(A) > 30 else ""),
        B[:30] + ("..." if len(B) > 30 else ""),
        distancia,
        iteracoes,
        instrucoes,
        f"{tempo:.6f}s"
    ])

# Tabela
cabecalho = ["Palavra A", "Palavra B", "Distância de Edição", "Iterações", "Instruções", "Tempo"]
print(tabulate(dados, headers=cabecalho, tablefmt="grid"))