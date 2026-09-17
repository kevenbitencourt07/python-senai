# Faça um programa que peça o nome de um time de futebol,
# a quantidade de vitórias e empates.
# Sabendo que cada vitória vale 3 pontos e cada empate vale 1 ponto,
# calcule e mostre a pontuação total do time.

# Entrada de dados
time = input("Digite o time: ")
vitorias = int(input("Digite o número de vitórias: "))
empates = int(input("Digite o número de empates: "))

# Processamento computacional
vit = vitorias * 3
emp = empates * 1
pontuacao = vit + emp

# Saída de informações
print(f"Time: {time}")
print(f"Número de vitórias: {vitorias}")
print(f"Número de empates: {empates}")
print(f"Pontuação final: {pontuacao} pontos")