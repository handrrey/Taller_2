class Cuenta:
    def __init__(self, numeroDeCuenta, documento, nombre, saldo):
        self.numeroDeCuenta__ = numeroDeCuenta
        self.documento = documento
        self.nombreCliente = nombre
        self.saldo = saldo


    def depositarDinero(self, montoIngresado):
        if montoIngresado > 0:
            self.saldo = self.saldo + (montoIngresado-montoIngresado*0.19)
            print("saldo retenido 19%: ", montoIngresado*0.19)
            print("Deposito exitoso, su saldo es de:", self.saldo)
        else:
            print("Monto ingresado no valido")


    def retirarDinero(self, montoRetirar):
        if self.saldo > montoRetirar:
            self.saldo = self.saldo - montoRetirar
            print("Retiro exitoso, su saldo actual es de:{:.2f}".format(self.saldo))
        else:
            print("Saldo insuficiente, consulte nuevamente el valor a retirar")

    def mostrarDatos(self):
        print("----- Datos de la cuenta -----")
        print("Numero de cuenta:",self.numeroDeCuenta__)
        print("Documento de cliente:", self.documento)
        print("Nombre del cliente:", self.nombreCliente)
        print("Saldo actual: {:.2f}".format(self.saldo))

    def obtenerNumeroCuenta(self):
        return self.numeroDeCuenta__

    def obtenerSaldo(self):
        return self.saldo


cuentaClientes = []

#cuentaMaria = Cuenta(1096, 2332, "Maria", 50)
#cuentaMaria.depositarDinero(100)
#cuentaMaria.retirarDinero(150)
#cuentaMaria.mostrarDatos()

#cuentaAndrea = Cuenta(1097, 2334, "Andrea", 100)
#cuentaAndrea.retirarDinero(50)
