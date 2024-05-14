import cv2
import numpy as np
import os

# Define video properties
width, height = 1920, 1080
fps = 60
duration = 60*60  # seconds

rojo = [0, 50, 100, 150, 200, 255]
verde = [0, 50, 100, 150, 200, 255]
azul = [0, 50, 100, 150, 200, 255]

for r in rojo:
    for v in verde:
        for a in azul:
            color_rgb = (r, v, a)  # Solid background color (RGB format - Red in this case)

            output_filename = f'output_video_RGB_{color_rgb[0]}_{color_rgb[1]}_{color_rgb[2]}.mp4'

            # Check if the file already exists
            if not os.path.exists(output_filename):
                # Create a blank image with the solid color
                frame = np.ones((height, width, 3), dtype=np.uint8)
                frame[:, :] = color_rgb[::-1]  # Filling the entire frame with the specified color (reversed for BGR)

                # Create a video writer object
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                video_writer = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

                # Write the same frame for the entire duration
                for _ in range(duration * fps):
                    video_writer.write(frame)

                # Release the video writer
                video_writer.release()

                print(f"Video saved as '{output_filename}'")
            else:
                print(f"File '{output_filename}' already exists. Skipping...")
