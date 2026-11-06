total = 0

for numero_despesas in range(1, 5):
    despesa = float(input("Digite o valor da despesa: R$"))
    total = total + despesa 

print("Valor total das despesas: R$", total)
