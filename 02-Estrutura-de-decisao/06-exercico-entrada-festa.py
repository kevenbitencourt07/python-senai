# 18 anos ou mais: Pode entrar na festa.
# 16 ou 17 anos: Pode entrar com responsável.
# Menos de 16 anos: Não pode entrar na festa.


# Solicita a idade
idade = int(input("Digite sua idade: "))

# Verifica a idade
if idade >= 18:
    print("Você pode entrar na festa!")
elif idade == 17 or idade == 16:
    print("Você pode entrar somente acompanhado do seu responsável!")
else:
    print("Você não pode entrar na festa!")