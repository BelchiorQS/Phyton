soma = lambda a,b: a + b
mult = lambda a,b,c: (a +b) *c
print((lambda a,b: a - b)(3,2))

print(soma(10, 5))
print(mult(2, 5,3))

r= lambda x,func:x +func(x)
res = r(2,lambda x:x+x)
print(res)