import random

def tirar_dados():
    p1 = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    p2 = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]

    return p1, p2

def check_dados_PC(pc):
    i = 0
    for dado in pc:
        if dado < 3:
            dado = random.randint(1, 6)
            pc[i] = dado
            break
        i+=1

    return pc    

def sumar_dados(dados):
    cont = 0
    for dado in dados:
        cont += dado

    return cont

if __name__ == "__main__":
    
    p1, pc = tirar_dados()

    print("Dados antes de relanzar: ")
    print("Dados Player 1 -> ", p1, " = ", sumar_dados(p1))
    print("Dados PC       -> ", pc, " = ", sumar_dados(pc))

    pc = check_dados_PC(pc)

    relanzar = 5

    while (relanzar < 0 or relanzar > 3):

        relanzar = int(input("Si quiere relanzar, seleccione el dado (del 1 al 3 | escoja 0 para quedarse con los dados actuales): "))
        if relanzar > 0 and relanzar < 4:
            p1[relanzar - 1] = random.randint(1, 6)
        elif relanzar != 0:
            print("Opcion invalida, intente de nuevo")

    
    print("Dados luego de relanzar: ")
    print("Dados Player 1 -> ", p1, " = ", sumar_dados(p1))
    print("Dados PC       -> ", pc, " = ", sumar_dados(pc))

    if (sumar_dados(p1) > sumar_dados(pc)):
        print("El ganador es Player 1")
    elif (sumar_dados(p1) < sumar_dados(pc)):
        print("El ganador es PC")
    else:    
        print("Empate!")
