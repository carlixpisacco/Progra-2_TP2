from estudiante import Estudiante
from profesor import Profesor
from carrera import Carrera
from funciones import *
import os

      
carrera = Carrera("Tecnicatura en Programación Web", 2)
carreras = [carrera]

estudiante_1 = Estudiante("Carla", "Pisacco", "carlapisacco@gmail.com","contraseña1", 1111,"Tecnicatura en Programación Web", 2019)
estudiante_2 = Estudiante("Kevin", "Caceres", "kevincaceres@gmail.com","contraseña2", 2222,"Tecnicatura en Programación Web", 2020)
estudiante_3 = Estudiante("Clara", "Perez", "claraperez@gmail.com","contraseña3", 3333,"Tecnicatura en Programación Web", 2020)
estudiante_4 = Estudiante("Mariano", "Castelli", "marianocastelli@gmail.com","contraseña4", 4444,"Tecnicatura en Programación Web", 2021)

estudiantes = [estudiante_1, estudiante_2, estudiante_3, estudiante_4]

profesor_1 = Profesor("Martin", "Gonzalez", "martingonzalez@gmail.com", "contraseña1", "Ingeniero en Sistemas", 1990)
profesor_2 = Profesor("Paula", "Lopez", "paulalopez@gmail.com", "contraseña2", "Programadora", 1999)
profesor_3 = Profesor("Pablo", "Rodriguez", "pablorodriguez@gmail.com", "contraseña3", "Porgramador", 2005)
profesor_4 = Profesor("Martina", "Gil", "martinagil@gmail.com", "contraseña4", "Ingeniera Electrónica", 2010)

profesores = [profesor_1, profesor_2, profesor_3, profesor_4]

cursos_disponibles = []

respuesta = ''
while respuesta != "salir":
    menu()
    opt_principal = input("Ingrese la opción de menú: ")
    os.system("cls")  #Limpiar pantalla
    estudiante = None
    profesor = None
    respuesta_alumno = ''
    respuesta_profesor = ''
    if opt_principal.isnumeric():
        if int(opt_principal) == 1:
            email = input("Ingrese su email: ")  #email ingresado por el usuario
            contraseña = input("Ingrese su contraseña:")  #contraseña ingresada por el usuario
            estudiante = buscar_estudiante_email(email, estudiantes)  #creo una variable para almacenar lo que me devuelva la funcion buscar estudiante email, es decir guardo el objeto que esta ingresando.
            if estudiante == None:  #si me devuelve nada, tira que no esta en la base de datos
                print("Alumno/a no encontrado/a en la base de datos. Debe darse de alta en alumnado")
            else:  #si encuentra un estudiante me devuelve el objeto estudiante que tiene ese mail
                if estudiante.validar_credenciales(contraseña):  #aca uso ese estudiante para instanciar el metodo validar credenciales y le envio la contraseña que ingreso
                    while respuesta_alumno != "salir":
                        menu_alumno()
                        opt_alumno = input("Ingrese la opción de menú: ")
                        os.system("cls")  #Limpiar pantalla
                        if opt_alumno.isnumeric():
                            if int(opt_alumno) == 1:
                                matricular_alumno(estudiante, cursos_disponibles)
                            elif int(opt_alumno) == 2:
                                desmatricular_alumno(estudiante, cursos_disponibles)
                            elif int(opt_alumno) == 3:
                                mostrar_curso_alumno(estudiante)
                            elif int(opt_alumno) == 4:
                                respuesta_alumno = "salir"
                            else:
                                print("Ingrese una opción válida")
                        else:
                            print("Ingrese una opción numérica")
                else:
                    continue

        elif int(opt_principal) == 2:
            email = input("Ingrese su email: ")
            contraseña = input("Ingrese su contraseña: ")
            profesor = buscar_profesor_email(email, profesores)
            if profesor == None:
                print(
                    "Profesor/a no encontrado/a en la base de datos. Debe darse de alta en alumnado"
                )
            else:
                if profesor.validar_credenciales(contraseña):
                    while respuesta_profesor != "salir":
                        menu_profesor()
                        opt_profesor = input("Ingrese la opción de menú: ")
                        os.system("cls")  #Limpiar pantalla
                        if opt_profesor.isnumeric():
                            if int(opt_profesor) == 1:
                                dictar_curso(profesor, cursos_disponibles)
                            elif int(opt_profesor) == 2:
                                mostrar_cursos_profesor(profesor)
                            elif int(opt_profesor) == 3:
                                respuesta_profesor = "salir"
                            else:
                                print("Ingrese una opción válida")
                        else:
                            print("Ingrese una opción numérica")
                else:
                    continue

        elif int(opt_principal) == 3:
            if not cursos_disponibles:
                print ("ERROR. Aún no hay cursos cargados.\n")
            else:
                ordenar_cursos(cursos_disponibles)
        elif int(opt_principal) == 4:
            respuesta = "salir"
        else:
            print("Ingrese una opción válida")
    else:
        print("Ingrese una opción numérica")

print("¡Hasta luego!.")
