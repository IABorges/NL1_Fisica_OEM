import Funcoes

print("Bem Vindo!")
print("Este programa é dedicado ao Estudo de Ondas Eletromageneticas e foi desenvolvido por:")
print("igor de Araujo - RA:")
print("Gabriel Afonso - RA:")
print("Gustavo Trovo - RA:")

while True: 
    print("--Menu--")
    print("2 - Fazer Exercicios")
    print("1 - Desenvolvedores")
    print("0 - Sair")

    i = int(input(""))

    if i == 0:  
        break
    elif i == 1:
        Funcoes.showDevs()
    elif i == 2:
        Funcoes.showOp()
    else:
        print("Opação invalida")
