import re  # Importamos el modulo 're' para trabajar con expresiones regulares

class ConversorRomano: 
    def __init__(self): # Definimos un diccionario de los numeros romanos
        self.no_romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def convertir(self, romano): # Metodo para convertir una cadena de numeros romanos a un numero entero
        if not isinstance(romano, str): # Si el valor no es una cadena de texto, muestramos un mensaje de error
            raise ValueError('ERROR...INTRODUCE UNA PALABRA')
        valor = romano.upper()  # Conviertimos el texto a mayusculas
        entero = 0  # Determinamos valor 0 a la variable para almacenar el numero entero resultante de la suma
        for i in range(len(valor)):
            if i > 0 and self.no_romanos[valor[i - 1]] < self.no_romanos[valor[i]]: # Recorremos cada caracter en la cadena de texto
                entero += self.no_romanos[valor[i]] - 2 * self.no_romanos[valor[i - 1]] # Determinamos si el valor del numero romano es menor que el valor del caracter actual
                # Ajustamos el valor sumando el valor actual y restando dos veces el valor anterior
            else:
                entero += self.no_romanos[valor[i]]
                # Si no es el caso anterior, simplemente sumamos el valor del caracter actual
        return entero  # Devuelvemos el numero entero ya convertido

    def extraer_numeros(self, texto):
        # Buscamos los numeros romanos en la palabra
        patron = r'[IVXLCDM]+'  # Esta es una expresion regular para encontrar a los numeros romanos
        return re.findall(patron, texto.upper())  # Devuelvemos la lista de todos los numeros romanos encontrados

def procesar(palabras, conversor):
    # Definimos la funcion para prcesar la lista de palabras para convertirlas a numeros romanos
    for palabra in palabras: # Recorremos cada palabra en la lista
        numeros_no_romanos = conversor.extraer_numeros(palabra) # Buscamos todos los numeros romanos en la palabra
        if numeros_no_romanos: # Si hay numeros romanos encontrados
            for numeral in numeros_no_romanos: # Recorremos cada numero romano encontrado
                print(f"{numeral} en '{palabra}' = {conversor.convertir(numeral)}") # Imprimimos el numero romano y su valor convertido
        else:
            print(f"No tiene numero romanos: '{palabra}'")

def mostrar_menu():
    # Menu de opciones para el usuario
    print("\nMenu")
    print("1 - Lista de palabras")
    print("2 - Ingresar manualmente")
    print("0 - Salir")

def main():
    # Funcion principal
    conversor = ConversorRomano()  # Creamos una instancia 
    while True: # Repitimos el ciclo hasta que indiquemos salir
        mostrar_menu()  # Mostramos el menu de opciones
        opcion = input("\nOpcion: ")  # Obtenemos la opcion del usuario
        if opcion == '0':
            break
        elif opcion == '1':
            lista_palabras = ["PIXEL", "CIVIL", "PACO", "HIJO", "TOXICO", "CAMION", "CLAVE", "XIMENA", "DAMIAN", "LILI", "CLAUDIA", "MEDALLON", "CLIMA"]
            procesar(lista_palabras, conversor)
        elif opcion == '2':
            entrada = input("Ingrese palabras: ")
            palabras = [palabra.strip() for palabra in entrada.split(',')] # Dividimos las palabras ingresadas por comas y eliminamos espacios extra
            procesar(palabras, conversor)
        else:
            print("Error") # Muestramos un mensaje de error si la opcion no es valida

if __name__ == "__main__":
    main()
    
