import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io

# Set up parameters
width = 1920
height = 1080
fps = 60
num_frames = 30  # Adjust the number of frames to control the length of the video

# Function to generate a frame
def generate_frame(circles, width, height):
    fig = Figure(figsize=(width / 100, height / 100), dpi=100)
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.axis('off')

    # Clear the previous frame
    ax.clear()

    # Draw circles
    for circle in circles:
        ax.add_patch(plt.Circle((circle['x'], circle['y']), 5, color=(circle['r'] / 255, circle['g'] / 255, circle['b'] / 255)))

    # Render the frame as an image
    canvas.draw()
    buf = canvas.buffer_rgba()
    frame = np.asarray(buf)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGRA)

    return frame

# Generate circles
num_circles = 35
circles = [{'x': np.random.random() * width, 'y': np.random.random() * height, 'direction': np.random.random() * np.pi * 2,
            'r': np.random.randint(0, 256), 'g': np.random.randint(0, 256), 'b': np.random.randint(0, 256)} for _ in range(num_circles)]

# Video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_out = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

# Generate frames and write to video
for _ in range(num_frames):
    frame = generate_frame(circles, width, height)
    video_out.write(frame)

# Release resources
video_out.release()
