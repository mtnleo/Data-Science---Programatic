import math, functools as ft

def Ejercicio1(): 
    num = int(input("Escribi un numero: "))
    if (num > 0) :
        print("\nEs positivo")
    elif (num < 0):
        print("\nEs negativo")
    else:
        print("\nEs 0!")

def Ejercicio2():
    radio = int(input("Ingresa el radio: "))
    print(f"EL perimetro del radio {radio} es {radio * math.pi * 2}")
    print(f"EL area del radio {radio} es {(radio*radio) * math.pi}")

def Ejercicio3():
    parimpar = int(input("Ingresa un numero: "))
    if parimpar % 2 == 0:
        print("Es par!")
    else:
        print("Es impar!")

def Ejercicio4(socio1, socio2, socio3, socio4):
    total = socio1 + socio2 + socio3 + socio4
    print(f"El socio 1 tiene {socio1 * 100 / total}%")
    print(f"El socio 2 tiene {socio2 * 100 / total}%")
    print(f"El socio 3 tiene {socio3 * 100 / total}%")
    print(f"El socio 4 tiene {socio4 * 100 / total}%")

def Ejercicio5y6(rango):
    pares = 0
    impares = 0
    for i in range(rango):
        numerico = int(input("Escribi un numero: "))
        if esPar(numerico):
            print("Es par")
            pares += 1
        else:
            print("Es impar")
            impares += 1

    print(f"Hay {pares} pares y {impares} impares")        

def esPar(numero):
    return numero % 2 == 0

def Ejercicio7():
    mayor = 0
    menor = 0
    for i in range(10):
        num = int(input("Escriba un numero: "))
        if i == 0:
            mayor = num
        else:
            if num > mayor:
                mayor = num
            elif num < menor:
                menor = num

    print(f"El mayor numero fue {mayor}\nEl menor numero fue {menor}")

def Ejercicio8(cant_nums):
    lista_numeritos = [int(input("Escriba un numero: ")) for i in range(0, cant_nums)]
    print(f"Resultado de la multiplicacion de dichos numeros: {ft.reduce(lambda suma, num: suma * num, lista_numeritos)}")

def Ejercicio9():
    USUARIO = "TINI"
    CONTRASENIA = "GUOLIS123"

    usu_guess = input("Nombre: ")
    pass_guess = input("Password: ")

    if (USUARIO == usu_guess and CONTRASENIA == pass_guess):
        print("Bienvenidx!")
    else:
        print("Intente de nuevo!")
        if (USUARIO != usu_guess):
            print("Verificar usuario")
        if (CONTRASENIA != pass_guess):
            print("Verificar contrasenia")

def Ejercicio10():
    suma = 0
    num = -1
    while num != 0:
        num = int(input("Ingrese un numero (0 para salir): "))
        if (num != 0):
            suma += num

    print(f"La suma final es de {suma}")

def Ejercicio11():
    MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    ganancia_mensual = dict()
    facturacion_total = 0
    coste_total = 0
    gasto_mes = 0
    ingreso_mes = 0

    for mes in MESES:
        print(f"{mes}.")
        ingreso_mes = int(input("Ingreso: "))
        gasto_mes = int(input("Gasto: "))

        facturacion_total += ingreso_mes
        coste_total += gasto_mes
        ganancia_mensual.update({mes: ingreso_mes - gasto_mes}) 

    print("Facturacion anual: ", facturacion_total)
    print("Ganancia promedio = ", facturacion_total / 12)
    print("Ganancia mensual: ", ganancia_mensual)

def Ejercicio12():
    n1 = int(input("Ingrese un valor: "))
    n2 = int(input("Ingrese otro valor: "))
    op = input("Ingrese operacion a realizar (+, -, /, *): ")

    if (op == '+'):
        print(n1 + n2)
    elif (op == '-'):
        print(n1 - n2)
    elif (op == '*'):
        print(n1 * n2)
    elif (op == '/'):
        print(n1 / n2)
    else:
        print("Elija un operador valido!")

if __name__ == "__main__":
    # ir hardcoding q ejercicio se hace :)
    Ejercicio1()
