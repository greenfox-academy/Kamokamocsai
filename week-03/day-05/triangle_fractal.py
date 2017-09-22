from tkinter import *
import time
import math

root = Tk()

canvas = Canvas(root, width='600', height='600')
canvas.pack()

size = 590


def draw_triangle(x, y, size):
    canvas.create_polygon(x, y, 
                          x + size, y,
                          x + (size / 2), y + size,
                          outline='black', fill='')




def draw_fractal(x, y, size):
    time.sleep(0.005)
    canvas.update()
    if size < 5:
        return
    else:
        draw_triangle(x, y, size)
        draw_fractal(x, y, size / 2)
        draw_fractal(x + size / 2, y, size / 2)
        draw_fractal(x + size / 4, y + size / 2, size / 2)
    
draw_fractal(10, 10, size)
root.mainloop()