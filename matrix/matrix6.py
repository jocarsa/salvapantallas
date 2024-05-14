import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import random
import time
from colorsys import rgb_to_hsv, hsv_to_rgb

def rgb_to_hsl(rgb):
    r, g, b = rgb
    r, g, b = r / 255.0, g / 255.0, b / 255.0

    max_color = max(r, g, b)
    min_color = min(r, g, b)
    delta = max_color - min_color

    l = (max_color + min_color) / 2.0

    if delta == 0:
        h = s = 0
    else:
        if l < 0.5:
            s = delta / (max_color + min_color)
        else:
            s = delta / (2.0 - max_color - min_color)

        if r == max_color:
            h = (g - b) / delta
        elif g == max_color:
            h = 2.0 + (b - r) / delta
        else:
            h = 4.0 + (r - g) / delta

        h /= 6.0
        if h < 0:
            h += 1.0

    return h, s, l

def hsl_to_rgb(hsl):
    h, s, l = hsl

    if s == 0:
        r = g = b = l
    else:
        def hue_to_rgb(p, q, t):
            if t < 0:
                t += 1
            if t > 1:
                t -= 1
            if t < 1 / 6:
                return p + (q - p) * 6 * t
            if t < 1 / 2:
                return q
            if t < 2 / 3:
                return p + (q - p) * (2 / 3 - t) * 6
            return p

        if l < 0.5:
            q = l * (1 + s)
        else:
            q = l + s - l * s

        p = 2 * l - q
        r = hue_to_rgb(p, q, h + 1 / 3)
        g = hue_to_rgb(p, q, h)
        b = hue_to_rgb(p, q, h - 1 / 3)

    return int(r * 255), int(g * 255), int(b * 255)

def rotate_hue(rgb, hue_rotation):
    hsl = rgb_to_hsl(rgb)
    h, s, l = hsl
    h = (h + hue_rotation) % 1.0
    rotated_rgb = hsl_to_rgb((h, s, l))
    return rotated_rgb

try:
    for i in range(0, 10):
        rotacion = random.random()
        # Load the image and print its size
        strip = Image.open("matrixstrip2.png")
        print(f"Loaded strip image with size: {strip.size}")

        # Set up parameters
        factor = random.randint(10, 60)
        width, height = 3840, 2160
        num_letters = 4600
        text = "abcdefghijklmnopqrstuvwxyz0123456789"
        font = ImageFont.truetype("matrix.ttf", factor)
        fps = 60
        fotogramas = fps * 60 * 60  # One minute of video

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

        # Generate a random hue shift value
        hue_shift = random.random()

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
                            # Apply hue shift to the color
                            #shifted_color = shift_hue(color, hue_shift)
                            original_rgb = color  # Red color
                            hue_rotation = rotacion  # Rotate by half the hue wheel
                            rotated_rgb = rotate_hue(original_rgb, hue_rotation)
                            
                            if j == 0:
                                big_draw.text((x_index * factor, trail_y), letters[y_index][x_index], fill=rotated_rgb, font=font)
                            else:
                                faded_color = tuple(int(c / (j + 1)) for c in rotated_rgb)
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

        print(f"Video saved as: {filename}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Release video writer and close OpenCV window
    out.release()
    cv2.destroyAllWindows()
