from modelo import Cuenta, cuentaClientes

def crearCuenta():
    try:
        numeroCuenta = int(input("Ingrese el número de cuenta: "))
        documento = int(input("Ingrese el documento de identidad: "))
        nombreCliente = input("Ingrese el nombre del cliente: ")
        saldo = float(input("Ingrese el saldo inicial: "))

        cuentaNueva = Cuenta(numeroCuenta, documento, nombreCliente, saldo)
        cuentaClientes.append(cuentaNueva)

        print("Su cuenta ha sido creada exitosamente.")
    except ValueError:
        print("Entrada no válida. Por favor ingrese datos correctos.")

def depositarDinero():
    try:
        numeroCuenta = int(input("Ingrese el número de cuenta para el depósito: "))
        monto = float(input("Ingrese el monto a depositar: "))

        cuentaEncontrada = None
        for cuenta in cuentaClientes:  
            if cuenta.obtenerNumeroCuenta() == numeroCuenta:  
                cuentaEncontrada = cuenta
                break  

        if cuentaEncontrada:
            cuentaEncontrada.depositarDinero(monto)  
        else:
            print("Error: Cuenta no encontrada.")
    except ValueError:
        print("Entrada no válida.")


def retirarDinero():
    try:
        numeroCuenta = int(input("Ingrese el número de cuenta para el retiro: "))
        monto = float(input("Ingrese el monto a retirar: "))

        cuentaEncontrada = None
        for cuenta in cuentaClientes:
            if cuenta.obtenerNumeroCuenta() == numeroCuenta:
                cuentaEncontrada = cuenta
                break

        if cuentaEncontrada:
            cuentaEncontrada.retirarDinero(monto)
        else:
            print("Cuenta no encontrada.")
    except ValueError:
        print("Entrada no válida.")

def mostrarDatosCuenta():
    try:
        numeroCuenta = int(input("Ingrese el número de cuenta para ver los datos: "))

        cuentaEncontrada = None
        for cuenta in cuentaClientes:
            if cuenta.obtenerNumeroCuenta() == numeroCuenta:
                cuentaEncontrada = cuenta
                break

        if cuentaEncontrada:
            cuentaEncontrada.mostrarDatos()
        else:
            print("Cuenta no encontrada.")
    except ValueError:
        print("Entrada no válida.")
