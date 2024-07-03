import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from algorithms.linear_search import linear_search
from utils.draw_data import draw_data

def run_linear_search():
    data = [64, 34, 25, 12, 22, 11, 90]
    target = 22
    linear_search(data, target, lambda data, color: draw_data(canvas, data, color), time_tick=0.5)

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Linear Search Visualization")
    window.geometry("800x600")

    canvas = tk.Canvas(window, width=800, height=400, bg="white")
    canvas.pack()

    start_button = tk.Button(window, text="Start Linear Search", command=run_linear_search)
    start_button.pack()

    window.mainloop()
