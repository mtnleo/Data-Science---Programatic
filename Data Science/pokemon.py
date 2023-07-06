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

        case 3:
            print("Cuántos pokemones tienen un 'Sp. Def' de 25 o menos?")
            print("Hay", df.loc[df["Sp. Def"] <= 25].shape[0], "con un Sp. Def de 25 o menos")
            print("Algunos de ellos: ")
            print(df.loc[df["Sp. Def"] <= 25])

        case 4:
            print("Seleccionar todos los pokemones legendarios (Legendary)")
            print("Hay", df.loc[df["Legendary"]].shape[0], "pokemones legendarios en el dataframe.")
            print("Algunos de ellos son:\n ", df.loc[df["Legendary"]])

        case 5:
            print("Encontrar el outlier raro: VER")    
            # don't have the picture lol

        case 6:
            print("Cuántos pokemones de tipo Fire y Flying hay?")   
            df_fire_flying = df.loc[(df['Type 1'] == 'Fire') & (df['Type 2'] == 'Flying')]
            print("Hay", df_fire_flying.shape[0], "de pokemones tipo fuego y volador.")
            print("Algunos de ellos:\n", df_fire_flying)

        case 7:
            print("Cuántos pokemones 'Poison' hay entre ambos tipos?")
            df_poison = df.loc[(df["Type 1"] == "Poison") | (df["Type 2"] == "Poison")]
            print("Hay", df_poison.shape[0], "Pokemones de tipo Veneno.")
            print("Son estos:\n", df_poison.to_string())

        case 8:
            print("Qué pokemon de tipo 1 'Ice' tiene la mejor defensa?") 
            df_ice = df.loc[df["Type 1"] == "Ice"].sort_values(by="Defense", ascending=False)
            print("Es este:\n", df_ice.iloc[0].to_string())



        
        case _:
            print("Seleccione una opcion adecuada")
    
    