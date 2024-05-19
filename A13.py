t_carros = ("HRV", "Golf", "Argo", "Focus")
l_carros = list(t_carros)
l_carros[2] = "Focus"
t_carros = list(l_carros)
 

for x in t_carros:
    print(x)
print("Fim do programa")