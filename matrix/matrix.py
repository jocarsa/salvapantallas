import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import random
import time
for i in range(0,20):
    # Set up parameters
    factor = random.randint(15,80)
    width, height = 3840, 2160
    num_letters = 1000
    text = "abcdefghijklmnopqrstuvwxyz0123456789"
    font = ImageFont.truetype("matrix.ttf", factor)
    fps = 60
    segundospominuto = 60
    minutos = 60
    fotogramas = fps*segundospominuto*minutos

    # Initialize positions and velocities
    positions_x = [random.randint(0, width // factor) for _ in range(num_letters)]
    positions_y = [random.randint(-200, 0) for _ in range(num_letters)]
    velocities = [random.random() for _ in range(num_letters)]
    letters = [[random.choice(text) for _ in range(width // factor)] for _ in range(height // factor)]

    # Load strip image and get its color
    strip = Image.open("matrixstrip2.png")

    # Set up video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    filename = f"matrix_screensaver_{int(time.time())}.mp4"
    out = cv2.VideoWriter(filename, fourcc, 30.0, (width, height))
    color_por_defecto = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    # Main loop
    for frame_num in range(fotogramas):  # Generate 300 frames
        # Create images
        big_canvas = Image.new("RGB", (width, height), "black")
        big_draw = ImageDraw.Draw(big_canvas)

        # Update positions
        for i in range(num_letters):
            positions_y[i] += int(velocities[i] * 2)
            if positions_y[i] > height // factor:
                positions_x[i] = random.randint(0, width // factor)
                positions_y[i] = -50

        # Update letters
        for x in range(width // factor):
            for y in range(height // factor):
                if random.random() < 0.02:
                    letters[y][x] = random.choice(text)

        # Draw letters onto big canvas
        for x in range(width // factor):
            for y in range(height // factor):
                try:
                    color = strip.getpixel((positions_x[x], positions_y[y]))  # Get color from strip image
                    color = color_por_defecto
                    big_draw.text((x * factor, y * factor), letters[y][x], fill=color, font=font)
                except IndexError:
                    pass
                    color = color_por_defecto  # Default to white if index out of range
                    big_draw.text((x * factor, y * factor), letters[y][x], fill=color, font=font)

        # Convert big canvas to numpy array
        frame_array = np.array(big_canvas)

        # Display frame
        #cv2.imshow('Frame', frame_array)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        # Write frame to video
        out.write(frame_array)

    # Release video writer
    out.release()

    # Close OpenCV windows
    #cv2.destroyAllWindows()

    print(f"Video saved as: {filename}")
