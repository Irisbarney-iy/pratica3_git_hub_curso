nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"Olá {nome}, você tem a idade suficiente.\n\n")
    preferido = int(input("[1] Torta de limão \n[2] Torta de morango \n[3] Torta de abacaxi \n\nQual você prefere: "))
    if preferido == 1:
        print(f"\nLegal {nome}, você gosta de Torta de limão")
    elif preferido == 2:
        print(f"\nLegal {nome}, você gosta de Torta de morango")
    elif preferido == 3:
        print(f"\nLegal {nome}, você gosta de Torta de abacaxi")
    else: print(f"\nOpção inválida {nome}")
        
else: 
    print(f"Olá {nome}, você não tem a idade suficiente para acessar.")

print("\n\nFim do programa")