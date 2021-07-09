def bubbleSort(arr):
    n = len(arr)
    var = 0
    # Traverse through all array elements
    for i in range(n - 1):
        
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                var += 1

    print(var)
# Driver code to test above
arr = [5, 4, 1, 3, 2, 6]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i]),