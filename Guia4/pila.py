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
        return True if len(self.pila) else False
    
    def mostrar_pila(self):
        for elemento in self.pila:
            print(elemento)
