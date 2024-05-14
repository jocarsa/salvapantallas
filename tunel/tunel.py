import cv2
import numpy as np
import math
import time

width = 1920
height = 1080
numerodelados = np.random.randint(10, 51)
centrox = width // 2
centroy = height // 2
circulos = []

def poligono(cx, cy, lados, radio, color, angulo, img):
    points = []
    for i in range(lados):
        x = int(cx + math.cos(math.pi * 2 * (i / lados) + angulo) * radio)
        y = int(cy + math.sin(math.pi * 2 * (i / lados) + angulo) * radio)
        points.append((x, y))
    cv2.polylines(img, [np.array(points)], isClosed=True, color=color, thickness=5)

def bucle(frame):
    global circulos
    global numerodelados

    frame[:] = (0, 0, 0)

    for circulo in circulos:
        circulo['radio'] *= 1.08
        poligono(circulo['x'], circulo['y'], numerodelados, int(circulo['radio']), (255, 255, 255), circulo['a'], frame)

    cursorx = centrox
    cursory = centroy
    cursorangulo = np.random.rand() * math.pi * 2

    cursorx += int(math.cos(cursorangulo) * 5)
    cursory += int(math.sin(cursorangulo) * 5)
    cursorangulo += (np.random.rand() - 0.5) * 0.7

    circulos.append({'x': cursorx, 'y': cursory, 'radio': 1, 'a': 0})

    if len(circulos) > 2:
        for i in range(1, len(circulos)):
            for j in range(numerodelados):
                cv2.line(frame, (int(circulos[i]['x'] + math.cos((j / numerodelados) * math.pi * 2 + circulos[i]['a']) * circulos[i]['radio']),
                                  int(circulos[i]['y'] + math.sin((j / numerodelados) * math.pi * 2 + circulos[i]['a']) * circulos[i]['radio'])),
                         (int(circulos[i - 1]['x'] + math.cos((j / numerodelados) * math.pi * 2 + circulos[i - 1]['a']) * circulos[i - 1]['radio']),
                                  int(circulos[i - 1]['y'] + math.sin((j / numerodelados) * math.pi * 2 + circulos[i - 1]['a']) * circulos[i - 1]['radio'])),
                         (255, 255, 255), thickness=5)

    circulos = [circulo for circulo in circulos if circulo['radio'] < width]

frame = np.zeros((height, width, 3), dtype=np.uint8)  # Crear un frame negro con el tamaño deseado
cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)  # Permitir el cambio de tamaño de la ventana
cv2.resizeWindow('Frame', width, height)  # Establecer el tamaño deseado de la ventana

# Configuración para guardar el video
fps = 60
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_filename = f'output_{int(time.time())}.mp4'  # Nombre único basado en el timestamp epoch
out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))
contador = 0
tiempo = fps*60*60
try:
    while contador < tiempo:
        contador += 1
        bucle(frame)
        cv2.imshow('Frame', frame)

        out.write(frame)  # Guardar el frame en el video

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # Cerrar el video correctamente al finalizar
    out.release()
    cv2.destroyAllWindows()
