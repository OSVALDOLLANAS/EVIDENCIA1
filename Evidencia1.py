biblioteca={}
while True:
    print("*"*40)
    print("****         MENU PRICIPAL         ****")
    opcion=int(input("[1]Registrar nuevo ejemplar\n[2]Consultas y reportes\n[3]Salir\nElija un opcion: "))
    print("*"*40)
    
    if opcion==1:
        print("*"*40)
        print("****  REGISTRO DE NUEVO EJEMPLEAR   ****")
        titulo=input("Ingrese el titulo: ")
        autor=input(f"Indique el autor de {titulo}: ")
        genero=input(f"Indique el genero de {titulo}: ")
        año_publicacion=input(f"Indique el año de publicación de {titulo}: ")
        isbn=input(f"Indique el ISBN de {titulo:}: ")
        fecha_adquisicion=input(f"Indique la fecha de adquisición de {titulo}: ")
        print("*"*40)
        identificador=max(biblioteca,default=0)+1
        biblioteca[identificador]=[identificador,titulo,autor,genero,año_publicacion,isbn,fecha_adquisicion]
        print(biblioteca)
        continue

    if opcion==2:
        while True:
            print("*"*40)
            print("****      CONSULTAS Y REPORTES      ****")
            opcion_2=int(input("[1]Consulta de titulo\n[2]Reportes\n[3]Volver al menu de consultas y reportes\nElija una opcion: "))
            print("*"*40)

            if opcion_2==1:
                while True:
                    print("*"*40)
                    opcion2_1=int(input("[1]Por titulo\n[2]Por ISBN\n[3]Volver al menu de consultas y reportes\nElija una opcion: "))

                    if opcion2_1==1:
                        print("*"*40)
                        print(f"ID\tTITULO")
                        print("*"*40)
                        for identificador,titulo,autor,genero,año_publicacion,isbn,fecha_adquisicion in biblioteca.values():
                            print(f"{identificador:3} | {titulo}")
                        else:
                            print("*"*40)
                        print("")
                        titulo_consulta=input("Elija una opcion para obtener todos los datos de el titulo: ")
                        print("")
                        print("*"*130)
                        print(f"ID\tTITULO\t\t\tAUTOR\t\tGENERO\t\tAÑO DE PUBLICACION\tISBN\t\tFECHA DE ADQUISICIÓN")
                        for identificador,titulo,autor,genero,año_publicacion,isbn,fecha_adquisicion in biblioteca.values():
                            if titulo==titulo_consulta:
                                print(f"{identificador:3}|{titulo:20}|{autor:20}|{genero:15}|{año_publicacion:20}|{isbn:20}|{fecha_adquisicion}")
                        else:
                            print("*"*130)
                
                    if opcion2_1==2:
                        print("*"*40)
                        print(f"ID\tISBN")
                        print("*"*40)
                        for identificador,titulo,autor,genero,año_publicacion,isbn,fecha_adquisicion in biblioteca.values():
                            print(f"{identificador:3} | {isbn}")
                        else:
                            print("*"*40)
                            print("")
                        isbn_consulta=input("Elija una opcion para obtener todos los datos de el isbn: ")
                        print("")
                        print("*"*130)
                        print(f"ID\tTITULO\t\t\tAUTOR\t\tGENERO\t\tAÑO DE PUBLICACION\tISBN\t\tFECHA DE ADQUISICIÓN")
                        for identificador,titulo,autor,genero,año_publicacion,isbn,fecha_adquisicion in biblioteca.values():
                            if isbn==isbn_consulta:
                                print(f"{identificador:3}|{titulo:20}|{autor:20}|{genero:15}|{año_publicacion:20}|{isbn:20}|{fecha_adquisicion}")
                        else:
                            print("*"*130)

                    if opcion2_1==3:
                        break

            if opcion_2==2:
                while True:
                    print("*"*40)
                    print("****            REPORTES            ****")
                    print("*"*40)
                    opcion2_2=int(input("[1]Catalago completo\n[2]Reporte por autor\n[3]Reporte por género\n[4]Por año de publicación\n[5]Volver al menú de reportes\nElija una opcion: "))
                    print("")

                    if opcion2_2==1:
                        print("*"*130)
                        print(f"ID\tTITULO\t\t\tAUTOR\t\tGENERO\t\tAÑO DE PUBLICACION\tISBN\t\tFECHA DE ADQUISICIÓN")
                        print("*"*130)
                        for identificador,titulo,autor,genero,año_publicacion,isbn,fecha_adquisicion in biblioteca.values():
                            print(f"{identificador:3}|{titulo:20}|{autor:20}|{genero:15}|{año_publicacion:20}|{isbn:20}|{fecha_adquisicion}")
                        else:
                            print("*"*130)
                        print("")
                        
                    if opcion2_2==2:
                        print("*"*40)
                        print(f"ID\tAUTOR")
                        print("*"*40)
                        for identificador,titulo,autor,genero,año_publicacion,isbn,fecha_adquisicion in biblioteca.values():
                            print(f"{identificador:3}|{autor}")
                        else:
                            print("*"*40)
                        print("")
                        autor_opcion=input(f"Elija un autor para mostrar todas los ejemplares existentes: ")
                        print("")
                        print("*"*130)
                        print(f"ID\tTITULO\t\t\tAUTOR\t\tGENERO\t\tAÑO DE PUBLICACION\tISBN\t\tFECHA DE ADQUISICIÓN")
                        print("*"*130)
                        for identificador,titulo,autor,genero,año_publicacion,isbn,fecha_adquisicion in biblioteca.values():
                            if autor==autor_opcion:
                                print(f"{identificador:3}|{titulo:20}|{autor:20}|{genero:15}|{año_publicacion:20}|{isbn:20}|{fecha_adquisicion}")
                        else:
                            print("*"*130)
                        print("")

                    if opcion2_2==3:
                        print("*"*40)
                        print(f"ID\tGENERO")
                        print("*"*40)
                        for identificador,titulo,autor,genero,año_publicacion,isbn,fecha_adquisicion in biblioteca.values():
                            print(f"{identificador:3}|{genero}")
                        else:
                            print("*"*40)
                        print("")
                        genero_opcion=input(f"Elija un genero para mostrar todas los ejemplares existentes: ")
                        print("")
                        print("*"*130)
                        print(f"ID\tTITULO\t\t\tAUTOR\t\tGENERO\t\tAÑO DE PUBLICACION\tISBN\t\tFECHA DE ADQUISICIÓN")
                        print("*"*130)
                        for identificador,titulo,autor,genero,año_publicacion,isbn,fecha_adquisicion in biblioteca.values():
                            if genero==genero_opcion:
                                print(f"{identificador:3}|{titulo:20}|{autor:20}|{genero:15}|{año_publicacion:20}|{isbn:20}|{fecha_adquisicion}")
                        else:
                            print("*"*130)
                        print("")

                    if opcion2_2==4:
                        print("*"*40)
                        print(f"ID\tAÑO ESPECIFICO")
                        print("*"*40)
                        for identificador,titulo,autor,genero,año_publicacion,isbn,fecha_adquisicion in biblioteca.values():
                            print(f"{identificador:3}|{año_publicacion}")
                        else:
                            print("*"*40)
                        print("")
                        año_publicacion_opcion=input(f"Elija un año para mostrar todas los ejemplares existentes: ")
                        print("")
                        print("*"*130)
                        print(f"ID\tTITULO\t\t\tAUTOR\t\tGENERO\t\tAÑO DE PUBLICACION\tISBN\t\tFECHA DE ADQUISICIÓN")
                        print("*"*130)
                        for identificador,titulo,autor,genero,año_publicacion,isbn,fecha_adquisicion in biblioteca.values():
                            if año_publicacion==año_publicacion_opcion:
                                print(f"{identificador:3}|{titulo:20}|{autor:20}|{genero:15}|{año_publicacion:20}|{isbn:20}|{fecha_adquisicion}")
                        else:
                            print("*"*130)
                        print("")
                    if opcion2_2==5:
                        break
            if opcion_2==3:
                break  
    if opcion==3:
        break