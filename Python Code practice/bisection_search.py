def search(arr,n):
    first = 0
    last = len(arr)-1

    while True:
        middle = (first + last) // 2
        if n ==arr[middle]:
            return f"{n}found in middle: {middle}"
        elif n >arr[middle]:
            first = middle+1
        else:
            last = middle-1


l = [1,3,4,5,2,9,7,10]
print(search(l,3))
