import time

def merge_sort(arr, draw_data, time_tick):
    merge_sort_alg(arr, 0, len(arr)-1, draw_data, time_tick)

def merge_sort_alg(arr, left, right, draw_data, time_tick):
    if left < right:
        mid = (left + right) // 2
        merge_sort_alg(arr, left, mid, draw_data, time_tick)
        merge_sort_alg(arr, mid + 1, right, draw_data, time_tick)
        merge(arr, left, mid, right, draw_data, time_tick)

def merge(arr, left, mid, right, draw_data, time_tick):
    left_part = arr[left:mid+1]
    right_part = arr[mid+1:right+1]
    
    left_idx = right_idx = 0
    
    for arr_idx in range(left, right+1):
        if left_idx < len(left_part) and right_idx < len(right_part):
            if left_part[left_idx] <= right_part[right_idx]:
                arr[arr_idx] = left_part[left_idx]
                left_idx += 1
            else:
                arr[arr_idx] = right_part[right_idx]
                right_idx += 1
        elif left_idx < len(left_part):
            arr[arr_idx] = left_part[left_idx]
            left_idx += 1
        else:
            arr[arr_idx] = right_part[right_idx]
            right_idx += 1
    
    draw_data(arr, get_color_array(len(arr), left, mid, right))
    time.sleep(time_tick)

def get_color_array(length, left, mid, right):
    color_array = []
    for i in range(length):
        if left <= i <= right:
            if left <= i <= mid:
                color_array.append("yellow")
            else:
                color_array.append("pink")
        else:
            color_array.append("white")
    return color_array
