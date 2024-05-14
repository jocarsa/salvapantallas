import os
from PIL import Image, ImageDraw, ImageFont
import random
import time

# Function to generate a random alphanumeric character
def generate_random_char():
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    return random.choice(chars)

def get_random_font(fonts_folder):
    fonts = os.listdir(fonts_folder)
    return os.path.join(fonts_folder, random.choice(fonts))

def get_random_color():
    return tuple(random.randint(0, 255) for _ in range(3))

fonts_folder = "fuentes"  # Folder containing fonts

for i in range(100):
    try:
        celda = random.randint(8, 292)
        color = get_random_color()
        # Dimensions of the image
        width = 8192
        height = 8192
        cell_size = celda  # size of each cell
        num_cols = width // cell_size
        num_rows = height // cell_size

        # Create a new blank image
        image = Image.new('RGB', (width, height), color='white')
        draw = ImageDraw.Draw(image)

        # Randomly select a font
        font_path = get_random_font(fonts_folder)
        font = ImageFont.truetype(font_path, celda)

        # Iterate through the cells and draw centered random characters
        for row in range(num_rows):
            for col in range(num_cols):
                char = generate_random_char()
                text_width, text_height = draw.textsize(char, font=font)
                x = col * cell_size + (cell_size - text_width) // 2
                y = row * cell_size + (cell_size - text_height) // 2
                
                draw.text((x, y), char, fill=color, font=font)

        current_epoch = int(time.time())
        # Save the image as PNG
        image.save(f"{current_epoch}_{i}.png")
    except:
        print("uy error")
