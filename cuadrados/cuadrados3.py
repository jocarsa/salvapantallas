import cv2
import numpy as np
import time
import random

for i in range(0, 10):
    # Define video parameters
    width, height = 3840, 2160
    fps = 60
    duration = 60 * 60  # seconds
    num_frames = fps * duration

    # Create video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    timestamp = int(time.time())
    out = cv2.VideoWriter(f'C:/rendercuadrados_{timestamp}.mp4', fourcc, fps, (width, height))

    # Define grid parameters
    celda = random.randint(32,512)
    proporcion = width/height
    rows, cols = celda, round(celda*proporcion)
    square_size = min(width // cols, height // rows)

    # Generate colors for squares
    colors = [tuple(np.random.randint(0, 255, 3).tolist()) for _ in range(rows * cols)]

    # Generate random frequencies and phase shifts for each square
    frequencies = np.random.uniform(0.1, 0.5, size=(rows, cols))
    phase_shifts = np.random.uniform(0, 2 * np.pi, size=(rows, cols))

    # Generate frames
    for i in range(num_frames):
        # Create blank frame with white background
        frame = np.ones((height, width, 3), dtype=np.uint8) * 255

        # Draw squares
        for row in range(rows):
            for col in range(cols):
                x = (col + 0.5) * (width // cols)
                y = (row + 0.5) * (height // rows)
                frequency = frequencies[row, col]
                phase_shift = phase_shifts[row, col]
                scale = np.sin(2 * np.pi * frequency * i / fps + phase_shift) * 0.25 + 0.75  # Sine wave for smooth shrink and grow
                size = int(square_size * scale / 2)
                color = colors[row * cols + col]
                cv2.rectangle(frame, (int(x - size), int(y - size)), (int(x + size), int(y + size)), color, -1)

        # Display frame buffer
        cv2.imshow('Frame Buffer', frame)
        cv2.waitKey(1)

        # Write frame to video
        out.write(frame)

    # Release video writer
    out.release()

    # Close frame buffer
    # cv2.destroyAllWindows()
