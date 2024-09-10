import Funcoes

print("Bem Vindo!")
print("Este programa é dedicado ao Estudo de Ondas Eletromageneticas e foi desenvolvido por:")
print("igor de Araujo - RA: 22.223.006-2")
print("Gabriel Afonso - RA:22.223.001-3")
print("Gustavo Trovo - RA: 22.223.018-7")

while True: 
    print("--Menu Principal --")
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
