def somar(n1, n2):
    r= n1 + n2
    print("Soma de " +str(n1)+ " + " +str(n2) + " = " +str(r))
somar(10,17)

def textos(*t):  #Argumento Arbitrário
    print(t[0])
    print(t[1])
    print(t[2])
textos("Belchior", "Quirinda", "Soares", "Domingos")

def carros(c = "golf"):
    print("Modelo: " +c)
carros()

valores = [10,20,30]
def soma(num):
    r = 0
    for n in num:
        r += n
    print("Soma: " +str(r))
soma(valores)