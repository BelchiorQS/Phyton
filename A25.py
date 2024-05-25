import os

class Carro:
    def __init__(self, nome, pot):
        self.nome = nome
        self.pot = pot
        self.ligado = False
        self.velmax = int(pot) * 2

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def info(self):
        print("Nome: ", self.nome)
        print("Potencia: ", self.pot)
        print("Valor Maximo: ", self.velmax)
        print("Ligado: ", "Ligado" if self.ligado else "Desligado")

carros = []

def menu():
    os.system("cls") or None

    print("1 - Novo carro")  
    print("2 - Informações de carro")  
    print("3 - Excluir carro")  
    print("4 - Ligar carro")  
    print("5 - Desligar carro")  
    print("6 - Listar carro")  
    print("7 - Sair")  

    print("Quantidade de carros: ", len(carros))
    opc = input("Digite uma opção: ")
    return opc

def novo_carro():
    os.system("cls") or None
    n = input("Nome do carro: ")
    p = input("Potencia do carro: ")
    
    car = Carro(n, p)
    carros.append(car)
    
    print("Novo carro Criado")
    os.system("pause") #dar uma pausa no Systema 

def informacoes():
    os.system("cls") or None
    n = input("Informe o numero do carro que deseja ver: ")
    try:
        carros[int(n)].info()
    except:
        print("Carro Não existe na lista")
    os.system("pause") #dar uma pausa no Systema 

def excluir_carro():
    os.system("cls") or None
    n = input("Informe o numero do carro que deseja excluir: ")
    try:
        del carros[int(n)]
        print("Carro excluído")
    except:
        print("Carro Não existe na lista")
    os.system("pause") #dar uma pausa no Systema 

def ligar_carro():
    os.system("cls") or None
    n = input("Informe o numero do carro que deseja ligar: ")
    try:
        carros[int(n)].ligar()
        print("Carro Ligado")
    except:
        print("Carro Não existe na lista")
    os.system("pause") #dar uma pausa no Systema 

def desligar_carro():
    os.system("cls") or None
    n = input("Informe o numero do carro que deseja desligar: ")
    try:
        carros[int(n)].desligar()
        print("Carro desligado")
    except:
        print("Carro Não existe na lista")
    os.system("pause") #dar uma pausa no Systema 

def listar_carros():
    os.system("cls") or None
    for i, carro in enumerate(carros):
        print(f"{i} - {carro.nome}")
    os.system("pause") #dar uma pausa no System

ret = menu()
while ret != "7":
    if ret == "1":
        novo_carro()
    elif ret == "2":
        informacoes()
    elif ret == "3":
        excluir_carro()
    elif ret == "4":
        ligar_carro()
    elif ret == "5":
        desligar_carro()
    elif ret == "6":
        listar_carros()
    ret = menu()

os.system("cls") or None
print("Fim do programa")
