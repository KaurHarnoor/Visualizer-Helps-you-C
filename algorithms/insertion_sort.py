import time

def insertion_sort(arr, draw_data, time_tick):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        draw_data(arr, ["blue" if x == j + 1 or x == i else "white" for x in range(len(arr))])
        time.sleep(time_tick)
    draw_data(arr, ["green" for x in range(len(arr))])
