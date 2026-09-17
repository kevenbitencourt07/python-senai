# Crie um programa que solicite o nome de um produto, 
# seu preço e a quantidade comprada. Depois, calcule o valor total da compra
# e exiba o nome do produto e o valor total.

# Entrada de dados
produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

# Processamento computacional
valor_total = preco * quantidade

# Saída de informações
print(f"Produto: {produto}")
print(f"Preço do produto: R${preco:.2f}")
print(f"Quantidade comprada: {quantidade} unidades")
print(f"Valor total da compra: R${valor_total}")