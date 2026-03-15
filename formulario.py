nome = input("Digite seu nome: ")
idade = int(input("Diite sua idade: "))

if idade >= 18:
    print(f"Olá {nome}, você tem a idade suficiente.")
else: 
    print(f"Olá {nome}, você não tem a idade suficiente para acessar.")