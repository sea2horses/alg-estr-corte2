#Ejercicio #2: Verificación de paréntesis balanceados. Escriba un programa que
#determine si una cadena de texto dada tiene los paréntesis ( ), { }, y [ ] balanceados.
#Use una pila para realizar el seguimiento de los paréntesis abiertos.


from auxiliar import Pila  # Usa tu clase Pila definida con nodos

class Ejercicio2:
    def verificar_parentesis(self, cadena):
        pila = Pila()
        pares = {')': '(', ']': '[', '}': '{'}
        apertura = '([{'
        cierre = ')]}'

        for caracter in cadena:
            if caracter in apertura:
                pila.push(caracter)
            elif caracter in cierre:
                if pila.length() == 0:
                    return False, f"Error: falta un paréntesis de apertura para '{caracter}'"
                ultimo = pila.peek()
                if pares[caracter] == ultimo:
                    pila.pop()
                else:
                    return False, f"Error: se esperaba cierre para '{ultimo}' pero se encontró '{caracter}'"
            elif not caracter.isspace():
                return False, f"Error: carácter inválido encontrado: '{caracter}'"

        if pila.length() > 0:
            ultimo = pila.peek()
            return False, f"Error: falta un paréntesis de cierre para '{ultimo}'"

        return True, "Paréntesis balanceados correctamente"




        
