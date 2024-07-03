import time

def binary_search(arr, target, draw_data, time_tick):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        draw_data(arr, get_color_array_binary(len(arr), left, mid, right))
        time.sleep(time_tick)
        if arr[mid] == target:
            draw_data(arr, get_color_array_binary(len(arr), left, mid, right, True))
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def get_color_array_binary(length, left, mid, right, found=False):
    color_array = []
    for i in range(length):
        if i == mid:
            color_array.append("blue")
        elif i >= left and i <= right:
            color_array.append("grey")
        else:
            color_array.append("white")
        if found and i == mid:
            color_array[i] = "green"
    return color_array
