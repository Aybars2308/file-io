import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import random

class PaintApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Paint")
        self.colors = ["black", "blue", "red", "pink", "purple", "orange", "yellow"]
        self.brush_color = "black"
        self.tool = "pen"  # varsayılan çizim aracı: kalem
        self.brush_size = 2
        self.bg_image = None

        self.canvas_frame = tk.Frame(root, bg="white")
        self.canvas_frame.pack(expand=True, fill="both")

        self.canvas = tk.Canvas(self.canvas_frame, width=600, height=400, bg="white")
        self.canvas.pack(expand=True, fill="both")

        self.setup_toolbar()
        self.canvas.bind("<B1-Motion>", self.draw)

    def setup_toolbar(self):
        self.toolbar = tk.Frame(self.root, bg="white")
        self.toolbar.pack(fill="x")

        self.pen_button = tk.Button(self.toolbar, text="Kalem", command=lambda: self.set_tool("pen"))
        self.pen_button.grid(row=0, column=0, padx=5, pady=5)

        self.brush_button = tk.Button(self.toolbar, text="Fırça", command=lambda: self.set_tool("brush"))
        self.brush_button.grid(row=0, column=1, padx=5, pady=5)

        self.eraser_button = tk.Button(self.toolbar, text="Silgi", command=lambda: self.set_tool("eraser"))
        self.eraser_button.grid(row=0, column=2, padx=5, pady=5)

        self.color_button = tk.Button(self.toolbar, text="Renk Seç", command=self.choose_color)
        self.color_button.grid(row=0, column=3, padx=5, pady=5)

        self.clear_button = tk.Button(self.toolbar, text="Temizle", command=self.clear_canvas)
        self.clear_button.grid(row=0, column=4, padx=5, pady=5)

        self.size_scale = tk.Scale(self.toolbar, from_=1, to=10, orient="horizontal", label="Fırça Boyutu", command=self.change_brush_size)
        self.size_scale.set(self.brush_size)
        self.size_scale.grid(row=0, column=5, padx=5, pady=5)

        self.bg_image_button = tk.Button(self.toolbar, text="Arka Plan Resmi Ekle", command=self.add_background_image)
        self.bg_image_button.grid(row=0, column=6, padx=5, pady=5)

    def draw(self, event):
        if self.tool == "pen":
            x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
            x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
            self.canvas.create_oval(x1, y1, x2, y2, fill=self.brush_color, outline="")
        elif self.tool == "brush":
            x, y = event.x, event.y
            self.canvas.create_rectangle(x, y, x+self.brush_size, y+self.brush_size, fill=self.brush_color, outline="")
        elif self.tool == "eraser":
            x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
            x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="")

    def set_tool(self, tool):
        self.tool = tool

    def choose_color(self):
        self.brush_color = random.choice(self.colors)

    def change_brush_size(self, size):
        self.brush_size = int(size)

    def clear_canvas(self):
        self.canvas.delete("all")

    def add_background_image(self):
        filename = filedialog.askopenfilename(filetypes=[("C://Users//Monster2//Documents//GitHub//file-io//Garticphone arka plan düzeltilmiş.webp")])
        if filename:
            image = Image.open(filename)
            self.bg_image = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image)

root = tk.Tk()
app = PaintApp(root)
root.mainloop()