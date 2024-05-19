class carro:
    velMax = 0
    ligado = False
    cor = ""
    def __init__(self,v,l,c):
        self.velMax = v
        self.ligado = l
        self.cor = c
    def mostrar(self):
        print("Velocidade Maxima: " + str(self.velMax))
        print("Cor: " + str(self.cor))
        estado = "Sim" if self.ligado else "nao" #Operador Ternário
        print("Ligado: " + str(estado))
        print("---------------------------------------------------")
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False
    def andar(self):
        if self.ligado:
            print("Andando....")
        else:
            print("Carro desligado..")
c1 = carro(200,False,"Preto")
c2 = carro(120,False, "Branco")
c3 = carro(350, False, "Vermelho")

c1.ligar()
c2.andar()
c1.mostrar()
c2.mostrar()
c3.mostrar()