import FuncoesMath

def showDevs():
    print("")
    print("----Desenvolvedores---")
    print("igor de Araujo - RA: 22.223.006-2")
    print("Gabriel Afonso - RA:")
    print("Gustavo Trovo - RA:")
    print("")

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
            FuncoesMath.opFrequencia()
        elif i == 2:
            FuncoesMath.opCompOnda()
        elif i == 3:
            FuncoesMath.opNumOnda()
        elif i == 4:
            FuncoesMath.opFreAng()
        elif i == 5:
            FuncoesMath.opCampMag()
        else:
            print("Opação invalida")
