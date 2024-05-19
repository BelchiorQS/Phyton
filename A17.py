from re import sub


n1 = 10
n2 = 7
def somar():
    r= n1 + n2
    print("Soma de " +str(n1)+ " + " +str(n2) + " = " +str(r))
def Sub():
    r= n1 - n2
    print("Subtracao de " +str(n1)+ " - " +str(n2) + " = " +str(r))
def Mult():
    r= n1 * n2
    print("Multiplicacao de " +str(n1)+ " x " +str(n2) + " = " +str(r))
def Calculos():
    somar()
    Sub()
    Mult()
Calculos()