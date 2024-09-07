import re

# Definir los valores de los símbolos romanos
roman_numerals = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

# Función para convertir un número romano a decimal
def roman_to_decimal(roman):
    value = 0
    prev_value = 0

    for char in reversed(roman):
        if char not in roman_numerals:
            return None
        current_value = roman_numerals[char]
        if current_value < prev_value:
            value -= current_value
        else:
            value += current_value
        prev_value = current_value

    return value

# Función para validar el patrón de números romanos
def is_valid_roman(roman):
    # Reglas de validación usando regex
    pattern = re.compile(r'^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
    return pattern.match(roman) is not None

# Función para analizar cada letra y encontrar secuencias válidas
def extract_roman_substrings(word):
    word = word.upper()
    roman_substrings = []
    
    # Buscar todas las posibles secuencias romanas en la palabra
    for i in range(len(word)):
        for j in range(i+1, len(word)+1):
            substring = word[i:j]
            if is_valid_roman(substring):
                roman_substrings.append(substring)
    
    return roman_substrings

# Función para convertir palabras a valores romanos
def word_to_roman_value(word):
    roman_substrings = extract_roman_substrings(word)
    
    if not roman_substrings:
        return None
    
    # Convertir las secuencias válidas a valores decimales
    values = [roman_to_decimal(substring) for substring in roman_substrings]
    
    return values

# Lista de palabras a evaluar
words = [
    'PIXEL', 'CIVIL', 'PACO', 'HIJO', 'TOXICO', 'CAMION', 'CLAVE',
    'XIMENA', 'DAMIAN', 'LILI', 'CLAUDIA', 'MEDALLON', 'CLIMA'
]

# Imprimir valores decimales para cada palabra
for word in words:
    values = word_to_roman_value(word)
    print(f'{word} = {values}')
