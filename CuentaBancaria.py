class CuentaBancaria:
    def __init__(self, saldo_inicial: float):
        self.saldo = saldo_inicial

    def calcular_interes(self):
        if self.saldo < 10000:
            interes = 0.03
        else:
            interes = 0.04
        self.saldo *= (1 + interes)

    def mostrar_saldo(self):
        print(f"El saldo final después de un año es: ${self.saldo:.2f}")


if __name__ == "__main__":
    # Recibir el saldo inicial (puedes cambiar el valor según sea necesario)
    saldo_inicial = float(input("Introduce el saldo inicial: "))

    # Crear una instancia de CuentaBancaria
    cuenta = CuentaBancaria(saldo_inicial)

    # Calcular el interés
    cuenta.calcular_interes()

    # Mostrar el saldo final
    cuenta.mostrar_saldo()