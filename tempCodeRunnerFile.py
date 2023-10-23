elif int(opt) == 2:
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
                        opt = input("\n Ingrese la opción de menú: ")
                        os.system("cls")  #Limpiar pantalla
                        if opt.isnumeric():
                            if int(opt) == 1:
                                nombre = input ("Ingrese nombre del curso que desea dictar: ")
                                curso = Curso(nombre, carrera)
                                profesor.dictar_curso(curso)
                                cursos_disponibles.append(curso)
                                print("Cursos disponibles:")
                                for curso in cursos_disponibles:
                                    print(curso)
                            elif int(opt) == 2:
                                pass
                            elif int(opt) == 3:
                                respuesta_profesor = "salir"
                            else:
                                print("Ingrese una opción válida")
                        else:
                            print("Ingrese una opción numérica")
                else:
                    continue
