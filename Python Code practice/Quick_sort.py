def quick_sort(lst):
    if len(lst)<2:
        return lst
    else:
        pivot = lst[-1]
        smaller,equal,larger = [],[],[]
        for num in lst:
            if num <pivot:
                smaller.append(num)
            elif num ==pivot:
                equal.append(num)
            else:
                larger.append(num)
        return quick_sort(smaller) + equal + quick_sort(larger)

lst = [6,8,1,4,10,7,8,9,3,2,5]

print(quick_sort(lst))