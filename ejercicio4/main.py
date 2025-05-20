from ejercicio4 import ColaPrioridad
while True:
    if __name__ == "__main__":
        cola = ColaPrioridad()
    while True:
        print("\nOpciones:")
        print("1. Insertar elemento")
        print("2. Desencolar elemento")
        print("3. Imprimir cola")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nombre = input("Ingrese el nombre del elemento: ")
            prioridad = int(input("Ingrese la prioridad (menor número indica mayor prioridad): "))
            cola.insertar(nombre, prioridad)
        elif opcion == '2':
            nombre, prioridad = cola.eliminar()
            if nombre is not None:
                print(f"Elemento desencolado: Nombre: {nombre}, Prioridad: {prioridad}")
        elif opcion == '3':
            cola.imprimir()
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

