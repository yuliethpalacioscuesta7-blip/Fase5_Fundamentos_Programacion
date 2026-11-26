
# Programa para evaluar la popularidad y actualidad
# de los titulos de una videoteca digital

videoteca = [
    ["Interestelar", 2014, 9.0, "Ciencia ficcion"],
    ["Encanto", 2021, 8.5, "Animacion"],
    ["Dune", 2021, 8.7, "Ciencia ficcion"],
    ["Titanic", 1997, 9.0, "Romance"],
    ["Spider-Man: No Way Home", 2021, 8.2, "Accion"],
    ["Coco", 2017, 8.5, "Animacion"],
    ["Oppenheimer", 2023, 9.0, "Drama"],
    ["Barbie", 2023, 7.5, "Comedia"]
]

# Criterios de evaluacion
umbral_calificacion = 8.0
ano_limite = 2020

# Funcion para contar los titulos que cumplen los criterios
def contar_titulos(matriz, calificacion_minima, ano_minimo):
    contador = 0

    for pelicula in matriz:
        if pelicula[2] >= calificacion_minima and pelicula[1] >= ano_minimo:
            contador += 1

    return contador

# Llamada a la funcion
total = contar_titulos(videoteca, umbral_calificacion, ano_limite)

# Mostrar resultado
print("INFORME DE LA VIDEOTECA DIGITAL")
print("--------------------------------")
print("Calificacion minima:", umbral_calificacion)
print("Ano limite:", ano_limite)
print("Total de titulos que cumplen los criterios:", total)

