import time
from algorithms.insertion_sort import insertion_sort

def bucket_sort(arr, draw_data, time_tick):
    max_value = max(arr)
    size = max_value // len(arr)

    buckets = [[] for _ in range(len(arr))]
    for i in range(len(arr)):
        j = min(len(arr) - 1, arr[i] // size)
        buckets[j].append(arr[i])
        draw_data(arr, ["blue" if x == i else "white" for x in range(len(arr))])
        time.sleep(time_tick)
    
    arr.clear()
    for bucket in buckets:
        insertion_sort(bucket, draw_data, time_tick)
        arr.extend(bucket)
    
    draw_data(arr, ["green" for x in range(len(arr))])
