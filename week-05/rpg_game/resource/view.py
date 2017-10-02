from tkinter import *

size = 720

root = Tk()
root.configure(background ='black')
root.title("Wanderer - RPG Game by Kamo")
canvas = Canvas(root, width=size, height=size, bg="yellow", bd=0)
canvas.pack()



class App:
    def __init__(self):
        self.rect = None
        self.floor = PhotoImage(file = "img/floor.png")
        self.draw_map()

    def hero(self, x, y, size):
        self.rect = canvas.create_rectangle(x, y, x+size, y+size, fill = "black", width=0)

    def move(self, dx, dy):
        canvas.move(self.rect, dx, dy )

    def draw_map(self):
        cell_size = size / 10
        for row in range(10):             
            for column in range(10): 
                cell = canvas.create_image(column * cell_size + 2, row * cell_size + 2, image = self.floor, anchor = 'nw')



myApp = App()

myApp.hero(0, 0, 72)

def on_key_press(e):
    if ( e.keysym == 'Up' ):
        myApp.move(0,-72)
    elif( e.keysym == 'Down' ):
        myApp.move(0,72)
    elif( e.keysym == 'Left' ):
        myApp.move(-72,0)
    elif( e.keysym == 'Right' ):
        myApp.move(72,0)


# Tell the canvas that we prepared a function that can deal with the key press events
root.bind("<KeyPress>", on_key_press)
canvas.pack()

# Select the canvas to be in focused so it actually recieves the key hittings
canvas.focus_set()



root.mainloop()