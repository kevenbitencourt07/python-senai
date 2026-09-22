# Objetivo:
# Praticar variáveis, números inteiros, operações matemáticas e f-strings.

# Descrição:
# Crie um programa que represente o resultado de uma partida de futebol.
#  O programa deve armazenar o nome de dois times 
#  e a quantidade de gols marcados por cada equipa.

# Depois, apresente o placar e calcule o total de gols da partida.

# Resultado no terminal
# ================================
#         RESULTADO DO JOGO
# ================================
# França 3 x 2 Espanha
# Total de gols: 5
# ================================


time1 = "Corinthians"
time2 = "Palmeiras"

gols1 = 7
gols2 = 1

print("================================")
print("       RESULTADO DO JOGO       ")
print("================================")

print(f"{time1} {gols1} x {gols2} {time2}")
print(f"Total de gols: ", gols1 + gols2)

print("================================")