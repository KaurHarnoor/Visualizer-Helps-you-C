import time

def bubble_sort(arr, draw_data, time_tick):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                draw_data(arr, ["blue" if x == j or x == j+1 else "white" for x in range(len(arr))])
                time.sleep(time_tick)
    draw_data(arr, ["green" for x in range(len(arr))])
