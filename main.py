from clientes import Cliente
from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from reservas import Reserva
from excepciones import (
    ClienteError,
    ServicioError,
    ReservaError
)
from gestor_logs import GestorLogs


clientes = []
servicios = []
reservas = []


# CLIENTE VÁLIDO
try:

    cliente1 = Cliente(
        1,
        "Carlos Perez",
        "carlos@gmail.com"
    )

    clientes.append(cliente1)

except ClienteError as e:

    GestorLogs.registrar(e)


# CLIENTE INVÁLIDO
try:

    cliente2 = Cliente(
        2,
        "",
        "correo"
    )

except ClienteError as e:

    GestorLogs.registrar(e)


# SERVICIO VÁLIDO
try:

    sala = ReservaSala(
        101,
        20,
        100000
    )

    servicios.append(sala)

except ServicioError as e:

    GestorLogs.registrar(e)


# SERVICIO INVÁLIDO
try:

    equipo = AlquilerEquipo(
        102,
        "VideoBeam",
        -5000
    )

except ServicioError as e:

    GestorLogs.registrar(e)


# ASESORÍA
try:

    asesoria = AsesoriaEspecializada(
        103,
        "Python",
        150000
    )

    servicios.append(asesoria)

except ServicioError as e:

    GestorLogs.registrar(e)


# RESERVA EXITOSA
try:

    reserva1 = Reserva(
        cliente1,
        sala,
        3
    )

    total = reserva1.procesar(
        0.19,
        10000
    )

    print(total)

except ReservaError as e:

    GestorLogs.registrar(e)


# RESERVA FALLIDA
try:

    reserva2 = Reserva(
        cliente1,
        sala,
        -1
    )

except ReservaError as e:

    GestorLogs.registrar(e)


# ASESORÍA EXITOSA
try:

    reserva3 = Reserva(
        cliente1,
        asesoria,
        8
    )

    total = reserva3.procesar(0.19)

    print(total)

except ReservaError as e:

    GestorLogs.registrar(e)


# CANCELACIÓN
try:

    reserva3.cancelar()

except Exception as e:

    GestorLogs.registrar(e)


# ERROR CONTROLADO
try:

    resultado = 10 / 0

except ZeroDivisionError as e:

    GestorLogs.registrar(e)


print("Sistema ejecutado correctamente")