from PIL import Image, ImageDraw
import random
import time

def create_grid(width, height, rows, cols, min_size, max_size):
    # Create a new blank image
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    # Calculate the size of each square
    cell_width = width / cols
    cell_height = height / rows
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for row in range(rows):
        for col in range(cols):
            # Randomly determine the size of the square
            size = random.randint(min_size, max_size)
            # Calculate the coordinates of the center of the square
            
            center_x = (col + 0.5) * cell_width
            center_y = (row + 0.5) * cell_height
            # Calculate the coordinates of the top-left and bottom-right corners
            x0 = center_x - size / 2
            y0 = center_y - size / 2
            x1 = center_x + size / 2
            y1 = center_y + size / 2
            # Draw the square
            draw.rectangle([x0, y0, x1, y1], fill=color)

    return img


for i in range(0,1000):

    # Parameters
    width = 4096  # Width of the image
    height = 4096  # Height of the image


    max_size = random.randint(5,50)  # Maximum size of each square
    max_size_real = max_size-5  # Maximum size of each square
    min_size = round(max_size/10)  # Minimum size of each square

    rows = round(width/max_size)  # Number of rows in the grid
    cols = round(height/max_size)  # Number of columns in the grid
    
    # Create the grid
    grid_img = create_grid(width, height, rows, cols, min_size, max_size_real)
    epoch_milliseconds = int(time.time() * 1000)
    # Construct the filename
    filename = f"grid_{epoch_milliseconds}.png"

    # Save the image
    grid_img.save(filename)
