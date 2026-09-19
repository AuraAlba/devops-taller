from calculator import multiplicacion, resta


def healthcheck():
    """Muestra el estado básico de la aplicación."""
    print("\n=================================")
    print("           HEALTHCHECK")
    print("=================================")
    print("Estado: OK")
    print("Aplicación: Calculadora DevOps")


def solicitar_numeros():
    """Solicita dos números al usuario."""
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        return a, b
    except ValueError:
        print("\nError: debe ingresar números válidos.")
        return None


def main():
    while True:
        print("\n=================================")
        print("       CALCULADORA DEVOPS")
        print("=================================")
        print("1. Restar")
        print("2. Multiplicar")
        print("3. Healthcheck")
        print("4. Salir")
        print("=================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "3":
            healthcheck()
            continue

        if opcion == "4":
            print("\n¡Hasta luego!")
            break

        if opcion not in {"1", "2"}:
            print("\nOpción no válida.")
            continue

        numeros = solicitar_numeros()

        if numeros is None:
            continue

        a, b = numeros

        if opcion == "1":
            resultado = resta(a, b)
        else:
            resultado = multiplicacion(a, b)

        print(f"\nResultado: {resultado}")


if __name__ == "__main__":
    main()
