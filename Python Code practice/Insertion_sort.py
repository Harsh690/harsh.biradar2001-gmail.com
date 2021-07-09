def insertion_sort(arr):
    for key in range(1,len(arr)):
        if arr[key]<arr[key-1]:
            i =key
            while i>0 and arr[i]<arr[i-1]:
                arr[i],arr[i-1]=arr[i-1],arr[i]
                i-=1


l = [6,1,8,4,10]
insertion_sort(l)
print(l)
















