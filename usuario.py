from abc import ABC, abstractmethod

class Usuario (ABC):
    def __init__(self, nombre: str, apellido: str, email:str, contraseña:str) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contraseña = contraseña

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def validar_credenciales(self, email, contraseña) -> bool:
        pass
