curso1 = "Curso de Python "
curso2 = "Curso de CSharp "
dia = 15
mes = "Desembro"
ano = 2024
cidade = "Luanda"

res1 = "Python".upper() in curso1.upper()
res2 = "Python" not in curso1
res3 = curso1 + " e " + curso2
res4 = "{}, {} de {} de {}"

#\' \" \n \r \t \b    Caracteres de escape

print(res1)
print(res2)
print(res3)
print(res4.format(cidade, dia, mes, ano))
print(cidade + ", " + str(dia) + " de "+ mes + " de " + str(ano) )
