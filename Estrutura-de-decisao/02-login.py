# Solicitar o login do usuário
login = input("Digite seu login: ")

# Solicitar a senha do usuário
senha = input("Digite sua senha: ")

#Verificar se o login e a senha estão corretos
if login == "admin" and senha == "1234":
    print("Seja bem-vindo, administrador!")
else:
    print("Login ou senha incorretos!")