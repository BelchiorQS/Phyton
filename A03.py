x = 1 #int
x = "Belchior" #string
x = 10.56 #float
x = True #bool
n1 = 1;n2 = 2;x = complex(n1,n2) #Complexo
ls =["carro","aviao","Navio",10,76.9,True] #List /Array
t = ("carro","aviao","Navio",10,76.9,True) #Tupla
Lr = range(0,100,1) #List
dn = {"Canal": "Belchior QS", "Curso": "Python", "Nome": "Lucas"} #Dicionário
st = {5,7,4,7,4,8} #set
fst = frozenset({5,7,4,7,4,8}) #frozenset

print("Dicionario: " +dn["Curso"])
print("Lista: " +str(ls[1]))
print(x.real)
print(x.imag)
print("Valor: " +str(x))
print("Tipo: "+str(type(x)))
print("Set: " +str(st))
print("Tipo: "+str(type(st)))