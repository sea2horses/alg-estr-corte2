from clases import Pila
from auxiliar import palabras_a_pila

if __name__ == "__main__":
  # Vamos a usar una pila ya que LIFO nos sirve para reversar una lista
  # Imprimimos el mensaje para el usuario
  print("Eliga una operación para invertir")
  # Guardamos la oración 
  oracion = input("> ")
  # Convertimos las palabras a pila
  pila = palabras_a_pila(oracion)
  # Ahora va a ir saliendo el último elemento que entró, asi que
  # las palabras saldrán en orden inverso
  print("\nOración al revés:")
  while pila.length() > 0:
    # Imprimimos cada palabra que salga
    print(pila.pop(), end=" ")
  # Terminado.