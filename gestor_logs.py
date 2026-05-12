from datetime import datetime


class GestorLogs:

    @staticmethod
    def registrar(mensaje):

        with open(
            "logs.txt",
            "a",
            encoding="utf-8"
        ) as archivo:

            archivo.write(
                f"[{datetime.now()}] "
                f"{mensaje}\n"
            )