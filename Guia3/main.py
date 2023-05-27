import random as rd
import os

def saludo(): # 1
    print("Hola!")

def saludo2(nombre): # 2
    print("Hola", nombre + "!")

def suma(n1, n2): # 3
    return n1 + n2

def saludo_personalizado(nombre, saludo="Hola!"): # 4
    print(saludo, nombre)

def promedio(*nums): # 5
    suma = 0
    for num in nums:
        suma += num
    return suma / len(nums)
    
def factorial (num): # 6
    if num > 1:
        num = num * factorial(num- 1)
    return num

def ordenar_lista(lista): # 7
    lista.sort()

def dividir(n1, n2): # 8
    try:
        return n1 / n2
    except:
        print("No se puede dividir por 0!")
        return None
    
def informacion_persona(nombre, edad, pais): # 9
    print("Nombre:", nombre, ", Edad:", edad, ", Pais:", pais)

# 10 es el de dividir repetido*

def concatenar_strings(*strings): # 11
    rtn = ""
    for str in strings:
        rtn = rtn + str

    return rtn

def eliminar_duplicados(lista): # 12
    lista_set = set(lista)
    return list(lista_set)

def fibonacci(num_final, i=1): # 13 (BY CHAT-GPT)
    if num_final <= 0:
        return []
    elif num_final == 1:
        return [0]
    elif num_final == 2:
        return [0, 1]
    else:
        sequence = fibonacci(num_final - 1)
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
        return sequence


def generar_numero_aleatorio(min, max):
    return rd.randint(min, max)

def contar_lineas(PATH):
    try:
        with open(PATH, "r") as file:
            suma = 0
            for linea in file:
                suma += 1
            return suma
    except FileNotFoundError:
        print("El archivo no fue encontrado en la ruta especificada.")
        return 0
    except IOError as e:
        print("Error al abrir el archivo:", str(e))
        return 0
    
def calcular_estadisticas(tup):
    suma = 0
    mayor = tup[0]
    for num in tup:
        suma += num
        if mayor < num:
            mayor = num

    return suma, suma / len(tup), mayor

###############

if __name__ == "__main__":
    print("Factorail de 5!", factorial(5))
    lista = [3, 9, 1, 4, 2, 4, 0, 8]
    print(lista)
    ordenar_lista(lista)
    print(lista)

    print(dividir(10, 5))
    print(dividir(10, 0))

    informacion_persona("Martin", 19, "Argentina")
    print(concatenar_strings("Hola", "me", "llamo", "Martin"))

    print(eliminar_duplicados([2, 5, 4, 5, 2, 5, 5, 5, 3, 7, 5, 7]))

    print("Fib's 9: ", fibonacci(num_final=9))

    print(generar_numero_aleatorio(1, 12))

    print("Suma/Promedio/Mayor:", calcular_estadisticas((10, 23, 29, 15)))

    

