carro = ["HRV", "Golf", "Argo", "Focus"]

#Adiciona Elementos a Lista
carro[0] = "Belchior QS"
carro.append("Quirinda") #Adiciona Elementos a Lista
carro.append("Soares")

#Remove Elementos da Lista
carro.remove("Argo") #Remove o elemento passdo como parametro
carro.pop() #Remove o ultimo elemento
del carro[1]

#Remove Elementos da Lista
print("Carros na Lista: " + str(len(carro)))
print(carro)
print(carro[0])
print(carro[-1])

#Copie elementos da Lista
carro2 = list(carro)

#Juntando os elementos da Lista
carro3 = carro + carro2

#Limpa toda a Lista carro
carro.clear() 

print(carro)
print(carro2)
print(carro3)