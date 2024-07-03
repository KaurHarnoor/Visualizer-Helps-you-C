import time

def quick_sort(arr, draw_data, time_tick):
    quick_sort_alg(arr, 0, len(arr)-1, draw_data, time_tick)

def quick_sort_alg(arr, low, high, draw_data, time_tick):
    if low < high:
        pivot_index = partition(arr, low, high, draw_data, time_tick)
        quick_sort_alg(arr, low, pivot_index - 1, draw_data, time_tick)
        quick_sort_alg(arr, pivot_index + 1, high, draw_data, time_tick)

def partition(arr, low, high, draw_data, time_tick):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            draw_data(arr, get_color_array(len(arr), low, high, i, j, True))
            time.sleep(time_tick)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    draw_data(arr, get_color_array(len(arr), low, high, i, high, False))
    time.sleep(time_tick)
    return i + 1

def get_color_array(length, low, high, border, curr_index, is_swapping):
    color_array = []
    for i in range(length):
        if low <= i <= high:
            color_array.append("grey")
        else:
            color_array.append("white")
        
        if i == high:
            color_array[i] = "blue"
        elif i == border:
            color_array[i] = "red"
        elif i == curr_index:
            color_array[i] = "yellow"
        
        if is_swapping:
            if i == border or i == curr_index:
                color_array[i] = "green"
    return color_array
