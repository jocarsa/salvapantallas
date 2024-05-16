@echo off
ffmpeg -framerate 60 -i render/img%%13d.jpg -c:v libx264 -pix_fmt yuv420p output.mp4
pause