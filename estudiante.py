from usuario import Usuario
from curso import Curso


class Estudiante(Usuario):

    def __init__(self, nombre: str, apellido: str, email: str, contraseña: str,legajo: int, carrera: str, año_inscripcion_carrera: int) -> None:
        super().__init__(nombre, apellido, email, contraseña)
        self._legajo = legajo
        self._carrera = carrera  #agrego esta instancia para verificar que esté inscripto a la carrera
        self._año_inscripcion_carrera = año_inscripcion_carrera
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

    def get_legajo(self):
        return self._legajo

    def set_legajo(self, legajo):
        self._legajo = legajo

    def get_carrera(self):
        return self._carrera

    def set_carrera(self, carrera):
        self._carrera = carrera

    def get_año_inscripcion(self):
        return self._año_inscripcion_carrera

    def set_año_inscripcion(self, año_inscripcion_carrera):
        self._año_inscripcion_carrera = año_inscripcion_carrera


    #str
    def __str__(self) -> str:
        return ""

    #validar credeciales
    def validar_credenciales(self, contraseña) -> bool:  #el self utiliza el objeto estudiante que instancia el metodo
        if self._contraseña == contraseña:  # es decir voy a solo va a verificar que la contraseña ingresada se corresponda al objeto estudiante que instancio el metodo.
            return True
        else:
            print("Error de ingreso. La contraseña es incorrecta")
            return False

    def matricular_en_curso(self, curso: Curso) -> None:
        self.mis_cursos.append(curso) 

    def desmatricular_en_curso(curso: Curso) -> None:
        pass
