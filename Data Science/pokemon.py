import pandas as pd
import matplotlib.pyplot as plt

PATH = "CSVs\pokemon.csv"

#1. Cuántos pokemones existen con un valor de Attack mayor a 150?
#2. Seleccionar todos los pokemones con una Speed de 10 o menos
#3. Cuántos pokemones tienen un "Sp. Def" de 25 o menos?
#4. Seleccionar todos los pokemones legendarios (Legendary)
#5. Encontrar el outlier raro: VER
#6. Cuántos pokemones de tipo Fire y Flying hay?
#7. Cuántos pokemones "Poison" hay entre ambos tipos?
#8.Qué pokemon de tipo 1 "Ice" tiene la mejor defensa?
#9. Cuál es el tipo más común de los pokemones legendarios?
#10. Cuál es el pokemon mas poderoso de las primeras 3 generaciones, de tipo "water"
#11. Cuál es el Dragón mas poderoso de las últimas 2 generaciones?
#12. Seleccionar los pokemones mas poderosos de tipo Fire
#13. Seleccionar todos los pokemones de tipo Water y Flying
#14. Seleccionar columnas específicas de pokemones legendarios de tipo Fire: Name, Attack, Generation
#15. Seleccionar los pokemones mas lentos y mas rápidos: VER

if __name__ == "__main__":
    #obtener el dataframe
    df = pd.read_csv(PATH)


    eleccion = int(input("Escriba el ejercicio que quiere ver: "))
  

    match eleccion:
        case 1:
            print("Cuántos pokemones existen con un valor de Attack mayor a 150?")
            print(df.loc[df["Attack"] > 150].shape[0])

        case 2:
            print("Seleccionar todos los pokemones con una Speed de 10 o menos")
            print("Hay ", df.loc[df["Speed"] <= 10].shape[0], " pokemones con esas caracteristicas:")
            print(df.loc[df["Speed"] <= 10])
        
        case _:
            print("Seleccione una opcion adecuada")
    
    