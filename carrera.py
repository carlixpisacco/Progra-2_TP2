class Carrera:
    def __init__(self, nombre:str, cant_años:int) -> None:
        self._nombre = nombre
        self._cant_años = cant_años

    #getters y setters
    def get_nombre (self):
        return self._nombre
    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_cant_años (self):
        return self.cant_años
    def set_cant_años(self, cant_años):
        self._cant_años = cant_años

    #str
    def __str__(self) -> str:
       return f"{self.get_nombre()}"

   