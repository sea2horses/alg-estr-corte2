from clases import Pila

# Esta función toma las palabras de un string y las pasa a una pila
def palabras_a_pila(src: str) -> Pila:
  # posicion en el string
  posicion = 0
  
  # Variable para la palabra actual
  palabra_actual = ""

  # Pila de palabras
  pila_palabras = Pila()

  # While para recorrer el string
  while posicion < src.__len__():
    # Si es un espacio
    if src[posicion].isspace():
      # Revisamos si llevamos una palabra recolectada
      if palabra_actual != "":
        # Pusheamis
        pila_palabras.push(palabra_actual)
        palabra_actual = ""
    else:
      # Agregamos el caracter a la palabra recolectada
      palabra_actual += src[posicion]
    # Continuamos
    posicion += 1
  
  # Si quedo una palabra la pusheamos
  pila_palabras.push(palabra_actual)
  
  # Retornamos la pila
  return pila_palabras