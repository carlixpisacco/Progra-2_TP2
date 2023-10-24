from usuario import Usuario
from curso import Curso


class Profesor(Usuario):

    def __init__(self, nombre: str, apellido: str, email: str, contraseña: str, titulo: str, año_egreso: int) -> None:
        super().__init__(nombre, apellido, email, contraseña)
        self._titulo = titulo
        self._año_egreso = año_egreso
        self.mis_cursos = []

    #getters y setters de los atributos privados
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_apellido(self):
        return self._apellido

    def set_apellido(self, apellido):
        self._apellido = apellido

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_contraseña(self):
        return self._contraseña

    def set_contraseña(self, contraseña):
        self._contraseña = contraseña

    def get_titulo(self):
        return self._titulo

    def set_titulo(self, titulo):
        self._titulo = titulo

    def get_año_egreso(self):
        return self._año_egreso

    def set_año_egreso(self, año_egreso):
        self._año_egreso = año_egreso

    def get_carrera_cursos(self):
        return self._carrera_cursos

    def set_carrera_cursos(self, carrera_cursos):
        self._carrera_cursos = carrera_cursos
    #str
    def __str__(self) -> str:
        return f"{self.mis_cursos}"

    #validar credeciales
    def validar_credenciales(self, contraseña) -> bool:
        if self._contraseña == contraseña:
            return True
        else:
            print("Error de ingreso. La contraseña es incorrecta")
            return False

    #dictar curso
    def dictar_curso(self, curso: Curso) -> None:  
        print("El curso se ha agregado con éxito.")
        print("Datos del curso dado de alta:")
        print(f"Nombre:{curso.get_nombre()}")
        print(f"Contraseña: {curso.get_contraseña_matriculacion()}")
        print(f"Carrera: {curso.get_carrera()}")
        print(f"Código: {curso.get_codigo()}")
        cantidad_archivos=len(curso.archivos)
        print(f"Cantidad de archivos:{cantidad_archivos}")
        self.mis_cursos.append(curso)
        
        






