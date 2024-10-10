import xmlrpc.client

def main():
    with xmlrpc.client.ServerProxy("http://localhost:8000/") as server:
        print("Para terminar, escribe 'salir'")
        while True:
            operacion = input("Operacion: ")
            if operacion == "salir":
                break

            try:
                resultado = server.procesar_op(operacion)
                print(f"Resultado: {resultado}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()
