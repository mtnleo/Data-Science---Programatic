from pila import Pila

if __name__ == "__main__":
    pilita = Pila()

    pilita.Apilar("Los Arrayanes")
    pilita.Apilar("Los Glaciares")
    pilita.Apilar("Nahuel Huapi")
    pilita.Apilar("Los Alerces")
    pilita.Apilar("Iguazú")

    pilita.Desapilar()

    pilita.mostrar_pila()