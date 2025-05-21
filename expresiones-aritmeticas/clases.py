# En este archivo van las clases necesarias para el funcionamiento del programa

# Primero queremos importar un enumerador para ayudarnos con los tokens
from enum import Enum

# Ahora creamos una clase TokenType o TipoToken que hereda la clase Enum
class TipoToken(Enum):
  NUMERO = 0,
  VARIABLE = 1,
  OPERADOR = 2,
  ABRIR_PARENTESIS = 3,
  CERRAR_PARENTESIS = 4
  
# Ahora creamos la clase Token
class Token:
  # Constructor
  def __init__(self, tipo: TipoToken, valor):
    self.Tipo = tipo
    self.Valor = valor
  
  # ToString
  def __str__(self):
    return f"<'{self.Valor}'>"
  
  # Representación (para que se imprima en el print)
  def __repr__(self):
    return self.__str__()
 
# Ahora queremos las definiciones de pila y cola

# Para eso primero queremos la clase nodo
class Nodo:
  # Constructor
  def __init__(self, valor, siguiente = None):
    self.Valor = valor
    self.Siguiente = siguiente

# Ahora construimos la clase pila
class Pila:
  # Constructor
  def __init__(self):
    self.Cabeza: Nodo = None
  
  # Agregar
  def push(self, valor):
    # Creamos un nuevo nodo
    nuevo_nodo = Nodo(valor)
    
    # Si no hay cabeza, asignamos la cabeza al nuevo nodo
    if self.Cabeza == None:
      self.Cabeza = nuevo_nodo
    # Si hay
    else:
      # Guardamos la vieja cabeza
      vieja_cabeza = self.Cabeza
      # Asignamos la cabeza al nuevo nodo
      self.Cabeza = nuevo_nodo
      # El siguiente nodo de la nueva cabeza va a ser la vieja cabeza
      nuevo_nodo.Siguiente = vieja_cabeza
  
  # Eliminar
  def pop(self):
    # Si no hay cabeza
    if self.Cabeza == None:
      raise Exception("illegal pop in stack")
    else:
      # Guardamos la vieja cabeza
      vieja_cabeza = self.Cabeza
      # Asignamos la cabeza a ser el nodo siguiente
      self.Cabeza = vieja_cabeza.Siguiente
      # Eliminamos el siguiente de la vieja cabeza
      vieja_cabeza.Siguiente = None
      # Retornamos el valor de la vieja cabeza
      return vieja_cabeza.Valor
  
  # Peek
  def peek(self):
    # Solo retornamos el valor cabeza
    return self.Cabeza.Valor
  
  # Tamaño
  def length(self):
    # Boom
    i = 0
    # Preparamos el nodo actual
    nodo_actual = self.Cabeza
    # Mientras el nodo actual no sea none, vamos
    while nodo_actual != None:
      # Sumamos 1
      i += 1
      # El nodo actual va a ser el siguiente
      nodo_actual = nodo_actual.Siguiente
    # Retornamos
    return i
  
  # Imprimir
  def print(self):
    valores = []
    # Nodo actual
    nodo_actual = self.Cabeza
    # Mientras el nodo actual sea válido
    while nodo_actual != None:
      # Pusheamos al arreglo al principio
      valores.insert(0,nodo_actual.Valor)
      # Actualizamos el nodo actual
      nodo_actual = nodo_actual.Siguiente
    # Printeamos el arreglo
    print(valores)

# Ahora construimos la clase cola
class Cola:
  # Constructor
  def __init__(self):
    self.Cabeza: Nodo = None
    self.Cola: Nodo = None
  
  # Agregar
  def push(self, valor):
    # Creamos un nuevo nodo
    nuevo_nodo = Nodo(valor)
    
    # Si no hay cabeza, asignamos la cabeza al nuevo nodo
    if self.Cabeza == None:
      self.Cabeza = self.Cola = nuevo_nodo
    # Si hay
    else:
      # Conseguimos la vieja cola
      vieja_cola = self.Cola
      # Asignamos la cola al nuevo nodo
      self.Cola = nuevo_nodo
      # Le asignamos siguiente a la vieja cola
      vieja_cola.Siguiente = nuevo_nodo
  
  # Agregar una Cola (función especial)
  def push_cola(self, cola: 'Cola'):
    # Vayamos obteniendo cada valor
    while cola.length() > 0:
      # Popeamos la cola y pusheamos a self
      self.push(cola.pop())
  
  # Eliminar
  def pop(self):
    # Si no hay cabeza
    if self.Cabeza == None:
      raise Exception("illegal pop in queue")
    else:
      # Guardamos la vieja cabeza
      vieja_cabeza = self.Cabeza
      # Asignamos la cabeza a ser el nodo siguiente
      self.Cabeza = vieja_cabeza.Siguiente
      # Eliminamos el siguiente de la vieja cabeza
      vieja_cabeza.Siguiente = None
      # Miramos si la cola quedo vacía
      if self.Cabeza == None:
        self.Cola = None
      # Retornamos el valor de la vieja cabeza
      return vieja_cabeza.Valor
  
  # Peek
  def peek(self):
    # Solo retornamos el valor cabeza
    return self.Cabeza.Valor
  
  # Cola
  def tail(self):
    return self.Cola
  
  # Tamaño
  def length(self):
    # Boom
    i = 0
    # Preparamos el nodo actual
    nodo_actual = self.Cabeza
    # Mientras el nodo actual no sea none, vamos
    while nodo_actual != None:
      # Sumamos 1
      i += 1
      # El nodo actual va a ser el siguiente
      nodo_actual = nodo_actual.Siguiente
    # Retornamos
    return i
    
  # Imprimir
  def print(self):
    valores = []
    # Nodo actual
    nodo_actual = self.Cabeza
    # Mientras el nodo actual sea válido
    while nodo_actual != None:
      # Pusheamos al arreglo al principio
      valores.append(nodo_actual.Valor)
      # Nodo actual actualizamos
      nodo_actual = nodo_actual.Siguiente
    # Printeamos el arreglo
    print(valores)