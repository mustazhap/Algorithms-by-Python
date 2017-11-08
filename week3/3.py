def sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
       
        return sort(less)+equal+sort(greater)
    
    else:
        return array
        

array = [12,4,25,26,27,23,21,15]
print(sort(array))
