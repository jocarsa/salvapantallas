import numpy as np
import cv2
import time
import sys

anchura = 1920
altura = 1080
numeroparticulas = 500
particulas = []
tiempo = 0
fps = 60
segundosenminuto = 60
minutos = 60
trails_length = 130  # Length of the trails
trail_fadeout_rate = 8  # Rate at which the trail fades out

class Particula:
    def __init__(self, x, y, vx, vy, m,movible):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.r = np.random.randint(0, 255)
        self.g = np.random.randint(0, 255)
        self.b = np.random.randint(0, 255)
        self.m = m
        self.trail = []  # List to store previous positions
        self.movible = movible

def calculaVelocidad(x1, y1, x2, y2, vx, vy, m1, m2):
    dx = x2 - x1
    dy = y2 - y1
    distancia_squared = dx * dx + dy * dy
    distancia = np.sqrt(distancia_squared)
    factor = (m2 + 1) / distancia

    vx += np.cos(np.arctan2(dy, dx)) * factor
    vy += np.sin(np.arctan2(dy, dx)) * factor

    return vx, vy

# Create immovable massive object at the center
centro_x = anchura // 2
centro_y = altura // 2
centro_m = 4000  # Large mass to make it immovable
particulas.append(Particula(centro_x, centro_y, 0, 0, centro_m,0))

# Inicialización de las partículas
for _ in range(numeroparticulas):
    particulas.append(Particula(
        np.random.random() * anchura,
        np.random.random() * altura,
        np.random.normal(0, 1) * 1000,
        np.random.normal(0, 1) * 1000,
        np.random.random() * 100 + 5,
        1
    ))
for i in range(0,10):
    # Crear el video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    filename = f"stars_screensaver_{int(time.time())}.mp4"
    video = cv2.VideoWriter(filename, fourcc, fps, (anchura, altura))

    try:
        # Bucle principal
        while tiempo < fps*segundosenminuto*minutos:
            if tiempo % fps == 0:
                print(f"{tiempo/fps} segundos")
            frame = np.zeros((altura, anchura, 3), dtype=np.uint8)

            for particula in particulas:
                if particula.movible == 1:
                    particula.x += particula.vx / 1250
                    particula.y += particula.vy / 1250

                for otra_particula in particulas:
                    if particula != otra_particula:
                        
                        particula.vx, particula.vy = calculaVelocidad(
                            particula.x,
                            particula.y,
                            otra_particula.x,
                            otra_particula.y,
                            particula.vx,
                            particula.vy,
                            particula.m,
                            otra_particula.m,
                        )

                # Add current position to the trail
                particula.trail.append((int(particula.x), int(particula.y)))

                # Draw the trail
                for i in range(len(particula.trail) - 1, max(-1, len(particula.trail) - trails_length), -1):
                    if i == -1:
                        break
                    fadeout_factor = 1 - (len(particula.trail) - i) / trails_length
                    trail_color = (max(0, int(particula.b * fadeout_factor)), max(0, int(particula.g * fadeout_factor)), max(0, int(particula.r * fadeout_factor)))
                    cv2.line(frame, particula.trail[i], particula.trail[i - 1], trail_color, thickness=2)

                # If the trail is longer than trails_length, remove the oldest position
                if len(particula.trail) > trails_length:
                    del particula.trail[0]

                cv2.circle(
                    frame, (int(particula.x), int(particula.y)), int(particula.m / 40), (particula.b, particula.g, particula.r), -1
                )

            # Mostrar el frame en la ventana
            cv2.imshow('Frame', frame)
            cv2.waitKey(1)

            # Guardar el frame en el video
            video.write(frame)

            tiempo += 1

    except KeyboardInterrupt:
        print("Interrupción del usuario. Cerrando el video...")

    finally:
        # Finalizar y cerrar el video
        video.release()
        cv2.destroyAllWindows()
        sys.exit(0)
