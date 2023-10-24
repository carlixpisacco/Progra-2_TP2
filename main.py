from estudiante import Estudiante
from profesor import Profesor
from curso import Curso
from carrera import Carrera
from archivo import Archivo
from funciones import *
import os
from datetime import datetime

def desmatricular_alumno(estudiante):
    if len(estudiante.mis_cursos)==0:
        print("Todavía no posee cursos matriculados.")
        return

    while True:
        for indice, curso in enumerate(estudiante.mis_cursos, 1):
            print(f"{indice} {curso}")

        opt = input("\nIngrese el curso: ")
        if opt.isnumeric():
            opt=int(opt)
            if opt<=len(estudiante.mis_cursos):
                estudiante.mis_cursos.remove(estudiante.mis_cursos[opt-1])
                print("Se ha registrado correctamente su desmatriculación")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
        else:
            print("Opción no válida. Ingrese una opción numérica")

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
                                    if not cursos_disponibles:
                                        print ("ERROR. Aún no hay cursos cargados para matricularse.\n")
                                    else:
                                        contador = 1
                                        print("Seleccione un curso para ver información del mismo:")
                                        for curso in cursos_disponibles:
                                            print(f"{contador} - {curso.get_nombre().title()}")
                                            contador += 1

                                        continuar = True
                                        while continuar:
                                            opt_curso_matricular = input("Ingrese la opción de menú: ")
                                            if opt_curso_matricular.isnumeric():
                                                opt_curso_matricular = int(opt_curso_matricular)
                                                if 1 <= opt_curso_matricular <= len(cursos_disponibles):
                                                    curso_elegido = cursos_disponibles[opt_curso_matricular - 1]
                                                    contraseña_ingresada = input("Ingrese la contraseña de matriculación del curso: ")
                                                    if curso_elegido in estudiante.mis_cursos:
                                                        print("El alumno ya está matriculado en este curso.")
                                                        continuar = False
                                                    else:
                                                        if curso_elegido.get_carrera() != estudiante.get_carrera():
                                                            if contraseña_ingresada == curso_elegido.get_contraseña_matriculacion():
                                                                print("Matriculación exitosa")
                                                                estudiante.mis_cursos.append(curso)
                                                                continuar=False
                                                            else:
                                                                print("ERROR. Contraseña de matriculación incorrecta")
                                                                continuar = False
                                                        else:
                                                                print("El alumno no se encuentra inscripto a la carrera a la cual pertenece el curso.")
                                                                continuar = False
                                                else:
                                                    print("Opción no válida. Ingrese un número dentro del rango.")
                                            else:
                                                print("ERROR. Ingrese una opción numérica")

                            elif int(opt_alumno) == 2:
                                desmatricular_alumno(estudiante)
                                pass
                            elif int(opt_alumno) == 3:
                                while True:
                                    for indice, curso in enumerate(estudiante.mis_cursos, 1):
                                        print(f"{indice} {curso}")
                                        
                                        opt = input("\nIngrese el curso:")
                                        
                                        if opt.isnumeric():
                                            opt=int(opt)
                                            if opt<=len(estudiante.mis_cursos):
                                                print(f"{(estudiante.mis_cursos[opt-1])}")
                                                for i in curso.archivos:
                                                    print(f"Nombre de archivo: {i._nombre} {i._formato} Fecha: {i._fecha}")
                                            else:
                                                print("Opción no válida. Por favor, seleccione una opción válida.")
                                        else:
                                            print("Opción no válida. Ingrese una opción numérica")
                                        
                                        break    
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
                                nombre = input ("Ingrese nombre del curso que desea dictar: ")
                                curso = Curso(nombre, carrera)
                                profesor.dictar_curso(curso)
                                cursos_disponibles.append(curso)
                                
                            elif int(opt_profesor) == 2:
                                if not profesor.mis_cursos:
                                    print ("ERROR. Aún no hay cursos cargados.\n")
                                else:
                                    contador = 1
                                    print("Seleccione un curso para ver información del mismo:")
                                    for curso in profesor.mis_cursos:
                                        print(f"{contador} - {curso.get_nombre().title()}")
                                        contador += 1

                                    continuar = True
                                    while continuar:
                                        opt_curso_profesor = input("Ingrese la opción de menú: ")
                                        if opt_curso_profesor.isnumeric():
                                            opt_curso_profesor = int(opt_curso_profesor)
                                            if 1 <= opt_curso_profesor <= len(profesor.mis_cursos):
                                                mostrar_info_curso(opt_curso_profesor, profesor)
                                                print("\n¿Desea agregar un archivo a este curso?")
                                                opt_archivos=input("Presione 1 si desea agregar un archivo. Presione cualquier tecla para volver al submenu de profesor: ")
                                                if opt_archivos== "1":
                                                    nombre = input ("Ingrese nombre del archivo que desea agregar: ")
                                                    fecha = datetime.now().date()
                                                    formato = input ("Ingrese el formato del archivo que desea agregar: ")
                                                    archivo = Archivo(nombre, fecha, formato)
                                                    curso.nuevo_archivo(archivo)
                                                    break
                                                else: 
                                                    break
                                            else:
                                                print("Opción no válida. Ingrese un número dentro del rango.")
                                        else:
                                            print("ERROR. Ingrese una opción numérica")

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
