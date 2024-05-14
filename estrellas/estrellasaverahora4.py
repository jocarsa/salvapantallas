import cv2
import numpy as np
import math
import time
import os

class Estrella:
    def __init__(self):
        self.angulo = np.random.rand() * 2 * math.pi
        self.distancia = np.random.rand() * 1000

numero_estrellas = 1000
estrellas = []

anchura = 1920  
altura = 1080

# Obtener la marca de tiempo de epoch
epoch_time = int(time.time())

# Nombre del archivo temporal con la marca de tiempo de epoch
nombre_archivo_temporal = f'estrellas_temp_{epoch_time}.mp4'

# Iniciar la captura de video
video = cv2.VideoWriter(nombre_archivo_temporal, cv2.VideoWriter_fourcc(*'mp4v'), 60, (anchura, altura))
fps = 60
segundosporminuto = 60
minutos = 60
contador = 0

# Crear una imagen negra semitransparente
imagen_negra = np.zeros((altura, anchura, 3), dtype=np.uint8)
imagen_negra.fill(0)
alfa = 0.2  # Transparencia, ajusta este valor según lo deseado
imagen_negra = cv2.addWeighted(imagen_negra, alfa, np.zeros(imagen_negra.shape, imagen_negra.dtype), 1 - alfa, 0)

try:
    while contador< fps*segundosporminuto*minutos:
        
        contador += 1
        if len(estrellas) < numero_estrellas:
            for i in range(0,1):
                estrellas.append(Estrella())

        frame = np.zeros((altura, anchura, 3), dtype=np.uint8)  # Se crea el marco en cada iteración
        frame.fill(0)

        for estrella in estrellas:
            estrella.distancia += (estrella.distancia / 100)*3
            if estrella.distancia > 1000:
                estrella.distancia = 0.1

            vertices = np.array([
                [anchura / 2 + estrella.distancia * np.cos(estrella.angulo), altura / 2 + estrella.distancia * np.sin(estrella.angulo)],
                [anchura / 2 + estrella.distancia * 1.04 * np.cos(estrella.angulo), altura / 2 + estrella.distancia * 1.04 * np.sin(estrella.angulo)],
                [anchura / 2 + estrella.distancia * 1.04 * np.cos(estrella.angulo + 0.002), altura / 2 + estrella.distancia * 1.04 * np.sin(estrella.angulo + 0.002)],
                [anchura / 2 + estrella.distancia * np.cos(estrella.angulo + 0.002), altura / 2 + estrella.distancia * np.sin(estrella.angulo + 0.002)]
            ])

            cv2.fillPoly(frame, [vertices.astype(np.int32)], (255, 255, 255))

        # Aplicar la imagen negra semitransparente DESPUÉS de dibujar las estrellas
        frame = cv2.addWeighted(frame, 1, imagen_negra, 1, 0)

        video.write(frame)

        cv2.imshow('Estrellas', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception as e:
    print("Se produjo un error:", e)

finally:
    video.release()
    cv2.destroyAllWindows()

    if os.path.exists(nombre_archivo_temporal):
        nombre_archivo_final = f'estrellas_{epoch_time}.mp4'
        os.rename(nombre_archivo_temporal, nombre_archivo_final)
        print(f"El video se ha guardado como '{nombre_archivo_final}'")
    else:
        print("No se pudo guardar el video.")
