from Ejercicio2 import Ejercicio2

if __name__ == "__main__":
    ejercicio2 = Ejercicio2()
while True:
    print(" ")
    print("\nOpciones:")
    print("1. Verificar paréntesis")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        cadena = input("Ingrese la cadena de texto ([], {}, () ): ")
        balenceado, mensaje = ejercicio2.verificar_parentesis(cadena)
        print(mensaje)
    elif opcion == '2':
        break
    else:
        print("Opción no válida. Intente de nuevo.")