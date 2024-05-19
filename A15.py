carro = {
    "Fabricante": "Honda", 
    "Modelo": "HMR",
    "Ano": "2024",
    "Cor": "Prata"
}

carro["Cor"] = "Preto" #Alterar valores do elemento
carro["Cambio"] = "Automatico" #Adicionar Elemento

carro.pop("Cor") #Remover elemento

print(carro["Modelo"])

print("tamnho do Dictionary:"  +str(len(carro)))

if "Modelo" in carro:
    print("SIM,Modelo e uma chave")

for c,v in carro.items():
    #print(x) #Chave
    print(c + ":" + v) #valor

carro.clear() #Limpar todo o dicionario

'''carros = {
    "Carro1":{
        "Fabricante": "Honda",
        "Modelo": "HRV"
    },

    "Carro2":{
        "Fabricante": "Volkswagem",
        "Modelo": "Golf"
    },

    "Carro3":{
        "Fabricante": "Ford",
        "Modelo": "Focus"
    }
}
print(carros["Carro1"]["Fabricante"])
'''

Carro1={
    "Fabricante": "Honda",
    "Modelo": "HRV"
}
Carro2={
    "Fabricante": "Volkswagem",
    "Modelo": "Golf"
}
Carro3={
    "Fabricante": "Ford",
    "Modelo": "Focus"
}

Carros={
    "C1": Carro1,
    "C2": Carro2,
    "C3": Carro3
}

print(Carros["C1"] ["Modelo"])