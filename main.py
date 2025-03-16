from ui import crearCuenta, depositarDinero, retirarDinero, mostrarDatosCuenta

while True:
    print("\n----- Bienvenido, ¿Qué necesita hacer? -----")
    print("1. Crear cuenta")
    print("2. Mostrar datos de la cuenta")
    print("3. Depositar")
    print("4. Retirar")
    print("5. Salir")
    
    try:
        opcionSeleccionada = int(input("Seleccione una opción: "))

        if opcionSeleccionada == 1:
            crearCuenta()
        elif opcionSeleccionada == 2:
            mostrarDatosCuenta()
        elif opcionSeleccionada == 3:
            depositarDinero()
        elif opcionSeleccionada == 4:
            retirarDinero()
        elif opcionSeleccionada == 5:
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida.")
    except ValueError:
        print("Error: Ingrese un número válido.")