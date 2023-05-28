if __name__ == "__main__":
    # LISTAS

    #1
    frutas = ["manzana", "banana", "naranja", "pera"]
    #print(frutas)
    #2
    #print(frutas[1])
    #3
    frutas[0] = "Cereza"
    # 4
    frutas.append("Sandia")
    #5
    frutas.remove("naranja")
    #6
    numeros = [1, 2, 3, 4, 5]
    #for num in numeros:
    #    print(num)
    #7
    pares = [x for x in range(1,11) if x % 2 == 0]
    pares.sort()
    #print(pares)
    #8
    cuadrados = [x*x for x in range(1,5)]
    #print(cuadrados)
    #9
    nombres = ["Seba", "Martin", "Felipe", "Malena", "Toto"]
    #usu = input("Escribi un nombre: ")
    #print(usu, "esta en la lista?", usu in nombres)
    #10
    numeros = [i for i in range(0,10)]
    num1 = numeros[:3]
    num2 = numeros[4:7]
    num3 = numeros[8:]
    
    # DICTS

    #1
    alumno = {"nombre": "Martin",
              "Edad": 19,
              "Carrera": "TUP"}
    #2
    alumno["Edad"] = 20
    #3
    alumno.update({"Universidad": "UTN"})
    #print(alumno)
    #4
    calificaciones = {"Matematica": 9,
                      "Fisica": 8,
                      "Quimica": 6}
    #5
    calificaciones.pop("Quimica")
    #print(calificaciones)
    #6
    keys = list(calificaciones.keys())
    #print(keys)
    #7
    agenda = {"Contacto1": {"Nombre": "Martin", "Telefono": 233838238, "email": "mtnleonardi@gmail.com"}, "Contacto2": {"Nombre": "Herni", "Telefono": 233812238, "email": "herni@gmail.com"}, "Contacto3": {"Nombre": "LongT", "Telefono": 123838238, "email": "longtinti@gmail.com"}}
    #print(agenda)
    

    # TUPLAS

    #1
    meses = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    #2
    #print(meses[2])
    #3
    #print(meses[-1])
    #4
    #las tuplas son inmutables, por eso el error
    #5
    meses_ficticios = ("Apolo", "Jupiter")
    tupla_concat = meses + meses_ficticios
    #6
    coords = (1, 2, 3)
    x, y, z = coords
    #7
    alumnes = ("Martin", 19, "Malena", 24, "Felipe", 21)


    # SETS

    #1
    frutas = {"manzana", "banana", "naranja", "pera"}
    #2
    frutas1 = {"manzana", "banana", "pera"}
    frutas2 = {"naranja", "sandia"}
    #print(frutas1.union(frutas2))
    #print(frutas1.difference(frutas2))
    #print(frutas1.intersection(frutas2))
    #3
    numeros = {1, 2, 3, 4, 5}
    numeros.add(6)
    numeros.remove(2)
    #print(numeros)
    #4
    vocales = {'a', 'b', 'c', 'd', 'e'}
    #comp = input("Escribe una letra: ")
    #print("Es vocal:", comp in vocales)
    #5
    numeros_repetidos = [12, 12, 12, 13, 13, 15]
    numeros_repetidos_set = set(numeros_repetidos)
    #6
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    #print(set1.symmetric_difference(set2))
    #print(set1 in set2)
    #print(set2 in set1)
    #7
    set_a = {1, 2, 3}
    set_b = {2, 3}
    set_c = set_a.difference(set_b)
    print(set_c)


