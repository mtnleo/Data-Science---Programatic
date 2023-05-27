class Pila:

    def __init__(self):
        self.pila = []

    def Apilar(self, dato):
        self.pila.append(dato)

    def Desapilar(self):
        if not self.esta_vacia():
            return self.pila.pop()
        else:
            return None
        
    def esta_vacia(self):
        return False if len(self.pila) > 0 else True
    
    def mostrar_pila(self):
        for elemento in self.pila:
            print(elemento)
