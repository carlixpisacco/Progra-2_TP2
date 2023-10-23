from archivo import Archivo
import random


class Curso:
    _prox_cod = 0  #atributo estatico.

    def __init__(self, nombre: str,  carrera) -> None:
        self._nombre = nombre
        self._contraseña_matriculacion = self._generar_contraseña()
        self._carrera = carrera
        self._codigo = Curso._prox_cod
        Curso._prox_cod += 1
        self.archivos= []

    #getters y setters
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_contraseña_matriculacion(self):
        return self._contraseña_matriculacion

    def set_contraseña_matriculacion(self, contraseña_matriculacion):
        self._contraseña_matriculacion = contraseña_matriculacion

    def get_carrera(self):
        return self._carrera

    def set_carrera(self, carrera):
        self._carrera= carrera

    def get_prox_cod(self):
        return self._prox_cod

    def get_codigo(self):
        return self._codigo

    #str
    def __str__(self) -> str:
        return f"Curso: {self.get_nombre()}, Contraseña: {self.get_contraseña_matriculacion()} Carrera: {self.get_carrera()} Codigo:{self.get_codigo()}"

    #nuevo archivo
    def nuevo_archivo(self, archivo: Archivo):
        self.archivos.append(archivo)

    #generar contraseña, metodo estatico
    @staticmethod
    def _generar_contraseña() -> str:
        contraseña = ""
        caracteres = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789"
        for i in range(4):
            contraseña += random.choice(caracteres)
        return contraseña
