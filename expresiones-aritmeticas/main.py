from auxiliar import tokenizar, a_postfix, evaluar_postfix, imprimir_postfix, validar_postfix, formatear_float

# Main
if __name__ == "__main__":
  # Loop infinito
  while True:
    # Imprimir Menú
    print(
"""
========================================================
  __             __                  __   __   __      
 /  `  /\\  |    /  ` |  | |     /\\  |  \\ /  \\ |__)  /\\ 
 \\__, /~~\\ |___ \\__, \\__/ |___ /~~\\ |__/ \\__/ |  \\ /~~\\

========================================================
  
  Que acción desea realizar?
  1. Convertir de Infijo a Postfijo
  2. Evaluar Expresión Numérica
  3. <- Salir
"""
    )
    
    # Usamos el try catch por si acaso hay un error
    try:
      # Conseguimos el input
      opcion = int(input("> "))
    except:
      print("El input debe ser un número entero!")
    
    # Ciclamos por las opciones
    if opcion == 1 or opcion == 2:
      if opcion == 1:
        print("\nIngresa la expresión a convertir a Postfija (variables y números)")
      elif opcion == 2:
        print("\nIngresa la expresión numérica a evaluar (solo números)")
      # Conseguimos el input
      expresion = input("> ")
      # Linea nueva
      print()
      # Lo tokenizamos
      tokens = tokenizar(expresion)
      # Checamos que no haya habido ningun error
      if tokens is None:
        print("Hubo un error durante la tokenización")
        input("Presiona enter para continuar...") 
        continue
      # Lo convertimos a postfijo
      try:
        postfix = a_postfix(tokens)
      except Exception as ex:
        print(f"Hubo un problema: {ex}")
        input("Presiona enter para continuar...") 
        continue


      # Validamos el postfix
      if not validar_postfix(postfix):
        print("La expresión no es válida!")
        input("Presiona enter para continuar...") 
        continue
      
      # Imprimimos el postfix
      print("Expresión a Postfix: ")
      imprimir_postfix(postfix)
      # Dos lineas nuevas
      print("\n")

      if opcion == 2:
        # Ahora lo evaluamos
        try:
          evaluado = evaluar_postfix(postfix)
          # Imprimimos el resultado
          print(f"El resultado de la expresión es: {formatear_float(evaluado)}")
        except Exception as ex:
          print(f"Hubo un problema: {ex}")

      input("Presiona enter para continuar...") 
    elif opcion == 3:
      break
