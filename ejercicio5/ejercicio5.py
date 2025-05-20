"""""Ejercicio #5: Búsqueda en una lista enlazada. Cree una función que busque un
valor específico en una lista enlazada. La función debe devolver la posición del valor
si se encuentra, o un mensaje indicando que el valor no está en la lista."""

import modulos as mo

if __name__ == "__main__":
    lista = mo.ListaEnlazada()
    
    while True:
        print("")
        print("ELIJA UNA OPCIÓN:")
        print("1) Insertar un nuevo valor al final de la lista")
        print("2) Buscar un valor en la lista y su posición")
        print("3) SALIR")
        opcion = input("Escribe una opción: ")
        print("")
        print("+-" * 25)

        match opcion:
            case "1":
                valor = input("Ingrese el nuevo valor para el final de la lista: ")
                lista.insertar(valor)
                print("Valor ingresado exitosamente.")
            case "2":
                valor = input("Ingrese el valor a buscar: ")
                posicion = lista.buscar(valor)
                if posicion != -1:
                    print(f"El valor fue encontrado en la posición #{posicion}.")
                else:
                    print("El valor no fue encontrado.")
            case "3":
                print("Adiós.")
                break
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")
        print("+-" * 25)