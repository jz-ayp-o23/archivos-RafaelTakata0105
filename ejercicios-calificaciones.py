def formato_promedio(archivo, salida):
    with open(archivo, "r", encoding = "utf8") as file_in:
        with open(salida, "w", encoding= "utf8") as file_out:
            for linea in file_in:
                palabras = linea.split()
                nombre = palabras[0]
                apellido = palabras[1].upper()
                nombre_completo = f"{apellido}, {nombre}"
                calificaciones = [float(calificacion) for calificacion in palabras[2:]]
                promedio = sum(calificaciones) / len(calificaciones)
                promedio = round(promedio, 2)
                formato_final = f"{nombre_completo}: {promedio} \n"
                file_out.write(formato_final)

formato_promedio("data\calificaciones.txt", "data\promedios.txt")

