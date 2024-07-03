import tkinter as tk
from tkinter import ttk
import random
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.selection_sort import selection_sort
from algorithms.bucket_sort import bucket_sort
from algorithms.merge_sort import merge_sort
from algorithms.quick_sort import quick_sort
from algorithms.linear_search import linear_search
from algorithms.binary_search import binary_search
from utils.draw_data import draw_data

def create_window():
    window = tk.Tk()
    window.title("Algorithm Visualizer")
    window.geometry("800x600")
    return window

def generate(canvas, window):
    global data
    data = [random.randint(1, 100) for _ in range(50)]
    draw_data(canvas, data, ["red" for _ in range(len(data))])

def start_algorithm(algo_name, canvas, window, speed):
    if algo_name == "Bubble Sort":
        bubble_sort(data, lambda data, color: draw_data(canvas, data, color), speed)
    elif algo_name == "Insertion Sort":
        insertion_sort(data, lambda data, color: draw_data(canvas, data, color), speed)
    elif algo_name == "Selection Sort":
        selection_sort(data, lambda data, color: draw_data(canvas, data, color), speed)
    elif algo_name == "Bucket Sort":
        bucket_sort(data, lambda data, color: draw_data(canvas, data, color), speed)
    elif algo_name == "Merge Sort":
        merge_sort(data, lambda data, color: draw_data(canvas, data, color), speed)
    elif algo_name == "Quick Sort":
        quick_sort(data, lambda data, color: draw_data(canvas, data, color), speed)
    elif algo_name == "Linear Search":
        linear_search(data, random.choice(data), lambda data, color: draw_data(canvas, data, color), speed)
    elif algo_name == "Binary Search":
        binary_search(data, random.choice(data), lambda data, color: draw_data(canvas, data, color), speed)

if __name__ == "__main__":
    window = create_window()
    
    canvas = tk.Canvas(window, width=800, height=400, bg="white")
    canvas.grid(row=0, column=0, padx=10, pady=5)
    
    frame = tk.Frame(window, width=600, height=200, bg="grey")
    frame.grid(row=1, column=0, padx=10, pady=5)
    
    algo_menu = tk.StringVar()
    algo_menu.set("Bubble Sort")
    menu = ttk.Combobox(frame, textvariable=algo_menu, values=["Bubble Sort", "Insertion Sort", "Selection Sort", "Bucket Sort", "Merge Sort", "Quick Sort", "Linear Search", "Binary Search"])
    menu.grid(row=0, column=0, padx=5, pady=5)
    
    speed_scale = tk.Scale(frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=tk.HORIZONTAL, label="Select Speed [s]")
    speed_scale.grid(row=0, column=1, padx=5, pady=5)
    
    generate_button = tk.Button(frame, text="Generate Array", command=lambda: generate(canvas, window))
    generate_button.grid(row=0, column=2, padx=5, pady=5)
    
    start_button = tk.Button(frame, text="Start", command=lambda: start_algorithm(algo_menu.get(), canvas, window, speed_scale.get()))
    start_button.grid(row=0, column=3, padx=5, pady=5)
    
    window.mainloop()
