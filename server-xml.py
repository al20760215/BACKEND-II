from xmlrpc.server import SimpleXMLRPCServer
import operator
import re

# Operaciones
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

# Definimos funcion que procesara la operacion
def procesar_op(operacion):
    # Definipos patron para leer la expresion regular
    regex = re.compile(r"(\d+)\s*([\+\-\*/])\s*(\d+)")
    # r(raw, descartamos \n y \t), \d(numeros), \s(para los espacios), [\+\-\*/](conjunto de operadores)
    resultado = regex.match(operacion)
    if resultado: # Definimos los datos de la expresion regular en un grupo
        n1, op, n2 = resultado.groups()
        n1, n2 = float(n1), float(n2)
    
        # Validamos division entre 0
        if op == '/' and n2 == 0:
            return "Error, no se puede dividir por 0"
        
        return ops[op](n1, n2)
    return "Operacion no valida"

# Configuracion del servidor
servidor = SimpleXMLRPCServer(("localhost", 8000))
print("Servidor activo en el puerto 8000...")
servidor.register_function(procesar_op, "procesar_op")
servidor.serve_forever()
