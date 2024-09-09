import math

c = 3.00e8 # velocidade
# lambda = c/frequencia
# numero de onda(k) = 2PI/ lambda
# frequencia Angular(w) = 2PI * frequencia
# completar com operações fisicas
def opFrequencia():
    print("Frequencia")
    print("")
    print("Digite o valor da Frequencia:")
    f = float(input("Digite o valor da Frequência (em Hz), por exemplo, 6.27e12: "))

     # a) Comprimento de onda (λ) em metros
    lambda_onda = c / f
    
    # b) Número de onda (k) em rad/m
    k = 2 * math.pi / lambda_onda
    
    # c) Frequência angular (ω) em rad/s
    omega = 2 * math.pi * f
    
    # Exibindo os resultados com formatação científica
    print("\nResultados:")
    print(f"a) Comprimento de onda (λ): {lambda_onda:.2e} m")
    print(f"b) Número de onda (k): {k:.2e} rad/m")
    print(f"c) Frequência angular (ω): {omega:.2e} rad/s")


def opCompOnda():
    print("em construção")
def opNumOnda():
    print("em construção")
def opFreAng():
    print("em construção")
def opCampMag():
    while True: 
        print("--Menu de Campo Magnetico--")
        print("2 -")
        print("1 - ")
        print("0 - Sair")

        i = int(input(""))

        if i == 0:  
            break
        elif i == 1:
            print("em construção")
        elif i == 2:
            print("em construção")
        else:
            print("Opação invalida")