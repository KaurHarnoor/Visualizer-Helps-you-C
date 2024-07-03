import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from algorithms.bubble_sort import bubble_sort
from utils.draw_data import draw_data

def run_bubble_sort():
    data = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(data, lambda data, color: draw_data(canvas, data, color), time_tick=0.5)

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Bubble Sort Visualization")
    window.geometry("800x600")

    canvas = tk.Canvas(window, width=800, height=400, bg="white")
    canvas.pack()

    start_button = tk.Button(window, text="Start Bubble Sort", command=run_bubble_sort)
    start_button.pack()

    window.mainloop()
