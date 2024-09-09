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

    Bm = float(input("Digite o valor da amplitude do campo magnetico:"))
    # tem que haver alguma conversao de dados, ex: uT para T ou vice versa
    Em = c*Bm
    I = (Em **2)/(2*u0*c)

    print("\nResultados:")
    print(f"Amplitude do campo elétrico (Em): {Em:.4e} V/m")
    print(f"Intensidade da onda (I): {I:.4e} W/m²")

def opCampEle():
    print("Campo Eletrico")
    print("")
    Em = float(input("Digite o valor da amplitude do campo eletrico:"))

    Bm = Em/c
    I = (Em **2)/(2*u0*c)
    print("\nResultados:")
    print(f"Amplitude do campo Magnetico (Bm): {Bm:.4e} T")
    print(f"Intensidade da onda (I): {I:.4e} W/m²")

def opInt():
    print("Intensidade da Onda")
    print("")
    I = float(input("Digite o valor da Intensidade da onda:"))

    Em = math.sqrt((I * 2*u0*c))
    Bm = Em/c
    print("\nResultados:")
    print(f"Amplitude do campo elétrico (Em): {Em:.4e} V/m")
    print(f"Amplitude do campo Magnetico (Bm): {Bm:.4e} T")

