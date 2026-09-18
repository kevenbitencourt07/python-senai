# Faça um programa em Python que peça o peso (kg) 
# e a altura (m) de um indivíduo. Calcule o IMC
# mostre a sua classificação:

# Menor que 18,5: abaixo do peso
# De 18,5 a 24,9: peso normal
# 25 ou mais: acima do peso


# Entrada de dados
peso = float(input("Digite sua massa corporal (kg): "))
altura = float(input("Digite sua altura (m): "))

# Processamento computacional
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

# Saída / verificação de informações
if imc < 18.5:
    print("Você está abaixo do peso ideal!")
elif imc <= 24.9:
    print("Você está no peso ideal!")
else:
    print("Você está acima do peso ideal!")