import datetime

class Archivo:
    def __init__(self, nombre: str, fecha:datetime.date, formato:str) -> None:
        self._nombre = nombre
        self._fecha = fecha
        self._formato = formato

    #getters and setters
    def get_nombre (self):
        return self._nombre
    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_fecha (self) -> datetime.date:
        return self._fecha
    def set_fecha(self, fecha: datetime.date):
        self._fecha = fecha

    def get_formato (self):
        return self._formato
    def set_formato(self, formato):
        self._formato = formato

    #str
    def __str__(self) -> str:
        return ""

