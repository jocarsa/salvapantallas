import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import random
import time
for i in range(0,10):
    # Load the image and print its size
    strip = Image.open("matrixstrip2.png")
    print(f"Loaded strip image with size: {strip.size}")

    # Set up parameters
    factor = 30
    width, height = 3840, 2160
    num_letters = 1600
    text = "abcdefghijklmnopqrstuvwxyz0123456789"
    font = ImageFont.truetype("matrix.ttf", factor)
    fps = 60
    fotogramas = fps * 60*60  # One minute of video

    # Initialize positions and velocities
    positions_x = [random.randint(0, width // factor) for _ in range(num_letters)]
    positions_y = [random.randint(-200, 0) for _ in range(num_letters)]
    velocities = [random.uniform(2, 5) for _ in range(num_letters)]
    letters = [[random.choice(text) for _ in range(width // factor)] for _ in range(height // factor)]
    # Assign each character a specific row from the strip image
    color_indices = [random.randint(0, strip.height - 1) for _ in range(num_letters)]

    # Probability of changing each character
    change_prob = 0.005

    # Set up video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    filename = f"matrix_screensaver_{int(time.time())}.mp4"
    out = cv2.VideoWriter(filename, fourcc, fps, (width, height))

    # Initialize OpenCV window for framebuffer
    cv2.namedWindow("Matrix Screensaver", cv2.WINDOW_NORMAL)

    # Main loop
    for frame_num in range(fotogramas):
        big_canvas = Image.new("RGB", (width, height), "black")
        big_draw = ImageDraw.Draw(big_canvas)

        # Update positions and redraw letters
        for i in range(num_letters):
            positions_y[i] += velocities[i]
            if positions_y[i] > height:
                positions_x[i] = random.randint(0, width // factor)
                positions_y[i] = random.randint(-200, 0)

            # Draw trailing letters
            for j in range(5):
                trail_y = int(positions_y[i] - factor * j)
                if 0 <= trail_y // factor < len(letters):
                    x_index = positions_x[i]
                    y_index = trail_y // factor
                    if x_index < len(letters[0]):
                        # Get the assigned color for each character from the assigned row
                        color = strip.getpixel((0, color_indices[i]))
                        if j == 0:
                            big_draw.text((x_index * factor, trail_y), letters[y_index][x_index], fill=color, font=font)
                        else:
                            faded_color = tuple(int(c / (j + 1)) for c in color)
                            big_draw.text((x_index * factor, trail_y), letters[y_index][x_index], fill=faded_color, font=font)

        # Update letters less frequently
        for x in range(len(letters[0])):
            for y in range(len(letters)):
                if random.random() < change_prob:
                    letters[y][x] = random.choice(text)

        # Convert big canvas to numpy array
        frame_array = np.array(big_canvas)

        # Show frame in OpenCV window
        cv2.imshow("Matrix Screensaver", frame_array)

        # Write frame to video
        out.write(frame_array)

        # Handle key events to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release video writer and close OpenCV window
    out.release()
    cv2.destroyAllWindows()
    print(f"Video saved as: {filename}")
