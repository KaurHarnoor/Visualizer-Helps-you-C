import time

def linear_search(arr, target, draw_data, time_tick):
    for i in range(len(arr)):
        if arr[i] == target:
            draw_data(arr, ["green" if x == i else "white" for x in range(len(arr))])
            return i
        draw_data(arr, ["blue" if x == i else "white" for x in range(len(arr))])
        time.sleep(time_tick)
    return -1

