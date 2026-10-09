saldo = float(input("Digite o saldo disponível:R$ "))
valor_compra = float(input("Digite o valor da compra:R$ "))
if saldo >= valor_compra:
    confirmação = input("Deseja confirmar compra?")
    if confirmação == "sim":
        print("Compra realizada")
    else:
        print("Compra cancelada")
else:
    print("Saldo infuciente")