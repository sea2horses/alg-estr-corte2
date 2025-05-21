from clases import Token, TipoToken, Cola, Pila

# Formatear float, para que 3.0 se vuelva 3 y 3.1400 se vuelva 3.14
def formatear_float(x):
  if isinstance(x, float):
    if x == int(x):
      return str(int(x))
    else:
      return str(x).rstrip('0')
  else:
    return x

# Precedencia de los operadores, tambien usado para verificar
# que operadores existen
def precedencia(operador) -> int:
  match operador:
    case '^':
      return 5
    case '*' | '/' | '%':
      return 4
    case '+' | '-' | '–':
      return 3
    case _:
      return -1

# Tokenización del input para trabajar con tokens y no texto
def tokenizar(source: str) -> Cola:
  # Creamos la cola de tokens
  tokens = Cola()

  # Posición en la expresión
  posicion = 0
  
  # Mientras estemos en el string
  while posicion < len(source):
    # Si es un espacio
    if source[posicion].isspace():
      # Nos lo saltamos
      posicion += 1
    # Si es una letra
    elif source[posicion].isalpha():
      # Creamos un nuevo token de variable
      nuevo_token = Token(TipoToken.VARIABLE, source[posicion])
      # Pusheamos el token
      tokens.push(nuevo_token)
      # Incrementamos la posición
      posicion += 1
    # Si es un número
    elif source[posicion].isnumeric():
      # Tenemos que leer el número completo
      string_numero = ""
      # Mientras sea un número o punto (soporte para decimales)
      while source[posicion].isnumeric() or source[posicion] == '.':
        # Agregamos el caracter
        string_numero += source[posicion]
        # Aumentamos la posición
        posicion += 1
        # Si la posición esta fuera de rango, rompemos el loop
        if posicion >= len(source):
          break
      # Creamos un nuevo token de número
      try:
        nuevo_token = Token(TipoToken.NUMERO, float(string_numero))
        # Pusheamos
        tokens.push(nuevo_token)
      except:
        print(f"Error, número invalido: '{string_numero}'")
        return None
    # Si es un caracter cualquiera
    else:
      # Determinaremos el tipo del token
      tipo: TipoToken = None

      # Dependiendo del caracter, asignamos un tipo
      if source[posicion] == '(':
        tipo = TipoToken.ABRIR_PARENTESIS
      elif source[posicion] == ')':
        tipo = TipoToken.CERRAR_PARENTESIS 
      elif precedencia(source[posicion]) != -1:
        tipo = TipoToken.OPERADOR
      # Si no encontramos ninguno, muerte al programa
      if tipo == None:
        print(f"Caracter no reconocido: '{source[posicion]}'")
        # Muerte
        return None
      # Pusheamos como operador
      nuevo_token = Token(tipo, source[posicion]) 
      # Pusheamos
      tokens.push(nuevo_token) 
      # Incrementamos la posición
      posicion += 1
  # Retornamos los tokens conseguidos
  return tokens

# Convierte tokens a postfix
def a_postfix(tokens: Cola, anidado = 0) -> Cola: 
  # Creamos la cola de postfix
  cola_total = Cola()
  pila_operadores = Pila()
  # Variable para identificar la rama principal (ayuda al control de parentesis)
  parentesis_cerrado = False
  # Ultimo tipo (para que no hayan dos operadores o operandos seguidos)
  ultimo_tipo = None

  while tokens.length() > 0:
    token_actual: Token = tokens.pop()
    
    # Dependiendo del tipo de token, hacemos cosas distintas
    match token_actual.Tipo:
      # Si abrimos parentesis usamos recursión
      case TipoToken.ABRIR_PARENTESIS:
        # Si hay un parentesis de apertura llamamos la función recursivamente
        cola_total.push_cola(a_postfix(tokens, anidado + 1))
      case TipoToken.CERRAR_PARENTESIS:
        # Comprobamos que no estemos en anidado 0 (parentesis de cierre de sobra)
        if anidado == 0:
          raise Exception("Parentesis de Cierre extra")
        # Si hay un parentesis de cierre cerramos el estadio y denotamos que no es la rama principal
        parentesis_cerrado = True
        break
      case TipoToken.VARIABLE | TipoToken.NUMERO:
        # No pueden haber dos operandos seguidos
        if ultimo_tipo == TipoToken.VARIABLE or ultimo_tipo == TipoToken.NUMERO:
          raise Exception("La expresión no es válida! (2 operandos seguidos)")
        # Los operandos los metemos a la cola actual
        cola_total.push(token_actual)
      case TipoToken.OPERADOR:
        # No pueden haber dos operadores seguidos
        if ultimo_tipo == TipoToken.OPERADOR:
          raise Exception("La expresión no es válida! (2 operadores seguidos)")
        # Obtenemos la precedencia del operador
        precedencia_actual = precedencia(token_actual.Valor)
        # Mientras no encontremos un operador con menor precedencia que el actual
        while pila_operadores.length() > 0 and precedencia(pila_operadores.peek().Valor) >= precedencia_actual:
          # Vaciamos la pila
          cola_total.push(pila_operadores.pop())
        # Metemos el nuevo operador a la pila
        pila_operadores.push(token_actual)
      
    # Actualizamos el ultimo tipo
    ultimo_tipo = token_actual.Tipo
  
  if anidado > 0 and parentesis_cerrado == False and tokens.length() == 0:
    raise Exception("Más parentesis de apertura que de cierre")
    
  # Ahora vaciamos la pila de operadores a la cola total
  while pila_operadores.length() > 0:
    cola_total.push(pila_operadores.pop())
    
  # Retornamos la cola total
  return cola_total

def imprimir_postfix(postfix: Cola):
  # Creamos una copia de la cola original
  copia = postfix.copy()
  # Ahora vamos imprimiendo el valor de cada token
  while copia.length() > 0:
    # Tenemos que sacar el valor porque
    # el postfix almacena tokens
    token: Token = copia.pop()
    # Imprimimos el valor
    print(formatear_float(token.Valor), end=" ")

# Función para validar la expresión sin evaluar
def validar_postfix(postfix: Cola) -> bool:
  pila = Pila()
  # Hacemos una copia para no modificar el original
  copia_postfix = postfix.copy()
  
  while copia_postfix.length() > 0:
    token = copia_postfix.pop()
    if token.Tipo == TipoToken.NUMERO or token.Tipo == TipoToken.VARIABLE:
      pila.push(token)
    elif token.Tipo == TipoToken.OPERADOR:
      if pila.length() < 2:
        # No hay suficientes operandos
        return False
      operando2: Token = pila.pop()
      operando1: Token = pila.pop()
      
      pila.push(Token(TipoToken.NUMERO, 0))
    else:
      # Token desconocido
      return False
  # Al final debe haber exactamente un resultado
  return pila.length() == 1

def evaluar_postfix(postfix: Cola):
  # Creamos la pila
  pila_postfix = Pila()
  
  while postfix.length() > 0:
    # Sacamos el token actual
    token_actual: Token = postfix.pop()

    # Checamos si es numero u operador
    if token_actual.Tipo == TipoToken.NUMERO:
      # Pila postfix
      pila_postfix.push(token_actual)
    # Si es un operador
    elif token_actual.Tipo == TipoToken.OPERADOR:
      # Vemos si hay mas de 2 elementos en la pila postfix
      if pila_postfix.length() < 2:
        continue
      # Sacamos los ultimos dos elementos
      operando2: Token = pila_postfix.pop()
      operando1: Token = pila_postfix.pop()
      # Vamos a sacar el nuevo numero
      nuevo_numero = None
      # Prix operemos
      match token_actual.Valor:
        case '+': nuevo_numero = operando1.Valor + operando2.Valor
        case '-' | '–': nuevo_numero = operando1.Valor - operando2.Valor
        case '*': nuevo_numero = operando1.Valor * operando2.Valor
        case '/': nuevo_numero = operando1.Valor / operando2.Valor
        case '%': nuevo_numero = operando1.Valor % operando2.Valor
        case '^': nuevo_numero = operando1.Valor ** operando2.Valor
        case _: raise Exception(f"Operador no manejado en el match: {token_actual.Valor}")
      # Subimos el numero a la pila
      pila_postfix.push(Token(TipoToken.NUMERO, nuevo_numero))
    # Si es una variable
    elif token_actual.Tipo == TipoToken.VARIABLE:
      raise Exception("No se permiten variables en evaluación directaa")
  
  # Al final, solo debe haber un token en la pila postfix
  if pila_postfix.length() == 1:
    return pila_postfix.pop().Valor
  else:
    raise Exception("Error: La expresión no es válida!") 