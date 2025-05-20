#Ejercicio #2: Verificación de paréntesis balanceados. Escriba un programa que
#determine si una cadena de texto dada tiene los paréntesis ( ), { }, y [ ] balanceados.
#Use una pila para realizar el seguimiento de los paréntesis abiertos.


# Archivo: Ejercicio2.py

class Ejercicio2:
    def verificar_parentesis(self, cadena):
        pila = []
        pares = {')': '(', ']': '[', '}': '{'}
        apertura = '([{'
        cierre = ')]}'

        for i, caracter in enumerate(cadena):
            if caracter in apertura:
                pila.append((caracter, i))  # Guarda también la posición
            elif caracter in cierre:
                if not pila:
                    return False, f"Error en posición {i}: falta un paréntesis de apertura para '{caracter}'"
                ultimo, pos = pila[-1]
                if pares[caracter] == ultimo:
                    pila.pop()
                else:
                    return False, f"Error en posición {i}: se esperaba cierre para '{ultimo}' pero se encontró '{caracter}'"

            elif not caracter.isspace():
                return False, f"Carácter inválido en posición {i}: '{caracter}'"

        if pila:
            ultimo, pos = pila[-1]
            return False, f"Falta un paréntesis de cierre para '{ultimo}' abierto en posición {pos}"

        return True, "Paréntesis balanceados correctamente"



        
