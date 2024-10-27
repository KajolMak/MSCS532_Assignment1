def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements smaller than key to one position ahead
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Test the function
array = [5, 2, 9, 1, 5, 6]
insertion_sort(array)
print("Sorted array in decreasing order:", array)
