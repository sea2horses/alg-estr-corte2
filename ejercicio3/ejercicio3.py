"""""Ejercicio #3: Simulación de una lista de reproducción de música. Implemente
una lista de reproducción de música utilizando una lista enlazada. El programa debe
permitir agregar canciones, eliminar canciones, reproducir la siguiente canción,
reproducir la canción anterior y mostrar la lista de reproducción actual."""

import modulos as mo

global cancionActual
cancionActual = -1

if __name__ == "__main__":
    lista = mo.ListaEnlazada()
    
    while True:
        print("")
        print("ELIJA UNA OPCIÓN:")
        print("1) Agregue una canción")
        print("2) Elimine una canción")
        print("3) Reproducir una canción")
        print("4) Lista de reproducción actual")
        print("5) Reproducir la canción anterior")
        print("6) Reproducir la siguiente canción")
        print("7) SALIR")
        opcion = input("Escribe una opción: ")
        print("")
        print("+-" * 25)

        match opcion:
            case "1":
                valor = input("Ingrese el nombre de la canción a agregar: ")
                lista.insertar(valor)
                print("Canción agregada exitosamente.")
            case "2":
                valor = input("Ingrese el nombre de la canción a eliminar: ")
                if lista.eliminar(valor):
                    print("La canción fue eliminado exitosamente de la lista de reproducción.")
                else:
                    print("La canción no fue encontrada.")
            case "3":
                valor = input("Ingrese la canción a reproducir: ")
                posicion = lista.buscar(valor)
                if posicion != -1:
                    cancionActual = posicion
                    print(f"¡Ahora estás escuchando '{valor}'!")
                else:
                    print("La canción no fue encontrada.")
            case "4":
                lista.imprimir()
            case "5":
                if cancionActual > 0:
                    cancionActual -= 1
                    actual = lista.cabeza
                    for i in range(cancionActual):
                        actual = actual.siguiente
                    print(f"Reproduciendo canción anterior: {actual.valor}")
                else:
                    print("No hay canción anterior para reproducir.")
            case "6":
                longitud = 0
                temp = lista.cabeza
                while temp:
                    longitud += 1
                    temp = temp.siguiente

                if cancionActual < longitud - 1:
                    cancionActual += 1
                    actual = lista.cabeza
                    for i in range(cancionActual):
                        actual = actual.siguiente
                    print(f"Reproduciendo canción siguiente: {actual.valor}")
                else:
                    print("No hay canción siguiente para reproducir.")
            case "7":
                print("Adiós.")
                break
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")
        print("+-" * 25)