from abc import ABC, abstractmethod
from entidades import Entidad
from excepciones import ServicioError


class Servicio(Entidad, ABC):

    def __init__(self, id_servicio, nombre, tarifa_base):

        super().__init__(id_servicio)

        if tarifa_base <= 0:
            raise ServicioError(
                "Tarifa inválida"
            )

        self._nombre = nombre
        self._tarifa_base = tarifa_base

    @abstractmethod
    def calcular_costo(self,
                        horas,
                        impuesto=0,
                        descuento=0):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):

    def __init__(self,
                 id_servicio,
                 capacidad,
                 tarifa_base):

        super().__init__(
            id_servicio,
            "Reserva Sala",
            tarifa_base
        )

        self.capacidad = capacidad

    def calcular_costo(self,
                        horas,
                        impuesto=0,
                        descuento=0):

        subtotal = self._tarifa_base * horas

        subtotal += subtotal * impuesto

        subtotal -= descuento

        return subtotal

    def descripcion(self):

        return (
            f"Sala para "
            f"{self.capacidad} personas"
        )

    def mostrar_info(self):
        return self.descripcion()


class AlquilerEquipo(Servicio):

    def __init__(self,
                 id_servicio,
                 tipo_equipo,
                 tarifa_base):

        super().__init__(
            id_servicio,
            "Alquiler Equipo",
            tarifa_base
        )

        self.tipo_equipo = tipo_equipo

    def calcular_costo(self,
                        horas,
                        impuesto=0,
                        descuento=0):

        subtotal = self._tarifa_base * horas

        subtotal += subtotal * impuesto

        subtotal -= descuento

        return subtotal

    def descripcion(self):

        return (
            f"Equipo: "
            f"{self.tipo_equipo}"
        )

    def mostrar_info(self):
        return self.descripcion()


class AsesoriaEspecializada(Servicio):

    def __init__(self,
                 id_servicio,
                 especialidad,
                 tarifa_base):

        super().__init__(
            id_servicio,
            "Asesoría",
            tarifa_base
        )

        self.especialidad = especialidad

    def calcular_costo(self,
                        horas,
                        impuesto=0,
                        descuento=0):

        subtotal = self._tarifa_base * horas

        if horas > 5:
            subtotal *= 0.9

        subtotal += subtotal * impuesto

        subtotal -= descuento

        return subtotal

    def descripcion(self):

        return (
            f"Asesoría en "
            f"{self.especialidad}"
        )

    def mostrar_info(self):
        return self.descripcion()