#Ejemplificando la creación de una lista enlazada simple

# Clase Nodo - representa un nodo de la lista
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Clase ListaEnlazada - gestiona la lista y sus operaciones
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Insertar un nuevo valor al final de la lista
    def insertar(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    # Eliminar el primer nodo que contenga el valor
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente

        return False

    # Buscar un valor en la lista
    def buscar(self, valor):
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.valor == valor:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1

    # Imprimir los valores de la lista
    def imprimir(self):
        actual = self.cabeza
        if not actual:
            print("La lista está vacía.")
            return
        print("Lista:", end=" ")
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    # Insertar al inicio de la lista
    def insertarInicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    # Contar la cantidad de nodos en la lista
    def longitudLista(self):
        actual = self.cabeza
        cantidad = 0
        while actual:
            cantidad += 1
            actual = actual.siguiente
        print(f"Hay {cantidad} nodos en la lista.")

    # Determinar si la lista está vacía
    def determinar(self):
        if not self.cabeza:
            print("La lista está vacía.")
        else:
            print("La lista no está vacía.")

    # Imprimir el último valor
    def buscarUltimo(self):
        if not self.cabeza:
            print("La lista está vacía.")
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        print(f"El último valor es: {actual.valor}")