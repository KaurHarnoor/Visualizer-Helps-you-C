import time

def selection_sort(arr, draw_data, time_tick):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw_data(arr, ["blue" if x == i or x == min_idx else "white" for x in range(len(arr))])
        time.sleep(time_tick)
    draw_data(arr, ["green" for x in range(len(arr))])
