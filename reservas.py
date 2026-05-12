from excepciones import ReservaError
from gestor_logs import GestorLogs


class Reserva:

    def __init__(self,
                 cliente,
                 servicio,
                 horas):

        if horas <= 0:
            raise ReservaError(
                "Horas inválidas"
            )

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

    def confirmar(self):

        self.estado = "Confirmada"

        GestorLogs.registrar(
            f"Reserva confirmada "
            f"{self.cliente.nombre}"
        )

    def cancelar(self):

        self.estado = "Cancelada"

        GestorLogs.registrar(
            f"Reserva cancelada "
            f"{self.cliente.nombre}"
        )

    def procesar(self,
                 impuesto=0,
                 descuento=0):

        try:

            costo = self.servicio.calcular_costo(
                self.horas,
                impuesto,
                descuento
            )

        except Exception as error:

            raise ReservaError(
                "Error procesando reserva"
            ) from error

        else:

            self.confirmar()

            return costo

        finally:

            GestorLogs.registrar(
                "Proceso finalizado"
            )