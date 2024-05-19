valores = [10,20,30]
def somar(num):
    r = 0
    for n in num:
        r += n
    return r
print(somar(valores))
print("Soma = " +str(somar(valores)))