import matplotlib.pyplot as plt
import io 
import tkinter as tk
from PIL import Image, ImageTk
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backend_bases import FigureManagerBase

class FigureCanvasTkAgg(FigureCanvasAgg):
    def __init__(self, figure):
        super().__init__(figure)
    
    @classmethod
    def new_manager(cls, figure, *args, **kwarg):
        canvas = cls(figure)
        manager = FigureManager(canvas, 1)
        return manager
    
class FigureManager(FigureManagerBase):
    def __init__(self, canvas, num):
        super().__init__(canvas, num)
    
    @staticmethod
    def pyplot_show(*args, **kwargs):

        canvas = plt.gcf().canvas
        buf = io.BytesIO()
        canvas.figure.savefig(buf, format='png')
        buf.seek = 0

        root = tk.Tk()
        root.title("Matplotlib Figure")

        img  = Image.open(buf)
        photo = ImageTk.PhotoImage(img)
        
        label = tk.label(root, image=photo)
        label.pack()

        root.mainloop()

