idade = int(input("Digite sua idade:"))
ingresso = input("Voce possui ingresso?")
if idade >= 18:
    if ingresso == "sim":
     print("Entrada permitida")
    else:
        print("Ingresso necessário")
else:
    print("Idade insuficiente")
