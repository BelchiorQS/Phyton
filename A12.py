import os

carros = []
carro = input("Digite o nome do novo carro: ")
while carro != "-1":
    carros.append(carro)
    carro = input("Digite o nome do novo carro: ")
os.system("clear")
for c in carros:
    print(c)
print("Fim do programa!")