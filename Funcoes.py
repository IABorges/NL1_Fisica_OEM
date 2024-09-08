import FuncoesMath

def showDevs():
    print("")
    print("----Desenvolvedores---")
    print("igor de Araujo - RA:")
    print("Gabriel Afonso - RA:")
    print("Gustavo Trovo - RA:")
    print("")

def showOp():
    while True: 
        print("--Menu de Exercicios--")
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
            FuncoesMath.opFrequencia()
        elif i == 2:
            break
        else:
            print("Opação invalida")
