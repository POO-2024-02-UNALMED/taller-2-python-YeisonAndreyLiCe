class Asiento:
    colores_permitidos = {"rojo", "verde", "amarillo", "negro", "blanco"}

    def __init__(self, color: str, precio: float, registro: int) -> None:
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color: str) -> None:
        if color.lower() in Asiento.colores_permitidos:
            self.color = color.lower()


class Motor:
    tipos_permitidos = {"electrico", "gasolina"}
    def __init__(self, numeroDeCilindros: int, tipo: str, registro: int) -> None:
        self.numeroDeCilindros = numeroDeCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro: int) -> None:
        self.registro = registro

    def asignarTipo(self, tipo: str) -> None:
        if tipo.lower() in Motor.tipos_permitidos:
            self.tipo = tipo.lower()


class Auto:
    cantidaCreados = 0
    def __init__(
            self,
            modelo: str,
            precio: float,
            asientos: list[Asiento],
            marca: str,
            motor: Motor,
            registro: int
        ) -> None:
        self.modelo = modelo
        self.precio = precio
        self.asientos = [asiento for asiento in asientos if isinstance(asiento, Asiento)]
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidaCreados += 1

    def cantidadAsientos(self) -> int:
        return len([asiento for asiento in self.asientos if isinstance(asiento, Asiento)])

    def verificarIntegridad(self) -> bool:
        message = "Auto original"
        if self.motor.registro != self.registro:
            message = "Las piezas no son originales"

        for asiento in self.asientos:
            if asiento.registro != self.registro:
                message = "Las piezas no son originales"

        return message
