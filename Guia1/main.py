import math

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




if __name__ == "__main__":
    Ejercicio7()
