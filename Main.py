
import math

import math

c = 3.00e8 # velocidadefloat
u0 = 4 * math.pi * 1e-7
# lambda = c/frequencia
# numero de onda(k) = 2PI/ lambda
# frequencia Angular(w) = 2PI * frequencia
# Em = c*Bm
#I = (Em ** 2)/ (2*u0*c) 

# completar com operações fisicas



# Função para calcular a partir da frequência
def opFrequencia():
    print("Frequência (f)")
    print("")
    f = float(input("Digite o valor da frequência (em Hz), por exemplo, 6.27e12: "))

    # a) Comprimento de onda (λ) em metros
    lambda_onda = c / f
    
    # b) Número de onda (k) em rad/m
    k = 2 * math.pi / lambda_onda
    
    # c) Frequência angular (ω) em rad/s
    omega = 2 * math.pi * f
    
    # Exibindo os resultados com formatação científica
    print("\nResultados:")
    print(f"Comprimento de onda (λ): {lambda_onda:.4e} m")
    print(f"Número de onda (k): {k:.4e} rad/m")
    print(f"Frequência angular (ω): {omega:.4e} rad/s")

# Função para calcular a partir do comprimento de onda
def opCompOnda():
    print("Comprimento de onda (λ)")
    print("")
    lambda_onda = float(input("Digite o valor do comprimento de onda (em metros): "))
    
    f = c / lambda_onda
    k = 2 * math.pi / lambda_onda
    omega = 2 * math.pi * f

    print("\nResultados:")
    print(f"Frequência (f): {f:.4e} Hz")
    print(f"Número de onda (k): {k:.4e} rad/m")
    print(f"Frequência angular (ω): {omega:.4e} rad/s")

# Função para calcular a partir do número de onda
def opNumOnda():
    print("Número de onda (k)")
    print("")
    k = float(input("Digite o valor do número de onda (em rad/m): "))

    lambda_onda = 2 * math.pi / k
    f = c / lambda_onda
    omega = 2 * math.pi * f

    print("\nResultados:")
    print(f"Frequência (f): {f:.4e} Hz")
    print(f"Comprimento de Onda (λ): {lambda_onda:.4e} m")
    print(f"Frequência angular (ω): {omega:.4e} rad/s")

# Função para calcular a partir da frequência angular
def opFreAng():
    print("Frequência angular da onda (ω)")
    print("")
    
    omega = float(input("Digite o valor da frequência angular da onda (em rad/s): "))

    f = omega / (2 * math.pi)
    lambda_onda = c / f
    k = 2 * math.pi / lambda_onda

    print("\nResultados:")
    print(f"Comprimento de Onda (λ): {lambda_onda:.4e} m")
    print(f"Número de onda (k): {k:.4e} rad/m")
    print(f"Frequência (f): {f:.4e} Hz")
    
def opCampMag():
    print("Campo Magnetico (Bm)")
    print("")

    Bm = float(input("Digite o valor em Tesla(T) da amplitude do campo magnetico:"))
    # tem que haver alguma conversao de dados, ex: uT para T ou vice versa
    Em = c*Bm
    I = (Em **2)/(2*u0*c)

    print("\nResultados:")
    print(f"Amplitude do campo elétrico (Em): {Em:.4e} V/m")
    print(f"Intensidade da onda (I): {I:.4e} W/m²")

def opCampEle():
    print("Campo Eletrico")
    print("")
    Em = float(input("Digite o valor em Volts por metro (V/m ) da amplitude do campo eletrico:"))

    Bm = Em/c
    I = (Em **2)/(2*u0*c)
    print("\nResultados:")
    print(f"Amplitude do campo Magnetico (Bm): {Bm:.4e} T")
    print(f"Intensidade da onda (I): {I:.4e} W/m²")

def opInt():
    print("Intensidade da Onda")
    print("")
    I = float(input("Digite o valor em Watts por metro quadrado (w/m²) da Intensidade da onda:"))

    Em = math.sqrt((I * 2*u0*c))
    Bm = Em/c
    print("\nResultados:")
    print(f"Amplitude do campo elétrico (Em): {Em:.4e} V/m")
    print(f"Amplitude do campo Magnetico (Bm): {Bm:.4e} T")


def showDevs():
    print("")
    print("----Desenvolvedores---")
    print("igor de Araujo - RA: 22.223.006-2")
    print("Gabriel Afonso - RA: 22.223.001-3")
    print("Gustavo Trovo - RA: 22.223.018-7")
    print("")

def showInfo():
    print("---------------------")
    print("Então você quer saber mais a respeito de Ondas Eletromagnéticas?.\n")
    print("As ondas eletromagnéticas são ondas que se propagam pelo espaço com a ajuda de campos elétricos e magnéticos oscilantes.")
    print("Elas não necessitam de um meio material para sua propagação e podem viajar através do vácuo.")
    print("Alguns exemplos de ondas eletromagnéticas incluem:")
    print("- Luz visível")
    print("- Ondas de rádio")
    print("- Micro-ondas")
    print("- Raios-X")
    print("Essas ondas são descritas pela teoria eletromagnética de Maxwell e variam em comprimento de onda e frequência, o que determina suas propriedades e aplicações.")
    print("A velocidade das ondas eletromagnéticas no vácuo é aproximadamente 300.000 km/s.")
    print("---------------------")


def showOp():
    while True: 
        print("-- Menu de Exercicios --")
        print("Selecione a opcao com base nos valores oferecidos pelo exercicio:")
        print("")
        print("5 - Ex com campo magnetico")
        print("4 - Frequencia Angular")
        print("3 - Numero de Onda")
        print("2 - Comprimento de Onda")
        print("1 - frequencia")
        print("0 - Sair")

        i = int(input(""))

        if i == 0:  
            break
        elif i == 1:
            opFrequencia()
        elif i == 2:
            opCompOnda()
        elif i == 3:
            opNumOnda()
        elif i == 4:
            opFreAng()
        elif i == 5:
            while True: 
                print("--Menu de Campo Magnetico--")
                print("Selecione a opcao com base nos valores oferecidos pelo exercicio:")
                print("")
                print("3 - Intesidade da Onda (I)")
                print("2 - Amplitude do Campo Eletrico (Em)")
                print("1 - Amplitude do campo Magnetico (Bm) ")
                print("0 - Sair")

                i = int(input(""))

                if i == 0:  
                    break
                elif i == 1:
                    opCampMag()
                elif i == 2:
                    opCampEle()
                elif i == 3:
                    opInt()

                else:
                    print("Opação invalida")
        else:
            print("Opação invalida")


print("Bem-vindo!\n")
print("Este programa tem o objetivo de resolver exercícios relacionados a ondas eletromagnéticas.")
print("Ele pode calcular os seguintes parâmetros:")
print("- Frequência angular")
print("- Número de onda")
print("- Comprimento de onda")
print("- Frequência")
print("- Amplitude do campo elétrico")
print("- Amplitude do campo magnético")
print("- Intensidade do campo eletromagnético\n")
print("O código funciona com base no exercício fornecido.")
print("Se o exercício te fornece apenas a frequência angular e você deseja descobrir outros elementos,")
print("vá para a opção 1 - Fazer Exercícios, selecione a opção 4 - Frequência Angular e digite o número no formato científico.")
print("")
print("--Desenvolvedores--")
print("igor de Araujo - RA: 22.223.006-2")
print("Gabriel Afonso - RA:22.223.001-3")
print("Gustavo Trovo - RA: 22.223.018-7")

while True: 
    print("--Menu Principal --")
    print("3 - Quero saber mais sobre OEM")
    print("2 - Fazer Exercicios")
    print("1 - Desenvolvedores")
    print("0 - Sair")

    i = int(input(""))

    if i == 0:  
        break
    elif i == 1:
        showDevs()
    elif i == 2:
        showOp()
    elif i ==3:
        showInfo()
    else:
        print("Opação invalida")

