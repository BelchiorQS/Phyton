import random
import os

erro = 0
sorteado = random.randrange(0,100)
jogador = int(input("Digit seu numero: "))
i = 0
while (sorteado != jogador):
    os.system("clear")
    if sorteado > jogador:
        print("ERRO, o numero e maior")
    elif (sorteado < jogador):
        print("ERRO, o numero e menor")
    erro += 1
    jogador = int(input("Digit seu numero: "))
print("Numero " + str(jogador)+", voce acertou em " +str(erro + 1)+ " Tentativas")

        
