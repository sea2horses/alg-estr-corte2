#Ejercicio #4: Implementación de una cola de prioridad. Diseñe una cola de
#prioridad donde los elementos se desencolan según su prioridad. Cada elemento
#tendrá un nombre y una prioridad (un número entero, donde un número menor indica
#mayor prioridad).

class Nodo:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad
        self.siguiente = None
class ColaPrioridad:
    def __init__(self):
        self.frente = None

    def insertar(self, nombre, prioridad):
        nuevo = Nodo(nombre, prioridad)
        if self.frente is None or self.frente.prioridad > prioridad:
            nuevo.siguiente = self.frente
            self.frente = nuevo
        else:
            actual = self.frente
            while actual.siguiente is not None and actual.siguiente.prioridad <= prioridad:
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
            
    def eliminar(self):
        if self.frente is None:
            print("La cola está vacía")
            return None
        viejo_frente = self.frente
        self.frente = self.frente.siguiente
        return viejo_frente.nombre, viejo_frente.prioridad 
    def imprimir(self):
        if self.frente is None:
            print("La cola está vacía")
            return
        actual = self.frente
        while actual is not None:
            print(f"Nombre: {actual.nombre}, Prioridad: {actual.prioridad}", end=" -> ")
            actual = actual.siguiente
        print("None")






