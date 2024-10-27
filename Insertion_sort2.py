def insertion_sort(arr):
    # Traverse through elements from index 1 to end of the array
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Shift elements that are greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Insert the key at the correct position

# Test the function
array = [12, 11, 13, 5, 6]
print("Original array:", array)
insertion_sort(array)
print("Sorted array in increasing order:", array)