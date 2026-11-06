quantidade_vendas = 0
continuar = "sim"

while continuar == "sim":
     valor_venda = float(input("Valor da venda: R$ "))
     quantidade_vendas += 1
     continuar = input("Registrar outra venda? (sim/nao):").lower()

print(f"Quantidade de vendas: {quantidade_vendas}")